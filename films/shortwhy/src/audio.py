#!/usr/bin/env python3
"""Sound design for THE SHORT WHY (15s vertical trailer).

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
bed = onepole_lp(rng.normal(0, 1, N), 110)
bed /= (np.max(np.abs(bed)) + 1e-9)
bed *= 0.075
fi, fo = int(0.8 * SR), int(1.2 * SR)
bed[:fi] *= np.linspace(0, 1, fi)
bed[-fo:] *= np.linspace(1, 0, fo)
bed *= 0.75 + 0.25 * np.sin(2 * np.pi * 0.13 * np.arange(N) / SR)
mix += bed

# Mixed for phone speakers: more mid presence, less sub than the long-form spec,
# because a phone reproduces almost nothing below 200 Hz.

# ---- S1 hook 0.00 ----
sub(0.00, f0=78, f1=46, gain=0.74)
swell(0.00, dur=0.60, gain=0.20)
tick(0.00, tone=2600); tick(0.07, tone=2350); tick(0.14, tone=2100)   # three hook lines
swell(1.05, dur=0.44, gain=0.17)                                      # Greenland lights up
tick(1.05, tone=3200, gain=0.16)
tick(2.02, tone=2200, gain=0.15)                                      # payoff line
whoosh(2.78, dur=0.62, gain=0.30, up=False)                           # the shrink travels
sub(3.52, f0=70, f1=42, dur=0.58, gain=0.70)                          # "14x" lands
tick(3.52, tone=1800, gain=0.18)

# ---- S2 economics 4.40 ----
whoosh(4.26, dur=0.30, gain=0.36)
tick(4.55, tone=2400, gain=0.15)
for i in range(5):
    paper(4.62 + i * 0.07, gain=0.15)                                 # five bars

# ---- S3 psychology 6.40 ----
whoosh(6.26, dur=0.30, gain=0.36)
tick(6.55, tone=2400, gain=0.15)
for i in range(8):
    tick(6.62 + i * 0.035, tone=2800 + i * 60, gain=0.07)             # name assembles
for n in range(8):
    tick(7.42 + n * 0.055, tone=1500 - n * 80, gain=0.06)             # and decays

# ---- S4 history 8.40 ----
whoosh(8.26, dur=0.34, gain=0.38)
sub(8.52, f0=64, f1=38, gain=0.52)
tick(8.96, tone=1900, gain=0.17)                                      # ring on the subject

# ---- S5 promise + CTA 10.65 ----
whoosh(10.49, dur=0.40, gain=0.42)
sub(10.65, f0=72, f1=36, dur=0.85, gain=0.80)                         # mask opens
tick(10.82, tone=2150, gain=0.13)
tick(10.98, tone=2000, gain=0.13)
sub(12.66, f0=66, f1=40, dur=0.80, gain=0.72)                         # wordmark
tick(13.20, tone=2100, gain=0.14)
tick(13.48, tone=2600, gain=0.20)                                     # follow chip
swell(13.80, dur=1.00, gain=0.11)

# ---------------------------------------------------------------- master
peak = np.max(np.abs(mix))
if peak > 0:
    mix *= min(1.0, 0.89 / peak)
t_ = int(0.3 * SR)
mix[-t_:] *= np.linspace(1, 0, t_)
st = np.stack([mix, mix], axis=1)
pcm = (st * 32767).astype(np.int16)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'audio', 'mix.wav')
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(f"wrote mix.wav  {DUR}s  peak={np.max(np.abs(mix)):.3f}")
