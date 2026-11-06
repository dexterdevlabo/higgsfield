---
name: vox-documentary-editor
description: Research, art-direct, animate, composite, edit and render explainer documentaries — history, geography, science, psychology, culture, politics, architecture, economics, interesting facts — in the editorial-motion-graphics tradition (Vox, Johnny Harris, Wendover, PolyMatter, Nat Geo). Use when asked to make, edit, storyboard, art-direct, animate, score or render a documentary, explainer, video essay, animated map sequence, data-driven motion-graphics sequence, or a 16:9 / 9:16 short-form cut of one; also for visual research, asset licensing registers, image cutouts, parallax compositions, color-grading passes and quality control on such a video.
---

# Vox Documentary Editor

A complete documentary production system: research → art direction → storyboard → asset
preparation → original graphics → animation → edit → sound → grade → QC → render.

**This skill produces actual video files.** Scripts alone are never the deliverable unless
the user explicitly asks for a script only.

## Operating principles

1. **Visuals explain, they do not decorate.** Never "put images over voiceover." Every shot
   answers: what must the audience *understand* here, and what is the most interesting way to
   show it? If a shot only fills time, cut it or replace it with a graphic that carries meaning.
2. **Art direction before production.** No frame is rendered before `ART_DIRECTION.md` exists
   with real HEX values, named typefaces, a motion language and a transition language.
3. **Original identity.** Study the storytelling *principles* of the reference creators. Never
   reproduce anyone's proprietary graphics, logos, branding, lower-third designs or exact
   compositions. Each project gets its own coherent look.
4. **Prototype before you commit.** Render 2–3 hero scenes and get them confirmed before
   rendering the full timeline.
5. **Accuracy is non-negotiable.** Maps, dates, borders, attributions and identifications are
   verified. Recreations are never presented as archival originals.
6. **Nothing is overwritten blind.** Read any existing file before replacing it.

## Workflow

Eleven stages, run in order. Full detail in `references/editing-workflow.md`.

| # | Stage | Gate / output |
|---|---|---|
| 1 | Research & fact verification | `RESEARCH.md` with sourced claims |
| 2 | Script analysis & beat breakdown | `SCRIPT.md`, beat table with timecodes |
| 3 | Visual research & asset collection | `ASSETS.md` register (license per asset) |
| 4 | Art direction | `ART_DIRECTION.md` (palette, type, motion, transitions) |
| 5 | Storyboard & shot list | `STORYBOARD.md` (one row per shot) |
| 6 | Asset prep: crop, mask, cutout, grade | `assets/prepared/` |
| 7 | Original graphics & animation | `build/scenes/` |
| 8 | Edit & VO sync | rough cut rendered |
| 9 | Sound design & color grade | mixed, graded cut |
| 10 | Quality control | `QC.md` checklist signed off |
| 11 | Export & verification | `out/` + ffprobe-verified playback |

**Checkpoint discipline:** after stage 4 and after the stage-7 prototype, show the user what
you have and wait for confirmation before continuing. Do not render a 10-minute documentary
to discover the look is wrong.

## Project layout

Create one directory per documentary; never mix projects.

```
<project>/
  PROJECT.md          brief, format, duration, audience, status, decisions log
  RESEARCH.md         verified claims + sources
  SCRIPT.md           narration, beat table, timecodes
  ART_DIRECTION.md    palette HEX, typography, motion + transition language
  STORYBOARD.md       shot list: shot / VO / visual / motion / transition / asset / sfx
  ASSETS.md           asset register: source, creator, license, use, attribution
  QC.md               quality-control sign-off
  assets/
    raw/              downloaded originals, never edited in place
    prepared/         crops, cutouts, graded plates, layer stacks
    audio/            VO, music, sfx
  build/
    scenes/           per-scene renders (lossless intermediates)
    graphics/         generated SVG/PNG graphics, maps, charts
  out/                final deliverables (16x9, 9x16)
```

`PROJECT.md` is per-documentary and holds nothing reusable. Reusable craft knowledge belongs
in this skill's `references/`, not in a project file.

## Reference files — load on demand

Read only what the current stage needs. Do not preload everything.

| File | Load when |
|---|---|
| `references/visual-art-direction.md` | stage 4; any look/identity decision |
| `references/color-theory.md` | choosing or auditing a palette; grading intent |
| `references/animation-principles.md` | stages 7–8; specifying any movement |
| `references/transition-design.md` | designing shot-to-shot connections |
| `references/image-manipulation.md` | stage 6; cutouts, crops, compositing, parallax |
| `references/visual-research.md` | stage 3; sourcing imagery, maps, archives |
| `references/copyright-and-attribution.md` | any time an asset may be reused |
| `references/typography.md` | type system, titles, labels, kinetic text |
| `references/sound-design.md` | stage 9; sfx, music, rhythm, mix levels |
| `references/editing-workflow.md` | stage sequencing, gates, pacing, VO sync |
| `references/technical-production.md` | tooling, ffmpeg/Remotion recipes, render settings |
| `references/quality-control.md` | stage 10; pre-export audit |
| `references/formats-and-reframing.md` | 9:16 / short-form recomposition |

Starter files live in `templates/` — `PROJECT.md`, `STORYBOARD.md`, `ASSETS.md` and
`art.json`. Copy them into a new project directory at stage 1 rather than writing the
structure from memory. `art.json` is the single source of truth for palette, type and motion
values: every graphics component reads it, so nothing is hard-coded twice and a palette change
is one edit plus a rebuild.

## Toolchain

Inspect the environment before choosing tools — never assume. Run:

```bash
for t in ffmpeg ffprobe convert magick python3 node npx blender manim rembg sox; do printf '%s: ' "$t"; command -v "$t" || echo MISSING; done
```

Baseline that is nearly always present: **ffmpeg/ffprobe** (compositing, motion, render),
**ImageMagick** (stills, masks, grading), **Python + PIL/numpy** (procedural graphics, SVG,
layer math), **Node/npx**.

Preferred renderer when available: **HyperFrames** (`heygen-com/hyperframes`) — authors a shot as
HTML + GSAP and renders it through headless Chrome + FFmpeg, giving real typography, masks and
shadows with deterministic output. Always run its `lint` before rendering; it catches silent
failures (muted audio, missing `@font-face`) that a finished file hides. See
`references/technical-production.md` for the composition shape and its sharp edges.

Install only what a shot actually requires, prefer FOSS, and prefer a technique the baseline
can already do. `references/technical-production.md` has working fallbacks for every
capability — including background removal and easing without `rembg` or `opencv`.

## Format targets

- **YouTube** — 16:9, 1920×1080 min (prefer 2560×1440 masters), 24 or 30 fps, documentary pacing, full mix.
- **Short-form** — 9:16, 1080×1920, 30 fps, for Shorts / Reels / TikTok.

Short-form is **recomposed, never center-cropped**. See `references/formats-and-reframing.md`.

## Hard rules

- Never fabricate a license, a creator, a permission, an attribution or a source URL.
- Never recolor or alter archival evidence in a way that misrepresents it; label recreations.
- Never present a subject as identified unless the source identifies it.
- Never apply a transition because the timeline felt static. A clean cut beats a decorative wipe.
- Never leave an asset in `ASSETS.md` without a license classification.
- Never render final output before `QC.md` is complete.
