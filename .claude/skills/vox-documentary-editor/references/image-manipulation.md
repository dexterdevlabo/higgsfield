# Advanced Image Manipulation & Compositing

An image is not an indivisible rectangle. It is a composition containing subjects, objects,
backgrounds, textures and details, each of which can be used separately.

## Triage: what should this image become?

For each candidate, decide one or more of:

- used whole · cropped to a region · reframed to another aspect · background removed ·
  split into foreground/background layers · turned into a cutout · masked into a shape ·
  used as texture · enlarged to isolate one detail · parallaxed · combined with original
  graphics · used as reference for an original recreation (see `copyright-and-attribution.md`).

Write the decision into `ASSETS.md` under *intended use* — before any editing.

## Subject isolation

Worth isolating: people, buildings, monuments, vehicles, objects, geographic features,
documents, artifacts, machinery, animals.

Tool preference, in order of what the environment actually has:

1. `rembg` — fastest acceptable result on organic subjects, if installed.
2. SAM / Segment Anything — best for precise, prompted selection; heavy, install only if several shots need it.
3. OpenCV — GrabCut for hard-edged subjects, contour work for documents and maps.
4. ImageMagick — `-fuzz` flood fill for flat or sky backgrounds; `-morphology` for edge cleanup.
5. GIMP (scriptable via `script-fu`), Photoshop or Blender if present.
6. Manual mask drawn as a PNG (PIL `ImageDraw`, or an SVG path rasterised with `cairosvg`)
   and applied with ImageMagick or PIL — always available, and the right answer for a single
   hero cutout.

Never install the whole list. Detect, then pick.

```bash
# Flat/sky background removal, no extra deps
convert in.jpg -fuzz 12% -transparent '#8FB7D8' -morphology Close Disk:1 cut.png
# Alpha matte from a hand-authored mask (PNG; rasterise the SVG first — see the
# SVG caveat in technical-production.md, ImageMagick may have no SVG delegate)
convert in.jpg \( mask.png -alpha extract \) -compose CopyOpacity -composite cut.png
# Edge quality pass: 1px feather + slight contract so no halo survives
convert cut.png -channel A -morphology Erode Disk:1 -blur 0x0.8 +channel clean.png
```

Edge quality is the difference between a cutout and a mistake. Check at 200%: no halo of the
old background, no jagged stair-stepping, hair and foliage feathered not clipped, and the
cutout's black level matched to the plate it lands on.

## Layered compositions

A photograph becomes a scene. Worked example — a historical city street:

1. Isolate the foreground vehicle as its own layer.
2. Separate architectural elements where the perspective allows a clean split.
3. Keep the original background as the rearmost layer, patched where the cutouts left holes
   (content-aware fill, or extend with cloned texture).
4. Add atmospheric depth: 1–3% blur and 4–8% desaturation per layer going back.
5. Animate a slow camera push on the whole stack (≤4% over the shot).
6. Move the foreground layer faster than the background (parallax, see below).
7. Add a geographic annotation anchored to a real feature in frame.
8. Set the historical date in the project's supporting typeface.
9. Design the exit transition out of an element that is already in the frame.

Depth must not invent geometry that changes what the photograph documents. Parallax that makes
a flat crowd appear to be a deep crowd is fine; parallax that moves a building to a different
street is falsification.

### Parallax math

For layers at depths `d` (0 = far, 1 = near), if the camera moves `M` pixels, layer offset is
`M × (0.35 + 0.65d)`. Scale each layer by `1 + 0.06d` before moving so edges never reveal.
Keep total travel ≤6% of frame width; more than that exposes the flatness.

## Cropping

Crops are decisions, not fitting operations. Before cropping, determine: the main subject,
its position, the negative space you need, the contextual information you must not lose, the
direction of implied movement, where text will sit, the camera move you intend, and the target
aspect ratio.

Rules:
- Lead space goes in the direction of movement or gaze.
- Reserve the text zone at crop time; do not discover later that the headline covers a face.
- Crop with headroom for the camera move: a 4% push needs ≥8% spare on every side.
- If the subject sits near an edge, **extend** the composition (outpaint, mirror-extend a
  neutral region, or place the image on a palette plate) rather than cutting information off.
- Never crop out the part of an archival image that establishes what it is.

```bash
# Crop to a chosen region at 16:9 with push headroom, then resize to master
convert in.jpg -crop 2880x1620+420+180 +repage -resize 2560x1440 crop.png
# Extend rather than cut: place subject on a palette plate
convert in.png -background '#0E1116' -gravity center -extent 2560x1440 plate.png
```

## Image-to-image compositing

Combine photography with original maps, labels, shapes, arrows, lines, textures, charts,
timelines and illustrations. To look art-directed rather than assembled, match:

- **Perspective** — shared horizon and vanishing direction; annotations drawn in the plane they describe.
- **Lighting** — one light direction for the whole film; shadows consistent in angle, softness, opacity.
- **Scale** — composited elements sized by real-world logic, not by what fits.
- **Shadow contact** — every cutout gets a contact shadow, or the film is explicitly flat with none.
- **Grain and black level** — unified at render, so no element looks cleaner than the plate.
- **Color** — composited elements use palette colors, not colors sampled from the photo.

```bash
# Composite a cutout with a soft contact shadow
convert plate.png \
  \( cut.png -background black -shadow 28x18+0+18 \) -gravity center -composite \
  cut.png -gravity center -composite shot.png
```

## Prohibited

Stretching to fit · upscaling beyond 1.6× without a dedicated upscaler · leaving a white
rectangle around a cutout · auto-levels applied per-image so stills no longer match · altering
an archival image's content · presenting a composite as a single authentic photograph.
