# Narration — measured state

**One line generated. 0.1 credits remain. The full script is not fundable at this rate.**

## What the platform API can and cannot do

`api.higgsfield.ai` (where the $7 sits) has **no text-to-speech**. Established by probing,
not by reading the docs: an endpoint that exists answers `400 'prompt' is a required
property`; one that does not answers `404 model_not_found`. Control `/z-image/turbo` → 400.

Probed and all 404: `/text-to-speech` `/tts` `/speech` `/audio` `/higgsfield-ai/tts`
`/higgsfield-ai/text-to-speech` `/elevenlabs/tts` `/minimax/speech` `/speech/v1`
`/audio/speech` `/voice/tts` `/higgsfield-ai/speech`. The probes cost nothing.

So narration has to come from the web app (the MCP), which bills a different balance.

## cozy_voice is unavailable on this plan

Every preset tried returns `Voice preset is not available for the selected model` —
Arthur, Grady, and the voice the user supplied. The ~2.6-credit full-script figure quoted
earlier is therefore unreachable; it fell through to `seed_audio` at about 6.7x the cost.

## The one line that exists

| | |
|---|---|
| Engine | `seed_audio` |
| Voice | preset `dc1c0a41-53cd-53af-aec5-ab637840505f` (user's choice) |
| Text | "In 1959, this was a trade. And then it was gone." (47 chars) |
| Cost | **0.4 credits** |
| Output | 6.90s, 24 kHz stereo PCM → mastered to 48 kHz, −16 LUFS, −2.0 dBFS peak |
| Files | `src/assets/vo/line01.wav` (raw), `line01_master.wav` (mastered) |

## Two problems this measurement exposes

**1. Cost.** 2,597 chars at this rate is **~22 credits**. Balance is 0.1.
Caveat: extrapolated from a 47-char sample, so fixed overhead may be over-weighted and
the true figure could be lower. Do not treat 22 as exact.

**2. Pace — this one is measured, not extrapolated.** 6.90s for that sentence is roughly
**70 wpm**. The script is written for 135 wpm over 240s. At this engine's delivery the
464-word script runs about **7 minutes**, not 4.

So even fully funded, the narration does not fit the cut. Either the cut is re-timed to a
slower read, or the script comes down to roughly 300 words. That is an editorial decision,
not a technical one, and it is the user's to make.

## Routes

1. **User records it.** Free, and fixes the pacing problem outright.
2. **Fund the web app** (~22 credits) and then re-time the cut or cut the script.
3. **Render silent with captions.** Free, and shows the whole film moving.
