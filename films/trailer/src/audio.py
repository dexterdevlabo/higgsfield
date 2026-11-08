#!/usr/bin/env python3
"""Sound design for the kite trailer.

Synthesised from scratch with numpy — no sourced audio, so nothing to licence.
Follows references/sound-design.md: events attach to on-screen motion, effects
lead the cut by 2-3 frames (~0.08s at 30fps), one sub impact per shot boundary,
and a near-inaudible bed underneath.
"""
import numpy as np, wave, os

SR, DUR = 48000, 10.0
N = int(SR * DUR)
mix = np.zeros(N, dtype=np.float64)
rng = np.random.default_rng(7)


def place(sig, t):
    """Add sig into the mix at time t (seconds), clipped to length."""
    i = int(t * SR)
    if i < 0:
        sig, i = sig[-i:], 0
    n = min(len(sig), N - i)
    if n > 0:
        mix[i:i + n] += sig[:n]


def env(n, attack, decay, power=2.0):
    a = int(attack * SR)
    e = np.ones(n)
    if a > 0:
        e[:a] = np.linspace(0, 1, a) ** 0.6
    d = n - a
    if d > 0:
        e[a:] = np.linspace(1, 0, d) ** power
    return e


def onepole_lp(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def onepole_hp(x, cutoff):
    return x - onepole_lp(x, cutoff)


def sub(t, f0=58, f1=38, dur=0.52, gain=0.72):
    """Low-frequency impact: a short downward pitch drop. One per shot boundary."""
    n = int(dur * SR)
    tt = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-tt * 9)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * env(n, 0.004, dur - 0.004, 2.6)
    click = onepole_hp(rng.normal(0, 1, n), 1800) * env(n, 0.0005, 0.02, 3) * 0.18
    place((body + click) * gain, t)


def tick(t, tone=2600, dur=0.055, gain=0.20):
    """Type / card / annotation tick: a thin transient on the first frame of movement."""
    n = int(dur * SR)
    tt = np.arange(n) / SR
    s = np.sin(2 * np.pi * tone * tt) * 0.5 + onepole_hp(rng.normal(0, 1, n), 2000) * 0.5
    place(s * env(n, 0.0008, dur, 3.4) * gain, t)


def whoosh(t, dur=0.30, gain=0.34, up=True):
    """Dark directional whoosh for a cut. Leads the cut by ~0.08s at the call site."""
    n = int(dur * SR)
    noise = rng.normal(0, 1, n)
    lo = onepole_lp(noise, 900)
    bp = onepole_hp(lo, 160)
    sweep = np.linspace(0.25, 1.0, n) if up else np.linspace(1.0, 0.25, n)
    e = env(n, dur * 0.42, dur * 0.58, 1.9)
    place(bp * sweep * e * gain, t)


def swell(t, dur=0.55, gain=0.20):
    """Soft air swell under a reveal."""
    n = int(dur * SR)
    s = onepole_lp(rng.normal(0, 1, n), 520)
    place(s * env(n, dur * 0.72, dur * 0.28, 1.5) * gain, t)


def paper(t, dur=0.14, gain=0.17):
    """Card / paper movement for the collage."""
    n = int(dur * SR)
    s = onepole_hp(onepole_lp(rng.normal(0, 1, n), 5200), 1100)
    place(s * env(n, 0.006, dur, 2.4) * gain, t)


# ---------------------------------------------------------------- bed
bed = onepole_lp(rng.normal(0, 1, N), 95)
bed /= (np.max(np.abs(bed)) + 1e-9)
bed *= 0.085
fi, fo = int(1.2 * SR), int(1.4 * SR)
bed[:fi] *= np.linspace(0, 1, fi)
bed[-fo:] *= np.linspace(1, 0, fo)
# slow breathing so the bed is not static
bed *= 0.75 + 0.25 * np.sin(2 * np.pi * 0.11 * np.arange(N) / SR)
mix += bed

# ------------------------------------------------- S1 · Harunobu 0.00
sub(0.00, gain=0.80)
swell(0.00, dur=0.70, gain=0.22)
tick(0.22); tick(0.28, tone=2300); tick(0.34, tone=2050)   # word stagger
swell(0.88, dur=0.50, gain=0.16)                           # ring draws on the kite
tick(0.92, tone=3100, gain=0.14)

# ------------------------------------------------- S2 · Perkins 2.60
whoosh(2.44, dur=0.34, gain=0.38)                          # leads the cut by 0.16s
sub(2.78, f0=62, f1=40, gain=0.66)                         # "1910" lands
tick(2.86, tone=2400, gain=0.15)
tick(3.46, tone=1900, gain=0.17)                           # ring on the man
tick(3.74, tone=2700, gain=0.13)                           # leader line
tick(3.92, tone=2200, gain=0.18)                           # chip

# ------------------------------------------------- S3 · collage 5.20
whoosh(5.04, dur=0.32, gain=0.36)
for i in range(4):                                         # four cards
    paper(5.30 + i * 0.09, gain=0.19)
    tick(5.52 + i * 0.09, tone=2000 + i * 180, gain=0.10)
swell(5.84, dur=0.46, gain=0.13)                           # rule sweep

# ------------------------------------------------- S4 · title 7.45
whoosh(7.29, dur=0.40, gain=0.42, up=True)
sub(7.45, f0=66, f1=34, dur=0.95, gain=0.85)               # mask opens
tick(8.06, tone=1700, gain=0.14)
swell(8.30, dur=0.90, gain=0.10)

# ---------------------------------------------------------------- master
peak = np.max(np.abs(mix))
if peak > 0:
    mix *= min(1.0, 0.89 / peak)                           # headroom, no clipping
tail = int(0.35 * SR)
mix[-tail:] *= np.linspace(1, 0, tail)

st = np.stack([mix, mix], axis=1)                          # mono content, stereo file
pcm = (st * 32767).astype(np.int16)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'audio', 'mix.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(f"wrote mix.wav  {DUR}s  peak={np.max(np.abs(mix)):.3f}")
