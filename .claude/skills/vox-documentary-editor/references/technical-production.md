# Technical Production

## Inspect first

Never assume a tool exists. Run this before planning any shot:

```bash
for t in ffmpeg ffprobe convert magick python3 node npx blender manim rembg sox qgis gs inkscape; do
  printf '%-10s ' "$t"; command -v "$t" || echo MISSING; done
python3 -c "
import importlib
for m in ['PIL','numpy','cv2','moviepy','rembg','scipy','matplotlib','cairosvg','shapely','geopandas','skimage']:
    try: importlib.import_module(m); print(f'{m:12} ok')
    except Exception: print(f'{m:12} MISSING')"
```

Record the result in `PROJECT.md`. Install only what a planned shot requires; prefer FOSS;
prefer a technique the baseline already covers.

**Typical baseline:** ffmpeg/ffprobe, ImageMagick (`convert`), Python 3 + PIL + numpy, Node + npx.
Everything below has a baseline-only path.

**SVG caveat:** ImageMagick only rasterises SVG through a delegate (`rsvg-convert` or
Inkscape). On a minimal image that delegate is absent and `convert in.svg out.png` fails with
*delegate failed `rsvg-convert`*. Test it once before planning an SVG-based pipeline:
`convert -size 10x10 xc:none t.svg && convert t.svg t.png`. If it fails, either install
`cairosvg` (pure-Python, light) or draw with PIL and skip SVG entirely.

## Capability map

| Need | First choice | Baseline fallback |
|---|---|---|
| Timeline, composite, render | **HyperFrames** (see below) | ffmpeg filter graphs |
| Still editing, masks, grading | ImageMagick | PIL |
| Procedural graphics, charts, maps | SVG generated from Python → rasterise | PIL drawing |
| SVG rasterisation | `cairosvg`, `inkscape`, `rsvg-convert` | draw directly with PIL — do **not** assume ImageMagick can do it (see note) |
| Complex synced typographic timelines | HyperFrames, else Remotion or Motion Canvas | per-frame PNG sequence from Python |
| Math/science animation | Manim | SVG keyframes from Python |
| Background removal | `rembg`, SAM | ImageMagick fuzz/flood + hand SVG mask |
| 3D, camera projection | Blender (`--background` + script) | fake depth via parallax layers |
| Cartography | QGIS, GeoPandas | GeoJSON → SVG projection in pure Python |
| VO word timestamps | `faster-whisper` / `whisper` | manual beat marking against waveform |
| Audio measurement/mixing | ffmpeg `ebur128`, `loudnorm` | — |

## HyperFrames — preferred renderer

`heygen-com/hyperframes` renders an HTML document to MP4: it seeks a paused GSAP timeline frame
by frame in headless Chrome and encodes with FFmpeg, so the same input gives the same output.
Prefer it whenever a shot needs real typography, masks, shadows, filters or many synchronised
layers — which is most documentary motion graphics. It needs Node 22+ and FFmpeg.

```bash
npm install --ignore-scripts hyperframes     # or: npx hyperframes init <project>
./node_modules/.bin/hyperframes lint    <proj>   # catches silent failures BEFORE rendering
./node_modules/.bin/hyperframes render  <proj> -o out/film.mp4 --fps 30 --quality delivery
```

Composition shape (one HTML file):

```html
<div id="root" data-composition-id="root" data-width="1920" data-height="1080" data-fps="30">
  <div class="clip" id="s1" data-start="0" data-duration="2.7">…</div>
  <audio id="mix" data-start="0" data-duration="10" src="assets/mix.wav"></audio>
  <script src="…/gsap.min.js"></script>
  <script>
    const tl = gsap.timeline({paused:true});
    tl.fromTo("#s1k1",{opacity:0,y:26},{opacity:1,y:0,duration:.44,ease:"power4.out"},0.22);
    window.__timelines = {root: tl};
  </script>
</div>
```

Hard-won rules, each of which cost a render:

- **The film's length is the GSAP timeline's length**, not the last clip's `data-start+duration`.
  A timeline whose last tween ends at 8.96s produces an 8.96s film however long the clips are.
  End with a terminal hold tween at the intended duration.
- **An `<audio>` or media element without an `id` renders SILENT.** The file still gets an AAC
  stream, so this passes a casual check — `lint` catches it, and measuring loudness proves it.
- **Run `lint` before every render.** It also catches fonts used without `@font-face`, which
  otherwise silently fall back to a generic face and quietly wreck the typography.
- **Vendor fonts into the project** with `@font-face` and a relative `url()`. Do not rely on
  system fonts; a render elsewhere will not have them.
- Scene-level opacity fades are usually unnecessary — give scenes `z-index` and hard-cut. Fades
  that end after the next scene starts leave black frames.
- A mask reveal must open *over* the outgoing shot, and the incoming content must already be
  opaque inside the mask. Fading content in after the mask has covered the frame yields a
  black hole; `blackdetect` will find it.
- Easing: GSAP `power4.out` ≈ the entrance curve, `power3.in` ≈ exit, `power1.inOut` ≈ camera.
- Useful companions: `timeline` (prints the renderer's own model of your clips, which is how you
  find elements it thinks are never visible), `snapshot`, `validate`, `inspect`, `measure`,
  `grade-compare`, `audio`, `beats`.
- It is telemetric by default. `hyperframes telemetry disable` before working on anything the
  user would not want reported.

## Rendering model

Work in a **frame-sequence-and-intermediate** pipeline, which is reproducible and debuggable:

1. Generate each scene's graphics as PNG sequences (`build/scenes/s014/%05d.png`) or as a
   single plate plus an ffmpeg motion expression.
2. Render each scene to a lossless/near-lossless intermediate.
3. Concatenate intermediates, add audio, apply the global grade and grain, then encode deliverables.

Never encode to the delivery codec more than once.

```bash
# PNG sequence -> intermediate (FFV1 lossless; or prores_ks if available)
ffmpeg -framerate 24 -i build/scenes/s014/%05d.png -c:v ffv1 -level 3 -pix_fmt yuv420p \
  build/scenes/s014.mkv

# Ken Burns / camera push on a still, with proper easing (scale up front, crop a moving window)
# 4% push over 6s at 24fps on a 2560x1440 plate, eased with a smoothstep expression
ffmpeg -loop 1 -i plate.png -t 6 -filter_complex \
 "scale=3072:1728,zoompan=z='1+0.04*(3*pow(on/143,2)-2*pow(on/143,3))':\
  x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=2560x1440:fps=24" \
 -c:v ffv1 build/scenes/s009.mkv

# Parallax: background and foreground moving at different rates
ffmpeg -loop 1 -i bg.png -loop 1 -i fg_cut.png -t 5 -filter_complex \
 "[0:v]scale=2688:1512,crop=2560:1440:'60*t':0[b];\
  [1:v]scale=2688:1512[f];[b][f]overlay=x='-120+40*t':y=0:format=auto,fps=24" \
 -c:v ffv1 build/scenes/s014.mkv

# Mask-reveal transition between two scenes (circle expanding), via a generated mask sequence
ffmpeg -i a.mkv -i b.mkv -i mask/%05d.png -filter_complex \
 "[1:v][2:v]alphamerge[bm];[0:v][bm]overlay=format=auto" -c:v ffv1 t07.mkv

# Hard-cut assembly
printf "file 's009.mkv'\nfile 's014.mkv'\n" > build/list.txt
ffmpeg -f concat -safe 0 -i build/list.txt -c copy build/picture.mkv

# Global grade + uniform grain + vignette, applied once at the end
ffmpeg -i build/picture.mkv -i assets/audio/mix_norm.wav -filter_complex \
 "[0:v]eq=contrast=1.06:saturation=0.95:gamma=1.02,\
  noise=alls=6:allf=t+u,vignette=PI/5" \
 -map '[v]' -map 1:a -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p \
 -c:a aac -b:a 320k -movflags +faststart out/film_master.mp4
```

### Easing in ffmpeg

ffmpeg has no bezier primitive. Use these expressions with normalised time `p = on/(N-1)`:

- smoothstep (ease-in-out): `3*pow(p,2)-2*pow(p,3)`
- ease-out cubic: `1-pow(1-p,3)`
- ease-in cubic: `pow(p,3)`
- ease-out quint (close to the standard entrance curve): `1-pow(1-p,5)`

For exact bezier curves, precompute positions per frame in Python and generate the sequence
there. This is the preferred route for anything the art direction specifies as a bezier.

## Reusable component library

Build these once per project into `build/graphics/`, driven by `ART_DIRECTION.md` values
loaded from a single `art.json` so no colour or size is ever hard-coded twice:

animated map (projection, borders, routes, region fills, labels) · act title · lower third ·
label chip · annotation set (circle, arrow, bracket, underline) · photo cutout with contact
shadow · parallax stack · timeline · bar / line / area chart · counting figure · comparison
split · transition masks · sfx manifest · end credits roll.

Each component is a Python function or Remotion component taking `(art, props, frame)` and
returning a frame or SVG. Modular, parameterised, maintainable — no copy-pasted scene scripts.

```python
# build/graphics/lib.py — sketch
import json, pathlib
ART = json.loads(pathlib.Path('art.json').read_text())

def ease(p, kind='entrance'):
    if kind == 'entrance': return 1 - (1 - p) ** 5
    if kind == 'exit':     return p ** 3
    return 3 * p ** 2 - 2 * p ** 3

def label_chip(text, xy, frame, start, dur=10):
    p = min(max((frame - start) / dur, 0), 1)
    return {'text': text, 'x': xy[0], 'y': xy[1] + 24 * (1 - ease(p)),
            'opacity': ease(p), 'fill': ART['palette']['text'],
            'bg': ART['palette']['bg-raised'], 'font': ART['type']['label']}
```

## Remotion, when justified

Use it when a scene has many typographic layers that must stay synchronised, or when the user
will want to iterate on timing. Otherwise ffmpeg plus generated frames is lighter and faster.

```bash
npx create-video@latest --template blank docgfx   # then render:
npx remotion render src/index.ts Scene14 build/scenes/s014.mov --codec prores
```

Keep the art direction in the same `art.json` the Python components read.

## Delivery encodes

```bash
# YouTube 16:9 master
ffmpeg -i out/film_master.mp4 -c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p \
  -c:a aac -b:a 384k -movflags +faststart out/film_1080p.mp4
# Short-form 9:16 (recomposed sequence, NOT a crop — see formats-and-reframing.md)
ffmpeg -i build/picture_vertical.mkv -i assets/audio/mix_short.wav \
  -c:v libx264 -crf 17 -preset slow -r 30 -s 1080x1920 -pix_fmt yuv420p \
  -c:a aac -b:a 256k -movflags +faststart out/film_shorts.mp4
```

## Discipline

Deterministic builds: a `Makefile` or `build.sh` that regenerates everything from sources, so
a palette change is one edit plus one rebuild. Never hand-edit an intermediate. Keep
`assets/raw/` immutable. Clean `build/` aggressively — frame sequences fill a disk fast; if
writes start failing, delete intermediates you can regenerate rather than declaring defeat.
