---
name: kids-shorts
description: Produce short educational videos for children for YouTube Shorts, Instagram Reels and TikTok — 9:16, from a supplied script and direction. Generates stills and voiceover through Higgsfield, then animates and edits them locally with HyperFrames and ffmpeg. Use when asked for a kids' short, an explainer for children, a Shorts/Reels/TikTok educational clip, or a series of them. Enforces a credit budget, an age band, child-safety rules and factual accuracy.
---

# Kids Shorts

Short-form educational video for children. The user supplies the **script and direction**;
this skill turns that into a finished 9:16 film for all three platforms.

Built on `vox-documentary-editor` — its accuracy, sourcing and QC rules all still apply.
This skill adds three things that one doesn't have: a **credit budget**, an **age band**, and
**child-safety constraints**.

## The economic rule that shapes everything

**Generate stills. Animate them in code.**

Video generation is the expensive call; image generation is a fraction of it; code-drawn
graphics and synthesised sound cost nothing. A 40-second short needs roughly **8–12 images
and one voiceover** — nothing else should ever be paid for.

| Paid (Higgsfield) | Free (local, in-repo) |
|---|---|
| illustrated scenes and characters | all titles, captions, labels, numbers |
| the voiceover | diagrams, charts, arrows, maps |
| *(video gen only if a shot truly cannot be a moving still)* | transitions, masks, backgrounds |
| | Ken Burns, parallax, camera moves |
| | the entire sound design |

The kite film in `films/trailer` is the proof: still images cut into depth layers and
parallaxed read as motion. Apply the same technique to generated art.

**Never pay twice for the same thing.** No regenerating for a crop or a pan — crop in code.
No text inside generated images — models garble lettering and you pay for the retry; all text
is drawn locally.

Full tactics, including the batching rules and a worked budget: `references/credit-budget.md`.

## Hard gate before spending

1. Write the shot list with a **GENERATED / DRAWN** decision per beat.
2. Count the generated assets and produce a **cost quote**.
3. **Show the user the quote and wait for an explicit yes.** One approval covers one
   generation run, not the project.
4. Check `unlim.available` first — if a free allowance exists, use it and spend nothing.

This holds even when the user has already said "make it". A quote is cheap; a wasted batch is not.

## Workflow

| # | Stage | Output |
|---|---|---|
| 1 | Intake — script, direction, **age band**, topic | `PROJECT.md` |
| 2 | Fact-check every claim in the script | `RESEARCH.md` |
| 3 | Beat breakdown, 1 beat ≈ 1 idea ≈ 1 image | `SHOTLIST.md` with GENERATED/DRAWN per beat |
| 4 | Budget + **spend gate** | quote shown, approval recorded |
| 5 | One batched image call; one voiceover call | `assets/generated/` |
| 6 | Assemble: Ken Burns, parallax, code-drawn graphics, captions | `src/index.html` |
| 7 | Sound design, synthesised | `src/audio.py` |
| 8 | QC — luma, loudness, safe areas, reading speed | `QC.md` |
| 9 | Export + per-platform notes | `out/` |

## Non-negotiables for children's content

- **It must be true.** Educational means a child will believe it. The parent skill's accuracy
  rules apply in full; no invented statistics, no "scientists say".
- **Declare an age band** (3–5, 6–9, 10–12) before writing a shot. It sets vocabulary, sentence
  length, dwell time, pacing and music.
- **No peril, no jump scares, no darkness as threat.** No sudden loud transients — children
  often listen on headphones.
- **No photorealistic children** in generated imagery, and no real child's likeness. Stylised
  or illustrated characters only.
- **No engagement bait.** No "wait for it", no manufactured cliffhanger, no countdown pressure.
- **Captions always**, burned in. Children watch muted, and on-screen text supports reading.
- **YouTube "Made for Kids" is a legal flag** (COPPA), not a category choice. Tell the user it
  disables comments and personalised ads before they upload.

Detail: `references/child-safety.md`.

## Format

One master serves all three platforms: **1080×1920, 9:16, 30fps**.

Build to the **intersection** of their safe areas — top 14%, bottom 26%, right 12% clear of
anything essential. The right margin is for TikTok's action rail, which the other two don't
have. Length caps and per-platform notes: `references/platform-specs.md`.

## Templates

`templates/` holds `PROJECT.md`, `SHOTLIST.md`, a `build.sh` that goes generate → assemble →
render → verify, and `composition.html` — a tested 9:16 skeleton with Ken Burns, a caption
track, safe-area guides and placeholder art, so a new short starts from something that
already renders.

## Inherited, do not relearn

From `vox-documentary-editor/references/`: the HyperFrames traps (timeline length, silent
audio without an `id`, `fromTo` from 0 being 0 at t=0), `qc_luma.py` instead of `blackdetect`,
and treatment-follows-source. Read `technical-production.md` before the first render.
