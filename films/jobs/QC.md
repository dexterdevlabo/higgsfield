# QC — THE WORK (films/jobs)

Measured on the rendered master, not on the composition. Date 8 Nov 2026.

## Delivery

| | measured |
|---|---|
| File | `out/THE_WORK_1080p.mp4` · 228.5 MB |
| Duration | **240.000000 s** (target 4:00.000 — exact) |
| Video | h264 High, 1920×1080, **24/1 fps**, 5760 frames, 7985 kb/s |
| Audio | AAC LC, 48 kHz, stereo, 11251 frames |
| Render | 5760/5760 frames in 16m 56.1s, software GPU, beginframe capture |

Frame count reconciles exactly: 240.000 s × 24 fps = 5760.

## Audio — silent by design, and verified so

`volumedetect` over the whole track: **n_samples 23,040,000** (= 240 s × 48 000 × 2),
**mean −91.0 dB, max −91.0 dB**. Flat digital silence.

This is the intended state: `assets/mix.wav` is a 240 s silence placeholder because the
narration is being recorded elsewhere. The sample count is the thing to check — a stream
that is *absent* and a stream that is *silent but present* look the same in a player, and
the HyperFrames trap (a media element with no `id` renders silent while still emitting an
AAC stream) produces the second. Here the stream is complete and deliberately empty.

## Luma — 240 frames, 1 fps across the whole film

Per-frame mean luma and bright extreme; the gate is mean ≥ 6 **and** max ≥ 120.
`blackdetect` is the wrong instrument for this palette — it flagged 4.3 s of a correct end
card in `films/shortwhy`, which is why `qc_luma.py` exists.

| | |
|---|---|
| Frames checked | 240 |
| Mean luma overall | 44.2 (median 43.9) |
| Below the gate | 4 frames, **all explained** |

| t | mean/max | what it is |
|---|---|---|
| 0 | 12.0 / 56 | the 1 s fade-up from black that opens the film |
| 115 | 29.0 / 68 | mid-crossfade, strike part I → part II — card visible at partial opacity |
| 168 | 29.0 / 68 | mid-crossfade at the end of ch3 — card, slug and year all visible |
| 215 | 29.0 / 68 | **scripted empty frame** on "They were replaced by a file" |

Frames 115 and 168 were inspected directly rather than trusted to the number: both carry
footage on screen. A crossfade dipping below the bright-extreme threshold is normal, not a
hole in the cut.

Fully black by intent and excluded from the gate: t 104–105, 169–171 (the two scripted
black beats) and 234–240 (grade to black, then the credits card, which reads mean 4.2 /
max 172 — dark field, bright type, correct).

## Coverage

Every second of the cut was checked for footage on screen. Six gaps, all accounted for:

| from | to | |
|---|---|---|
| 14.60 | 20.00 | black, then the title card |
| 104.00 | 106.00 | scripted black beat |
| 168.50 | 172.00 | scripted black |
| 215.00 | 218.00 | scripted empty frame |
| 239.00 | 240.00 | end credits card |

Two earlier defects — 1.0 s of bare base at 90–91 and 1.8 s at 170.2–172 — were found by
this check and closed before the render.

## Lint

`hyperframes lint`: **0 errors, 3 warnings.** All three are
`duplicate_media_discovery_risk` from grid tiles that deliberately reuse one source at
several crops. An overlapping-tween warning on `#credits` was fixed before rendering.

## Not yet done

- **No narration.** 56 lines in `SCRIPT_FOR_VO.md` with picture timings; `out/THE_WORK_narration.srt` for import.
- **No music, no SFX.** The track is silence, not a mix.
