# Image prompts — ready to run

**Three images, one batched call.** Do not run until the budget in `PROJECT.md` is approved.

## Shared style (prepend to each)

> Warm picture-book illustration for a children's science video. Soft gouache texture,
> rounded shapes, friendly and calm. Honey-gold, amber and cream palette with deep warm
> brown shadows. Gentle directional light. No text, no letters, no numbers, no watermark.
> No people. Vertical composition, 9:16, subject centred with clear space in the upper third.

Style notes exist for a reason:
- **"No text"** — models garble lettering and you pay for the retry. Every word on screen is
  drawn locally.
- **"No people"** — the child-safety reference rules out photorealistic children; the
  simplest guarantee is no human figures at all. Bees only.
- **"Clear space in the upper third"** — captions and titles live there; art that fills the
  frame forces a crop or a scrim.

## GEN-1 — the dark hive  *(used beat 2; re-cropped for beat 9)*

> …shared style… Inside a beehive at night. Rows of golden hexagonal honeycomb filling the
> frame, several honeybees resting on the comb, very dim warm light, deep shadow, intimate
> and quiet. The comb runs vertically. Mysterious but safe, not frightening.

Aspect 9:16. This one carries two beats, so favour the best of the batch.

## GEN-2 — the meadow  *(beat 1)*

> …shared style… A sunlit summer meadow seen from just above the flowers, masses of simple
> round wildflowers in yellow, white and soft pink, one honeybee in flight near the centre,
> bright midday light, soft depth of field behind. Open sky in the upper third.

Aspect 9:16.

## GEN-3 — the dancer  *(beat 5, the hero)*

> …shared style… A single honeybee on golden honeycomb, seen from directly above, close and
> clear, her body angled diagonally across the frame. Warm dim hive light. Simple uncluttered
> background so a diagram can be drawn over her.

Aspect 9:16. **The diagram overlays this shot**, so composition matters more than detail —
reject any result that is busy behind the bee.

## Call shape

One `generate_image_batch` call, three prompts, 9:16, fixed seed recorded below so a later
re-run matches. Pass `max_credits` at the approved quote.

- seed: _(record the seed actually used here after the run)_
- model: _(record)_
- cost: _(record)_

## Voiceover — one call

Text: the eleven lines in `SCRIPT.md`, concatenated with the pauses as written.
Engine: `text2speech_v2`, or `elevenlabs_v4_turbo` for a single steady voice.
Voice: pick a warm, unhurried preset — **audition `preview_url` first**; the voice list
carries no language or age metadata, so the only way to choose is to listen.
Save to `assets/vo.wav`. `build.sh` ducks the bed under it automatically.

**Do not** generate per line. One call, cut locally.
