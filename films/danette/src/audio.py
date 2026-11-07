#!/usr/bin/env python3
"""Sound design for the Danette concept film (15s).

Synthesised from scratch with numpy — no sourced audio, so nothing to licence.
Follows references/sound-design.md: events attach to on-screen motion, effects
lead the cut by ~0.14s, one sub impact per beat boundary, and a quiet bed underneath.
"""
import numpy as np, wave, os

SR, DUR = 48000, 15.0
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
# Warm and soft for a food brand: a low pad rather than the documentary drone.
bed = onepole_lp(rng.normal(0, 1, N), 160)
bed /= (np.max(np.abs(bed)) + 1e-9)
bed *= 0.10
fi, fo = int(1.0 * SR), int(1.6 * SR)
bed[:fi] *= np.linspace(0, 1, fi)
bed[-fo:] *= np.linspace(1, 0, fo)
bed *= 0.72 + 0.28 * np.sin(2 * np.pi * 0.10 * np.arange(N) / SR)
mix += bed

# a gentle warm tone under the whole film, two soft fifths
for f, g in ((110.0, 0.030), (164.5, 0.020)):
    tt = np.arange(N) / SR
    pad = np.sin(2 * np.pi * f * tt) * g
    env_ = np.clip(np.sin(np.pi * tt / DUR), 0, 1) ** 0.7
    mix += pad * env_

# ---- S1 the swirl 0.00 ----
swell(0.00, dur=0.80, gain=0.20)
sub(0.00, f0=66, f1=40, dur=0.60, gain=0.46)      # soft, not a documentary impact
tick(0.30, tone=2100, gain=0.11)
swell(0.10, dur=2.00, gain=0.13)                  # the pipe-on, long and soft
tick(0.52, tone=1800, gain=0.10)

# ---- S2 three flavours 3.30 ----
whoosh(3.18, dur=0.30, gain=0.28)
for i in range(3):
    paper(3.44 + i * 0.12, gain=0.16)             # each column rising
    tick(3.76 + i * 0.12, tone=1900 + i * 150, gain=0.10)

# ---- S3 the number 6.40 ----
whoosh(6.28, dur=0.28, gain=0.28)
sub(6.58, f0=70, f1=42, dur=0.62, gain=0.60)      # the number lands
tick(6.98, tone=2000, gain=0.11)

# ---- S4 the slogan stands up 9.40 ----
whoosh(9.28, dur=0.30, gain=0.30)
for i in range(4):
    tick(9.56 + i * 0.17, tone=1500 + i * 190, gain=0.15)   # one per word standing
sub(10.24, f0=64, f1=38, dur=0.70, gain=0.56)

# ---- S5 lockup 12.60 ----
whoosh(12.46, dur=0.36, gain=0.36)
sub(12.60, f0=72, f1=36, dur=0.95, gain=0.74)
tick(13.26, tone=2200, gain=0.12)
swell(13.40, dur=1.30, gain=0.13)

# ---------------------------------------------------------------- master
peak = np.max(np.abs(mix))
if peak > 0: mix *= min(1.0, 0.89 / peak)
t_ = int(0.35 * SR); mix[-t_:] *= np.linspace(1, 0, t_)
st = np.stack([mix, mix], axis=1)
pcm = (st * 32767).astype(np.int16)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'audio', 'mix.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(f"wrote mix.wav  {DUR}s  peak={np.max(np.abs(mix)):.3f}")
