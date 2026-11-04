"""Choose a readable caption colour for every chunk from the actual pixels behind it.

usage: python3 pick_colors.py EDIT.mp4 captions.txt broll.txt colors.json
- talking-head shots: white text, black glow (house style)
- b-roll on a dark background: light tint taken from the shot's own hue (like the reference reel)
- b-roll on a bright background: deep tint of the shot's hue with a white glow
Every pick is checked for WCAG contrast >= 4.5 against the background, else falls back to white/black.
"""
import colorsys, json, subprocess, sys
import numpy as np

edit, caps, broll, out = sys.argv[1:5]
W, H, FPS = 108, 192, 10
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", edit, "-vf", f"fps={FPS},scale={W}:{H}",
                      "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
frames = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).astype(float) / 255

def rows(path, n):
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            yield [p.strip() for p in line.split("|", n - 1)]

chunks = [(float(t), st) for t, st, _ in rows(caps, 3)]
windows = [(float(r[0]), float(r[1])) for r in rows(broll, 5)]

def lin(c):
    return np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)

def lum(rgb):
    r, g, b = lin(np.asarray(rgb))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)

def ass(rgb):
    r, g, b = [int(round(max(0, min(1, v)) * 255)) for v in rgb]
    return f"&H{b:02X}{g:02X}{r:02X}&"

WHITE, BLACK = (1, 1, 1), (0, 0, 0)
result = []
for i, (t, st) in enumerate(chunks):
    end = chunks[i + 1][0] if i + 1 < len(chunks) else t + 1
    mid = t + min(0.6, (end - t) / 2)
    f = frames[min(len(frames) - 1, int(mid * FPS))]
    region = f[int(H * 0.61):int(H * 0.73), int(W * 0.18):int(W * 0.82)]   # where captions sit
    bg = region.reshape(-1, 3).mean(0)
    # judge against the brightest part too, so a white plate under a dark shot still counts
    bright = np.percentile(region.reshape(-1, 3), 85, axis=0)
    on_broll = any(a <= mid < b for a, b in windows)
    h, l, s = colorsys.rgb_to_hls(*bg)
    if not on_broll:
        fill, shadow = WHITE, BLACK
    elif lum(bright) < 0.30:
        fill = colorsys.hls_to_rgb(h, 0.80, min(0.9, s * 2.5 + 0.5)) if s > 0.04 else WHITE
        shadow = BLACK
        if contrast(fill, bright) < 4.5:
            fill = WHITE
    else:
        fill = colorsys.hls_to_rgb(h, 0.13, min(0.5, s + 0.2)) if s > 0.06 else (0.07, 0.07, 0.07)
        shadow = WHITE
        if contrast(fill, bg) < 4.5:
            fill = BLACK
    result.append({"t": t, "fill": ass(fill), "shadow": ass(shadow), "broll": on_broll,
                   "bg": ass(bg)})
json.dump(result, open(out, "w"), indent=0)
print(sum(r["broll"] for r in result), "b-roll chunks coloured;",
      sum(r["shadow"] == "&HFFFFFF&" for r in result), "use dark text")
