# Quality Control

Complete before export. Copy this into the project as `QC.md` and record pass / fail / fixed
per line, with the shot numbers of any failure. A blank checkbox is a blocker.

## Visual identity
- [ ] Palette consistent with `ART_DIRECTION.md`; no stray colours sampled from assets.
- [ ] Any palette arc follows the declared shot numbers; no unexplained jumps between cuts.
- [ ] Typography coherent: declared families, weights, sizes, tracking only.
- [ ] Animation language consistent: one easing set, one entrance distance, one stagger rate.
- [ ] Transitions limited to the declared 3–5; each one justified by a relationship.
- [ ] Composition professional: grid respected, margins consistent, nothing accidentally centred.
- [ ] Grain, black level and highlight character uniform across archival, modern and graphic shots.

## Image quality
- [ ] Every crop deliberate; nothing important cut off; lead space in the direction of motion.
- [ ] Masks clean at 200%: no halo, no stair-stepping, hair and foliage feathered.
- [ ] Cutouts integrated: contact shadows, matched black level, matched grain.
- [ ] Perspective consistent where elements are composited.
- [ ] No upscaling artefacts; nothing stretched off its native aspect.
- [ ] Reference-only material used only as reference; no traced or filtered derivatives shipped.

## Editing
- [ ] Every shot earns its place: name the information it delivers, or cut it.
- [ ] Pacing varied; no run of equal-length shots; a pause after each difficult idea.
- [ ] No unnecessary transitions; hard cuts where a hard cut is stronger.
- [ ] Graphics land 60–150ms before their words; figures land on stressed syllables.
- [ ] Final states held ≥400ms; no cuts on motion unless motion continues.
- [ ] Hook present in the first 8s (16:9) / 1.5s (9:16).
- [ ] Scene-to-scene connections deliberate; no orphaned shots.

## Factual accuracy
- [ ] Maps correct: projection stated, borders match the narrated year, place names period-correct.
- [ ] Dates, figures, units and definitions match `RESEARCH.md`.
- [ ] Every image correctly identified; nothing shown as a place or person it is not.
- [ ] Recreations, colourisations, composites and generated imagery labelled on screen.
- [ ] Contested scholarship presented as contested.

## Legal & attribution
- [ ] Every asset in `ASSETS.md` has a licence class; nothing `PENDING-REVIEW` is in the cut.
- [ ] Attribution requirements satisfied in the required place (on screen vs description).
- [ ] Share-alike and no-derivatives implications checked.
- [ ] Trademark, personality-rights and privacy concerns reviewed.
- [ ] Music and sfx licences logged.
- [ ] `out/CREDITS.md` generated from `ASSETS.md`; the two agree.
- [ ] No fabricated licence, creator, permission, attribution or URL anywhere.

## Technical
- [ ] Resolution and aspect ratio correct per deliverable.
- [ ] Frame rate constant; no duplicated or dropped frames at scene joins.
- [ ] Audio in sync start to finish (check at 0%, 50%, 100%).
- [ ] Loudness within target; true peak ≤ −1.5 dBTP; no clipping.
- [ ] Subtitles readable, correctly timed, inside safe areas; sidecar file loads.
- [ ] No missing media, no black frames, no placeholder text, no debug overlays.
- [ ] No render errors or corrupt frames.
- [ ] Output verified playable end to end.

## Verification commands

```bash
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,nb_frames,duration \
        -show_entries format=duration,bit_rate -of default=noprint_wrappers=1 out/film_1080p.mp4
ffmpeg -i out/film_1080p.mp4 -af ebur128=peak=true -f null -          # loudness + true peak
ffmpeg -i out/film_1080p.mp4 -vf "blackdetect=d=0.3:pic_th=0.98" -f null -   # black frames
ffmpeg -v error -i out/film_1080p.mp4 -f null - 2>&1 | head           # stream errors (expect silence)
for p in 05 25 50 75 95; do ffmpeg -v error -ss $((p*DUR/100)) -i out/film_1080p.mp4 \
  -frames:v 1 build/qc_$p.png; done                                   # spot-check frames
```

Inspect the spot-check frames. Then watch the whole film once, at full size, with sound, and
ask the three questions: did I learn something, did any frame confuse me, did anything look
accidental. If the answer to the last is yes, it is not finished.
