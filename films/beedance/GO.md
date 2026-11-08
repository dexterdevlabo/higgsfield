# GO — the sequence when you say start

Everything else is done. These are the only steps that spend anything.

## 0. Pre-flight (free)

```
models_explore action:"get" model_id:"<image model>"     # confirm price + params
list_voices                                              # audition preview_url, pick a warm voice
```

Check the `unlim` block. If a free allowance exists, use it: `use_free_gens=true`,
`max_credits=0`. Never fall back to paid silently.

## 1. Quote and approval

Fill the budget table in `PROJECT.md` with real numbers and **show it**. Wait for a yes.
One approval covers this run only.

## 2. Images — ONE batched call

Three prompts from `PROMPTS.md`, 9:16, one `generate_image_batch`, `max_credits` at the quote.
Record model, seed and cost into `ASSETS.md`.

Save as — names must match exactly, the composition already points at them:

```
assets/generated/gen1_hive.png
assets/generated/gen2_meadow.png
assets/generated/gen3_dancer.png
```

Download with `curl` from the returned URLs (both Higgsfield CDNs are reachable; verified).

## 3. Voiceover — ONE call

Full script text from `SCRIPT.md`, one call, chosen voice. Save to `assets/vo.wav`.
Do not generate per line.

## 4. Build — free

```bash
cd films/beedance && bash build.sh
```

It regenerates the bed, ducks it under the VO, copies assets, lints, renders at delivery
quality, then verifies: decode, per-frame luminance, loudness.

## 5. Check before publishing

- `out/short.mp4` — 44.000s, 1320 frames, 1080×1920
- luminance: PASS on all frames
- loudness: around **−18 LUFS**, true peak ≤ −1.5 dBTP (quieter than adult short-form, on purpose)
- render one frame with `data-guides="on"` and confirm nothing essential sits in the red bands
- watch it once at phone size with sound

## Current state without any generation

`out/short.mp4` already exists and plays, using drawn placeholders. It is 44.000s, passes
luminance on all 1320 frames and measures −18.1 LUFS. Swapping the three PNGs is the only
visual change step 2 makes.

## If you want to trim the spend further

- Drop GEN-3 and run beat 5's angle diagram over the honeycomb background instead: **2 images**.
- Drop GEN-2 and open on a drawn meadow: **1 image**.
- The film still works at one image, because the lesson is the diagram.
