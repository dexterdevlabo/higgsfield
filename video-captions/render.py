"""Render: original video + b-roll cutaways + burned captions.

usage: python3 render.py ORIGINAL BROLL_DIR OUT.mp4 [--preview T]
Reads broll.txt, captions.txt from this folder; builds caps.ass via make_ass.py.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
src, bdir, out = sys.argv[1], sys.argv[2], sys.argv[3]
preview = float(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[4] == "--preview" else None

ass = os.path.join(HERE, "caps.ass")
subprocess.run([sys.executable, os.path.join(HERE, "make_ass.py"),
                os.path.join(HERE, "captions.txt"), ass, "1290"], check=True)

def probe(path):
    w, h = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries",
                           "stream=width,height", "-of", "csv=p=0", path],
                          capture_output=True, text=True).stdout.strip().split(",")[:2]
    return int(w), int(h)

rows = []
for line in open(os.path.join(HERE, "broll.txt")):
    line = line.strip()
    if line and not line.startswith("#"):
        s, e, cid, off, fx = [p.strip() for p in line.split("|")]
        rows.append((float(s), float(e), cid, float(off), float(fx)))

inputs = ["-i", src]
fc = ["[0:v]scale=1080:1920:flags=lanczos,setsar=1[base0]"]
last = "base0"
for i, (s, e, cid, off, fx) in enumerate(rows, start=1):
    path = os.path.join(bdir, f"{cid}.mp4")
    w, h = probe(path)
    dur = e - s
    inputs += ["-ss", f"{off}", "-t", f"{dur + 0.1}", "-i", path]
    # cover-fit to 1080x1920, crop horizontally around the focus point
    if fx < 0:   # subject on black: centre-crop to the top 1250px, caption sits on black below
        geo = "scale=-2:1250:flags=lanczos,crop=1080:1250,pad=1080:1920:0:0:black"
    else:        # cover-fit, crop horizontally around the focus point
        sh = 1920
        sw = round(w * sh / h / 2) * 2
        if sw < 1080:
            sw, sh = 1080, round(h * 1080 / w / 2) * 2
        cx = max(0, min(sw - 1080, round(sw * fx - 540)))
        geo = f"scale={sw}:{sh}:flags=lanczos,crop=1080:1920:{cx}:{(sh - 1920) // 2}"
    fc.append(f"[{i}:v]fps=24,{geo},setsar=1,eq=saturation=0.92:brightness=-0.06,"
              f"setpts=PTS-STARTPTS+{s}/TB[b{i}]")
    fc.append(f"[{last}][b{i}]overlay=eof_action=pass:enable='between(t,{s},{e})'[base{i}]")
    last = f"base{i}"
fc.append(f"[{last}]ass={ass}[v]")

cmd = ["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", ";".join(fc),
       "-map", "[v]", "-map", "0:a"]
if preview is not None:
    cmd += ["-ss", str(preview), "-frames:v", "1", out]
else:
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
subprocess.run(cmd, check=True)
print("wrote", out)
