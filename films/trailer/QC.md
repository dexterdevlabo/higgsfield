# Quality Control — The Art of Kite Flying (capability trailer)

Signed off against `references/quality-control.md`. Measured values are from the delivered file,
not estimates. `out/trailer_1080p.mp4`, 1920×1080, 30 fps, 300 frames, 10.000 s, 6.5 MB.

## Visual identity
- [x] Palette consistent with ART_DIRECTION.md; no colour sampled from assets into graphics.
- [x] No palette arc declared, and none drifts.
- [x] Typography limited to the declared system (Inter Display 700 / Inter 600 / Inter 400 / JetBrains Mono 700).
- [x] One easing set throughout: entrance `power4.out`, exit `power3.in`, camera `power1.inOut`.
- [x] Transitions limited to the declared set: three hard cuts and one shape-mask reveal. No dissolves.
- [x] 80 px margins and the persistent corner slug hold across all four shots.
- [x] Grain (5.5% overlay) and vignette applied once, globally, not per asset.

## Image quality
- [x] Crops deliberate; the Harunobu is framed right so the kite stays in shot, the Perkins mount is cropped off.
- [x] Cutout edges checked at 200%: flood-fill at fuzz 11% keeps the robes intact (fuzz 14% ate them, fuzz 8% left the sky).
- [x] Print sheet edge clipped (`clip-path: inset(18px 0 0 0)`) after it showed as a seam in an earlier render.
- [x] Parallax is depth-correct: the distant kite travels 26 px, the willow 54 px, the near figure group 96 px.
- [x] No upscaling: every asset is downscaled from the institutional original.
- [x] No reference-only material used; nothing traced or filtered from a copyrighted source.

## Editing
- [x] Every shot carries information: 1766 artefact → 1910 photograph → four-archive spread → title.
- [x] Pacing varied: 2.7 s / 2.7 s / 2.95 s / 2.55 s, with staggered internal beats.
- [x] No decorative transitions; hard cuts carry three of the four joins.
- [x] Annotations and type lead their beat; the title is revealed *by* the mask rather than fading in after it.
- [x] No cut lands on motion; no black frames (verified, see below).

## Factual accuracy
- [x] No map appears, so no projection or border-vintage claim is made.
- [x] On-screen dates reproduce the source institution's own dating, including "ca. 1830–33" from the LoC record "[between 1830 and 1833]".
- [x] No image is captioned as a place, person or event beyond its catalogue record.
- [x] No colourisation, recreation or generated imagery, so no recreation labelling is required.
- [x] "Five centuries" is supported by the collection's own range (1430–1929); the film's own items span 1766–1917.

## Legal & attribution
- [x] All six assets classified (all class A) with the source's verbatim rights statement in ASSETS.md.
- [x] Each item verified at its **source institution**, not at the aggregator that listed it.
- [x] Art Institute of Chicago items excluded — rights unverifiable (HTTP 403), recorded in ASSETS.md.
- [x] On-screen courtesy credits in S1, S2 and the end card; full credits in `out/CREDITS.md`, generated from ASSETS.md.
- [x] Audio fully synthesised; fonts are SIL OFL 1.1.
- [x] No fabricated licence, creator, permission, attribution or URL.

## Technical (measured)
- [x] Resolution 1920×1080, 16:9. · [x] 30 fps constant, 300 frames, no duplicates at scene joins.
- [x] Duration exactly 10.000 s (an earlier build ran 8.97 s because the renderer takes its length from the GSAP timeline; a terminal hold fixed it).
- [x] Audio present and audible — **verified by measurement**, after lint caught that an `<audio>` without an `id` renders silent.
- [x] Integrated loudness **−17.7 LUFS**, LRA 4.1 LU, true peak **−1.8 dBTP**.
      Note: this is 1.7 LU under the −16 LUFS target in `sound-design.md`. The mix is transient-heavy
      (sub impacts), so pushing further hit the true-peak ceiling; −1.8 dBTP with clean peaks was
      preferred over hitting the number. Recorded rather than rounded off.
- [x] `blackdetect` clean at d=0.1, pic_th=0.97 (two earlier builds failed this and were fixed).
- [x] `ffmpeg -v error` decode: no output, no errors, no corrupt frames.
- [x] No missing media, placeholder text or debug overlays. HyperFrames lint: 0 errors.
- [x] Output verified playable end to end.

## Known limitations (not defects, but stated)
- No subtitles: the film has no speech. A sidecar would be empty.
- Four HyperFrames lint warnings remain (`nested_structure_needs_subcomposition`). They are Studio
  timeline-display advice, not render faults; splitting four shots into sub-composition files would
  add structure for no gain on a 10-second piece.
- No 9:16 cut was requested; the composition would need genuine recomposition, not a crop.
