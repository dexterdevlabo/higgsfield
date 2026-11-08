#!/usr/bin/env python3
"""Procedural base plate: the static surface every clip is laid on.
Deterministic (fixed seed), so the same plate rebuilds byte-identically.
  A cool editing bench · B warm archive desk · C steel projection room"""
import numpy as np
from PIL import Image, ImageFilter
W, H, SEED = 1920, 1080, 7

def fields():
    rng = np.random.default_rng(SEED)
    acc = np.zeros((H, W), np.float32)
    for sc, amp in [(2, 1.0), (5, .55), (13, .3), (31, .16), (71, .09)]:
        n = rng.random((max(2, H // sc), max(2, W // sc))).astype(np.float32)
        acc += amp * np.asarray(Image.fromarray((n * 255).astype(np.uint8))
                                .resize((W, H), Image.BICUBIC), np.float32) / 255
    acc = (acc - acc.min()) / (acc.max() - acc.min())
    fib = np.asarray(Image.fromarray((acc * 255).astype(np.uint8))
                     .filter(ImageFilter.GaussianBlur(0.4)), np.float32) / 255
    fib = 0.5 * fib + 0.5 * np.roll(fib, 3, axis=1)      # anisotropic weave
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt(((xx - W * .5) / (W * .52)) ** 2 + ((yy - H * .42) / (H * .60)) ** 2)
    lamp = np.clip(1.0 / (1.0 + 2.3 * d * d), 0, 1)       # inverse-square pool
    return fib, lamp, rng

def plate(path, base, warm, strength=.18):
    fib, lamp, rng = fields()
    b = np.array(base, np.float32) / 255.0
    img = np.zeros((H, W, 3), np.float32)
    for c in range(3):
        v = b[c] * (0.20 + 1.35 * lamp)
        v = v * (1.0 + strength * (fib - 0.5) * 2.0)
        img[:, :, c] = v + warm[c] * lamp * 0.10
    img = np.clip(img + rng.normal(0, .012, (H, W, 1)).astype(np.float32), 0, 1)
    Image.fromarray((img * 255).astype(np.uint8)).save(path)
    print(f"{path}  mean luma {img.mean()*255:.1f}")

if __name__ == "__main__":
    plate("assets/surf_A.png", (34, 44, 50), (.10, .07, .02))
    plate("assets/surf_B.png", (58, 48, 32), (.14, .09, .02))
    plate("assets/surf_C.png", (38, 43, 52), (.06, .07, .10), .10)
