# Higgsfield cost — THE WORK (4:00)

All figures **measured** with `get_cost: true`, which submits nothing and spends nothing.
Checked 8 Nov 2026. Balance at time of checking: **0.5 credits, free plan.**

## Base plate (one static image, on screen all 240s)

| Model | Credits |
|---|---|
| `nano_banana` | **1** |
| `nano_banana_pro` @ 2k | **2** |

## Voiceover — 464 words / 2,597 chars

Hard cap of **2,048 chars per call**, so the script needs 2 calls minimum.
Priced on a 1,314-char half, doubled:

| Engine | half | full script |
|---|---|---|
| `text2speech_v2` · cozy_voice | 1.3 | **≈ 2.6** |
| `text2speech_v2` · minimax | 3.9 | **≈ 7.8** |
| `text2speech_v2` · elevenlabs | 3.9 | **≈ 7.8** |
| `seed_audio` (the default) | 8.7 | **≈ 17.4** |

Cost scales with character count, not per call — a 26-char line priced at 0.2.

## Music

| | Credits |
|---|---|
| `elevenlabs_music_v2_5` · 240s instrumental | **34.88** |
| `elevenlabs_music_v2_5` · 60s instrumental | 8.72 |

Music is the single most expensive item — more than everything else combined.

## Sound effects

`mirelo_text_to_audio` is flagged **game-pipeline only** and must not be used standalone.
No other SFX model in the catalogue. SFX will be synthesised locally (free), as in
`films/trailer/src/audio.py`.

## Totals

| Build | Credits |
|---|---|
| Minimum viable — nano_banana + cozy_voice, free music | **3.6** |
| **Recommended** — nano_banana_pro 2k + elevenlabs VO, free music | **9.8** |
| All-Higgsfield incl. 240s score | **44.7** |

## The actual blocker is the purchase floor, not the cost

`show_plans_and_credits` returns **no credit top-up packs** for this workspace —
`topups: []` and `credit_purchase_links: []`. Only plan upgrades are offered, and
auto-refill reports `is_eligible: false`. The MCP trial is `expired`.

So the cheapest route to any of this is **PLUS monthly, $49 for 1,000 credits**.
At the recommended build the film costs **9.8 of those 1,000 credits — about $0.49.**
The film is cheap; the minimum purchase is not.
