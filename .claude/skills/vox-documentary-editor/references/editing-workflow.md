# Editing Workflow

Eleven stages with explicit gates. Work in order. Do not start stage *n+1* while stage *n*'s
output is missing.

## Stage 1 — Research & factual verification
Establish the facts before the story. Collect claims into `RESEARCH.md`, each with a source
and a confidence note. Primary sources outrank summaries. Resolve contradictions explicitly;
where scholarship genuinely disagrees, the narration must say so. Record every number with
its unit, year, issuing body and definition — most statistical errors in explainers are
definition errors, not arithmetic errors.
**Gate:** no claim enters the script without a source line in `RESEARCH.md`.

## Stage 2 — Script analysis & narrative breakdown
Write or ingest the narration into `SCRIPT.md`. Then break it into beats: for each sentence
or clause, record the information it delivers and the question "what must the viewer see?"
Produce the beat table — beat ID, VO text, duration estimate (≈165 words/minute for
documentary delivery), information type (place / quantity / process / person / comparison /
cause / consequence), and the visual mode that best serves it (photographic, illustrated,
animated, typographic, cartographic, cinematic).
**Gate:** every beat has a visual mode assigned. Beats with no answer get rewritten or cut.

## Stage 3 — Visual research & asset collection
Per `visual-research.md`. Download to `assets/raw/`, log in `ASSETS.md` with licence class.
**Gate:** every beat has either an approved asset or an explicit "original graphic" decision.

## Stage 4 — Art direction
Per `visual-art-direction.md` and `color-theory.md`. Produce `ART_DIRECTION.md` with all
fourteen declarations and real values. Render a one-frame style plate showing the palette,
type system, an annotated map fragment and a graded photograph together.
**Checkpoint:** show the style plate to the user and wait for confirmation.

## Stage 5 — Storyboard & shot list
`STORYBOARD.md`, one row per shot:
`shot · in/out timecode · VO text · visual description · layers · motion spec · transition out · assets · on-screen text · sfx · notes`.
Resolve the whole film on paper here. Problems are free to fix at this stage and expensive later.
**Gate:** shot timecodes sum to the VO duration ±2%.

## Stage 6 — Asset preparation
Per `image-manipulation.md`. Crop, mask, cut out, grade, extend, build layer stacks into
`assets/prepared/`. Originals in `assets/raw/` stay untouched. Name files by shot:
`s014_bg.png`, `s014_ship_cut.png`.
**Gate:** every prepared asset inspected at 200% for edge and grade quality.

## Stage 7 — Original graphics & animation
Build maps, charts, timelines, titles, annotations and layer animation per
`animation-principles.md` and `technical-production.md`. Render per-scene intermediates to
`build/scenes/` as lossless or near-lossless (ProRes/FFV1/CRF 12), never as final-codec files.
**Checkpoint:** render 2–3 hero scenes, show them, confirm the direction before building the rest.

## Stage 8 — Edit & voiceover synchronisation
Assemble against the narration. Align graphic entrances 60–150ms ahead of their words, land
figures on stressed syllables, hold ends, cut on breaths. Use Whisper (or equivalent) to get
word-level timestamps from the VO and drive the timeline from them rather than eyeballing.
**Gate:** full rough cut plays start to finish with no missing media and no drift.

## Stage 9 — Sound design & colour grade
Per `sound-design.md`. Then the unifying grade pass: one black level, one grain, one highlight
character, applied at the sequence level so nothing looks cleaner than anything else.
**Gate:** measured loudness within target; grade applied once globally, not per clip.

## Stage 10 — Quality control
Per `quality-control.md`. Complete `QC.md` and fix every failure before export.
**Gate:** `QC.md` fully signed off.

## Stage 11 — Export & verification
Render deliverables to `out/`. Then verify: `ffprobe` the resolution, frame rate, duration,
codec and audio streams; spot-check frames at 10% intervals; play the file; confirm subtitles
load; confirm the 9:16 cut independently. Generate `out/CREDITS.md` from `ASSETS.md`.
**Gate:** verified playable output, both formats if both were requested.

## Decisions log

Append every creative decision and its reason to `PROJECT.md`. When the user changes direction
later, the log is what prevents re-litigating settled choices and prevents silent drift from
the art direction.

## Revision handling

Changes after stage 7 re-enter at the earliest affected stage, not at the top. A palette change
is a stage-4 change and invalidates every render. A VO re-record is a stage-8 change. Say which,
and say what has to be re-rendered, before starting.
