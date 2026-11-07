# Platform specs — Shorts, Reels, TikTok

One master serves all three: **1080×1920, 9:16, 30fps, H.264 + AAC**.

## Build to the intersection of the safe areas

Each platform overlays its own UI. Rather than three cuts, keep essential content inside the
region all three leave clear:

| Edge | Keep clear | Why |
|---|---|---|
| Top | **14%** (~270px) | status bar, platform header |
| Bottom | **26%** (~500px) | caption, handle, CTA, progress bar |
| Right | **12%** (~130px) | **TikTok's action rail** — Shorts and Reels don't have it |
| Left | 6% (~65px) | breathing margin |

Usable core: roughly **x 65–950, y 270–1420**. Put the focal element near **y ≈ 760**.

The right-hand reserve is the one people forget, because it only bites on TikTok.

**Verify before a launch.** Platform UI shifts; these are conservative figures, not a
specification. Render one frame with the guides on and check it against a real phone.

## Length

| Platform | Cap | Comfortable |
|---|---|---|
| YouTube Shorts | ~3 min | 25–60s |
| Instagram Reels | ~3 min | 20–60s |
| TikTok | ~10 min | 20–60s |

For children, shorter is better regardless of cap. One idea, told completely, is worth more
than three rushed.

## Audio

Master around **−18 LUFS, true peak ≤ −1.5 dBTP** — quieter than the −14 typical of adult
short-form, because children often use headphones and because all three platforms normalise
loudness on playback anyway. There is no advantage to a hot master and a real cost to it.

## Captions

Burn them in. Platform auto-captions are unreliable and styled outside your control.
Keep them inside the safe core, two lines maximum, and respect the age band's dwell minimum.

Also ship a sidecar `.srt` — it costs nothing and some uploaders use it.

## Delivery

```bash
ffmpeg -i master.mp4 -c:v libx264 -crf 18 -preset slow -r 30 -s 1080x1920 \
  -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart out/short.mp4
```

One file, uploaded three times. Per-platform re-encoding is unnecessary and only adds a
generation of loss.
