#!/usr/bin/env python3
"""Sound bed for a kids short — synthesised, so it costs nothing.

Deliberately gentler than the adult films in films/*: no sub-bass impacts, softer
transients, a warm pad instead of a drone. Children often listen on headphones, and
references/child-safety.md rules out sudden loud hits.

Writes assets/mix_bed.wav; build.sh masters it (and ducks it under a voiceover if present).
"""
import numpy as np, wave, os

SR, DUR = 48000, 44.0          # match the composition's timeline length
N = int(SR * DUR)
mix = np.zeros(N)
rng = np.random.default_rng(11)
t = np.arange(N) / SR


def place(sig, at):
    i = int(at * SR); n = min(len(sig), N - i)
    if n > 0: mix[i:i + n] += sig[:n]


def env(n, attack, power=2.0):
    a = max(1, int(attack * SR)); e = np.ones(n)
    e[:a] = np.linspace(0, 1, a) ** 0.7
    e[a:] = np.linspace(1, 0, n - a) ** power
    return e


def chime(at, freq, dur=0.9, gain=0.16):
    """A soft mallet tone. Used instead of the ticks and sub impacts of the adult films."""
    n = int(dur * SR); tt = np.arange(n) / SR
    body = (np.sin(2*np.pi*freq*tt) + 0.5*np.sin(2*np.pi*freq*2*tt)
            + 0.25*np.sin(2*np.pi*freq*3.01*tt))
    place(body * env(n, 0.006, 3.2) * gain, at)


def swish(at, dur=0.34, gain=0.10):
    """A soft air movement for a scene change. No whip, no impact."""
    n = int(dur * SR)
    noise = rng.normal(0, 1, n)
    k = np.exp(-2*np.pi*900/SR); y = np.zeros(n); acc = 0.0
    for i in range(n):
        acc = (1-k)*noise[i] + k*acc; y[i] = acc
    place(y * env(n, dur*0.45, 1.6) * gain, at)


# --- warm pad: a major triad, breathing. Nothing below 110 Hz. ---
for f, g in ((220.0, 0.055), (277.2, 0.040), (329.6, 0.034)):
    vib = 1 + 0.0016 * np.sin(2*np.pi*0.18*t)
    mix += np.sin(2*np.pi*f*t*vib) * g * np.clip(np.sin(np.pi*t/DUR), 0, 1) ** 0.6

# --- one chime per beat boundary, a rising figure so the film feels like progress ---
for at, f in ((0.10, 523.3), (3.70, 587.3), (7.70, 659.3), (11.70, 698.5),
              (17.50, 784.0), (23.80, 880.0), (29.00, 932.3), (34.50, 1046.5)):
    chime(at, f)
for at in (3.55, 7.55, 11.55, 17.35, 23.65, 28.85, 34.35, 39.65):
    swish(at)
# the angle reveal and the closing line get a little more weight
chime(20.20, 1174.7, dur=1.2, gain=0.19)
chime(39.80, 1318.5, dur=1.6, gain=0.17)
chime(43.00, 1046.5, dur=1.8, gain=0.15)        # resolve, under the last line

peak = np.max(np.abs(mix))
if peak > 0: mix *= min(1.0, 0.72 / peak)        # headroom; build.sh does the mastering
fo = int(0.5 * SR); mix[-fo:] *= np.linspace(1, 0, fo)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'mix_bed.wav')
os.makedirs(os.path.dirname(out), exist_ok=True)
st = (np.stack([mix, mix], axis=1) * 32767).astype(np.int16)
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
print(f"wrote mix_bed.wav  {DUR}s  peak={np.max(np.abs(mix)):.3f}")
