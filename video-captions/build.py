"""Full edit: original + colour-matched b-roll + adaptive-colour captions + music & SFX (+ optional outro).

usage: python3 build.py ORIGINAL BROLL_DIR AUDIO_DIR OUT.mp4 [OUTRO.mp4]
Files used from this folder: captions.txt, broll.txt, grade.json (from grade.py), sfx.txt
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
src, bdir, adir, out = sys.argv[1:5]
outro = sys.argv[5] if len(sys.argv) > 5 else None
tmp = os.path.join(bdir, "_build"); os.makedirs(tmp, exist_ok=True)
P = lambda n: os.path.join(HERE, n)

def run(cmd):
    subprocess.run(cmd, check=True)

def rows(path, n):
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            yield [p.strip() for p in line.split("|", n - 1)]

def probe(path, entries="stream=width,height", sel=["-select_streams", "v"]):
    return subprocess.run(["ffprobe", "-v", "error", *sel, "-show_entries", entries, "-of", "csv=p=0",
                           path], capture_output=True, text=True).stdout.strip()

DUR = float(probe(src, "format=duration", []))
grade = json.load(open(P("grade.json")))

# ---- 1. picture edit: base + graded b-roll with matching grain (no captions yet) ----
inputs, fc, last = ["-i", src], ["[0:v]scale=1080:1920:flags=lanczos,setsar=1[base0]"], "base0"
for i, (s, e, cid, off, fx) in enumerate(rows(P("broll.txt"), 5), start=1):
    s, e, off, fx = float(s), float(e), float(off), float(fx)
    path = os.path.join(bdir, f"{cid}.mp4")
    w, h = map(int, probe(path).split(",")[:2])
    inputs += ["-ss", str(off), "-t", str(e - s + 0.1), "-i", path]
    if fx < 0:   # subject on black: centre-crop to the top 1250px, caption sits on black below
        geo = "scale=-2:1250:flags=lanczos,crop=1080:1250,pad=1080:1920:0:0:black"
    else:        # cover-fit, crop horizontally around the focus point
        sw = round(w * 1920 / h / 2) * 2; sh = 1920
        if sw < 1080:
            sw, sh = 1080, round(h * 1080 / w / 2) * 2
        cx = max(0, min(sw - 1080, round(sw * fx - 540)))
        geo = f"scale={sw}:{sh}:flags=lanczos,crop=1080:1920:{cx}:{(sh - 1920) // 2}"
    fc.append(f"[{i}:v]fps=24,{geo},setsar=1,format=rgb24,{grade[cid]},format=yuv420p,"
              f"noise=alls=7:allf=t,setpts=PTS-STARTPTS+{s}/TB[b{i}]")
    fc.append(f"[{last}][b{i}]overlay=eof_action=pass:enable='between(t,{s},{e})'[base{i}]")
    last = f"base{i}"
edit = os.path.join(tmp, "edit.mp4")
run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", f"[{last}]",
     "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p", edit])

# ---- 2. caption colours from the real pixels, then the subtitle file ----
colors = os.path.join(tmp, "colors.json")
run([sys.executable, P("pick_colors.py"), edit, P("captions.txt"), P("broll.txt"), colors])
ass = os.path.join(tmp, "caps.ass")
run([sys.executable, P("make_ass.py"), P("captions.txt"), ass, "1290", str(DUR - 0.1), colors])

# ---- 3+4. final: captions on the edit (+ outro), voice + ducked music + sound effects ----
vin = ["-i", edit] + (["-i", outro] if outro else [])
A = len(vin) // 2                      # index of the first audio input
vf = f"[0:v]ass={ass},setsar=1[main]"
vf += (";[1:v]scale=1080:1920,fps=24,setsar=1,format=yuv420p[o];[main][o]concat=n=2:v=1:a=0[v]"
       if outro else ";[main]null[v]")
total = DUR + (float(probe(outro, "format=duration", [])) if outro else 0)
fmt = "aformat=sample_rates=48000:channel_layouts=stereo"
ain = ["-i", src, "-i", os.path.join(adir, "music.mp3")]
af = [f"[{A}:a]{fmt},asplit=2[voice][key]",
      f"[{A + 1}:a]{fmt},atrim=0:{total + 1},volume=0.22,afade=t=in:d=1.5[mus0]",
      "[mus0][key]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[mus]"]
mix = ["[voice]", "[mus]"]
sfx = []
for t, name, vol in rows(P("sfx.txt"), 3):
    if t.startswith("+"):            # "+x" = seconds into the outro
        if not outro:
            continue
        t = DUR + float(t[1:])
    sfx.append((float(t), name, vol))
for j, (t, name, vol) in enumerate(sfx):
    ain += ["-i", os.path.join(adir, name)]
    ms = max(0, int(t * 1000))
    af.append(f"[{A + 2 + j}:a]{fmt},volume={vol},adelay={ms}|{ms}[s{j}]")
    mix.append(f"[s{j}]")
af.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=longest,"
          f"atrim=0:{total},afade=t=out:st={total - 2}:d=2,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]")
run(["ffmpeg", "-v", "error", "-y", *vin, *ain, "-filter_complex", vf + ";" + ";".join(af),
     "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
     "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
print("wrote", out)
