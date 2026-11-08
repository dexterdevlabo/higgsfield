# Credit budget

The user's explicit constraint is to **minimise Higgsfield spend**. This is the discipline.

## Where the money goes

Roughly, per unit of output: **video generation ≫ image generation ≫ text-to-speech ≫ zero**.
So the whole strategy is to move work down that ladder.

Check actual prices at quote time with `models_explore action:"get"` and the preparation step
of whichever tool you use — never assert a price from memory.

## The ladder, in order of preference

1. **Code-drawn, zero cost.** Titles, captions, numbers, counters, labels, arrows, diagrams,
   charts, maps, shapes, backgrounds, transitions, masks, grain, vignette — all of it.
   Also the entire sound design, synthesised with numpy (see any `films/*/src/audio.py`).
2. **One generated still, animated.** A Ken Burns push, a parallax split or a mask reveal
   turns one image into a living shot. This is the default for any illustrated scene.
3. **One still reused across beats.** A character established in beat 2 can reappear in beat
   7 at a different crop and scale. Crop in code; never pay again.
4. **Generated video.** Only when a shot genuinely cannot be a moving still — fluid motion,
   a physical process, a character performing an action. Expect to justify it in `PROJECT.md`.

## Hard rules

- **Batch.** Use `generate_image_batch` for every image in the film in a single call, not one
  call per beat. Same for audio where the tool supports it.
- **One voiceover call for the whole script.** Not one per line. Cut it to beats locally with
  ffmpeg using word timings, exactly as `films/shortwhy` does for its VO slot.
- **No text inside generated images.** Models garble lettering, you pay for the retry, and
  the result can't be edited or translated. Every word on screen is drawn locally.
- **No regeneration for framing.** Wrong crop, wrong pan, wrong size — all fixable in code.
- **Fix the seed** and keep the style reference, so a later addition to a series matches
  without a round of re-rolls.
- **Draft first where a model offers it.** Seedance exposes a 480p draft that finalises at
  1080p within seven days; generate drafts, pick, finalise only the keeper.
- **Check `unlim` before every run.** `models_explore` returns an `unlim` block;
  `supports_unlim` marks eligible models. If an allowance exists, use it with
  `use_free_gens=true` and `max_credits=0`. Never silently fall back to paid.
- **Cap it.** Pass `max_credits` at or below the quote on every call, so a mispriced run
  fails instead of overspending.

## Worked budget — a 40s short, age 6–9

| Beat | Content | Decision |
|---|---|---|
| 1 | Hook question, big type over a colour field | **DRAWN** |
| 2 | The subject introduced — illustrated scene | **GENERATED** |
| 3 | A labelled diagram of how it works | **DRAWN** |
| 4 | Scene: the thing happening | **GENERATED** |
| 5 | A counting number, 0 → the figure | **DRAWN** |
| 6 | Close detail — reuse beat 4's image, cropped in | **free** |
| 7 | Comparison, two illustrated panels | **GENERATED** ×2 |
| 8 | Recap, three code-drawn icons | **DRAWN** |
| 9 | Sign-off card | **DRAWN** |

**Spend: 4 images + 1 voiceover.** Nine beats, two paid calls. Everything else is local.

A naive version of the same film — one generated video per beat — would cost on the order of
a hundred times more and look worse, because generated video cannot hold a legible diagram
or a correct number.

## The quote

Before any paid call, show the user a table like this and wait:

```
Images   4  (one batched call, <model>, <resolution>)   ~<n> credits
Voice    1  (<engine>, <m> words, ~<s>s)                ~<n> credits
Video    0
                                              total    ~<n> credits
Free allowance available: <yes/no>
```

Then stop. Approval is per run, not per project.
