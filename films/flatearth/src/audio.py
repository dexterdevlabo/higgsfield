#!/usr/bin/env python3
"""Sound design for THE SHORT WHY — "why the Earth is not flat" (10s).

Synthesised from scratch with numpy — no sourced audio, so nothing to licence.
Follows references/sound-design.md: events attach to on-screen motion, effects
lead the cut by ~0.14s, one sub impact per beat boundary, and a quiet bed underneath.
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
bed = onepole_lp(rng.normal(0, 1, N), 110)
bed /= (np.max(np.abs(bed)) + 1e-9)
bed *= 0.075
fi, fo = int(0.7 * SR), int(1.0 * SR)
bed[:fi] *= np.linspace(0, 1, fi)
bed[-fo:] *= np.linspace(1, 0, fo)
bed *= 0.75 + 0.25 * np.sin(2 * np.pi * 0.14 * np.arange(N) / SR)
mix += bed

# ---- S1 the exhibit 0.00 ----
sub(0.00, f0=78, f1=46, gain=0.74)
swell(0.00, dur=0.55, gain=0.20)
tick(0.08, tone=2500, gain=0.16)
paper(0.26, gain=0.22)                      # the map lands like a sheet on a table
tick(0.86, tone=3100, gain=0.16)            # ring

# ---- S2 the turn 2.30 ----
whoosh(2.16, dur=0.30, gain=0.36)
sub(2.32, f0=64, f1=40, dur=0.50, gain=0.54)
tick(2.62, tone=2200, gain=0.14)

# ---- S3 the proof 4.20 ----
whoosh(4.06, dur=0.32, gain=0.38)
tick(4.26, tone=2400, gain=0.14)
tick(4.36, tone=2200, gain=0.14)
swell(4.62, dur=2.40, gain=0.10)            # the long sail away
tick(6.10, tone=2000, gain=0.13)
tick(6.55, tone=1700, gain=0.17)            # "the hull goes first"
sub(6.90, f0=68, f1=38, dur=0.70, gain=0.72)  # payoff

# ---- S4 end card 7.95 ----
whoosh(7.79, dur=0.38, gain=0.42)
sub(7.95, f0=72, f1=36, dur=0.85, gain=0.80)
tick(8.54, tone=2100, gain=0.14)
tick(8.80, tone=2600, gain=0.20)
swell(9.05, dur=0.85, gain=0.11)

# ---------------------------------------------------------------- master
peak = np.max(np.abs(mix))
if peak > 0: mix *= min(1.0, 0.89 / peak)
t_ = int(0.3 * SR); mix[-t_:] *= np.linspace(1, 0, t_)
st = np.stack([mix, mix], axis=1)
pcm = (st * 32767).astype(np.int16)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'audio', 'mix.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(f"wrote mix.wav  {DUR}s  peak={np.max(np.abs(mix)):.3f}")
