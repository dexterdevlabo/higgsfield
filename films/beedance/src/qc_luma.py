#!/usr/bin/env python3
"""Per-frame luminance floor check.

blackdetect is the wrong instrument for a dark vertical palette: on a 1080x1920
frame of #0C1018 with white type, most pixels are legitimately dark, so it fires
on perfectly good end cards. This checks instead that every frame carries real
content — a minimum mean luma AND a bright extreme somewhere in frame.
"""
import subprocess, sys, numpy as np
SRC, W, H = sys.argv[1], 1080, 1920
MEAN_FLOOR, MAX_FLOOR = 6.0, 120
p = subprocess.run(['ffmpeg','-v','error','-i',SRC,'-f','rawvideo','-pix_fmt','gray','-'],
                   capture_output=True)
buf = np.frombuffer(p.stdout, dtype=np.uint8)
n = len(buf)//(W*H)
frames = buf[:n*W*H].reshape(n, H*W)
means, maxes = frames.mean(axis=1), frames.max(axis=1)
bad = [(i, means[i], maxes[i]) for i in range(n)
       if means[i] < MEAN_FLOOR or maxes[i] < MAX_FLOOR]
print(f"{n} frames · mean luma {means.min():.1f}–{means.max():.1f} · "
      f"darkest frame {means.argmin()} ({means.argmin()/30:.2f}s)")
if bad:
    print(f"FAIL {len(bad)} frame(s) under floor (mean<{MEAN_FLOOR} or max<{MAX_FLOOR}):")
    for i, m, mx in bad[:12]:
        print(f"  frame {i} ({i/30:.2f}s) mean={m:.1f} max={mx}")
    sys.exit(1)
print("PASS every frame carries content")
