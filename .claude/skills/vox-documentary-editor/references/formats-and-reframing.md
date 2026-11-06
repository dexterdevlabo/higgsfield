# Formats & Reframing

## Targets

**YouTube (16:9)** — master at 2560×1440 (deliver 1920×1080 minimum), 24fps for cinematic
pacing or 30fps for graphics-heavy work. Documentary pacing, full explanation, complete mix.
Hook in the first 8 seconds. Title-safe inset 120px at 1080p.

**Short-form (9:16)** — 1080×1920, 30fps, for YouTube Shorts, Instagram Reels, TikTok.
Hook in the first 1.5 seconds. Typical length 25–60s. Mastered to −14 LUFS.

Also supported when asked: 1:1 (1080×1080) and 4:5 (1080×1350) for feed placements — same
recomposition discipline.

## Short-form is recomposed, not cropped

Centre-cropping a 16:9 documentary destroys it: maps lose their geography, charts lose their
axes, type leaves frame, and cutouts end up headless. A vertical cut is a separate edit built
from the same assets.

Recompose each element:

- **Subjects** — reframe the crop around the subject's actual position per shot, not the frame centre.
- **Text** — re-typeset at vertical sizes and line lengths (≤26 characters per line), repositioned into the vertical safe band.
- **Maps** — re-project and re-zoom for a tall frame; a tall map shows latitude range, so choose the north–south extent deliberately; move labels inside.
- **Graphics and charts** — rebuild in vertical proportions. A wide bar chart becomes a horizontal-bar list; a wide timeline becomes a vertical timeline.
- **Animations** — re-key travel distances and directions for the new frame; vertical frames favour vertical motion.
- **Composition** — stack where 16:9 placed side by side. A two-up comparison becomes top/bottom.

### Vertical safe zones (1080×1920)

- Top 12% (≈230px): platform UI. No type.
- Bottom 22% (≈420px): captions, handles, CTA UI. No essential type or subjects.
- Usable core: y 230–1500. Put the single most important element at y ≈ 760.
- Keep a 60px side margin; type lives in the middle third of the height.

## Making the vertical cut

1. Select the beats that survive on their own. A short is one idea, not a compressed film.
2. Rewrite or re-cut the narration for the shorter form — do not speed-ramp the 16:9 VO.
3. Rebuild graphics from the component library at vertical dimensions (same `art.json`, so the
   identity is identical and only the layout differs).
4. Re-crop photographic plates from `assets/raw/` originals, not from the 16:9 prepared files,
   so you keep full resolution and can choose a new region.
5. Re-time: short-form tolerates faster cuts, but the dwell minimum for readable type still applies.
6. Burn in subtitles — most short-form is watched muted — inside the safe band, and still ship a sidecar.
7. Verify every frame: no clipped type, no decapitated subjects, no map without its context.

```bash
# Per-shot deliberate vertical reframe from the ORIGINAL, with a chosen region
convert assets/raw/a014.jpg -crop 1620x2880+980+140 +repage -resize 1080x1920 \
  assets/prepared/v_s014_bg.png
# Last resort only, when a shot is genuinely full-frame photographic with a centred subject:
# blurred-plate pillarbox (never for maps, charts or type)
ffmpeg -i shot.mkv -filter_complex \
 "[0:v]scale=1080:-2,crop=1080:1920:0:'(ih-1920)/2'[fg];\
  [0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=40[bg];\
  [bg][fg]overlay=(W-w)/2:(H-h)/2" -c:v ffv1 vertical.mkv
```

## What never gets a blurred pillarbox

Maps · charts · timelines · any frame containing type · any composition where the 16:9 width
carried the meaning. Those are rebuilt.
