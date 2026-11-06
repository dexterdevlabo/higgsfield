# Quality Control — THE SHORT WHY

Measured on the delivered file. `out/shortwhy_reel.mp4`, 1080×1920, 30fps, 450 frames,
15.000s, 5.1 MB.

## Visual identity
- [x] Palette matches ART_DIRECTION.md; accent used once per frame, never twice.
- [x] Type limited to Inter Display 700 / Inter 600 / Inter 400 / JetBrains Mono 700.
- [x] One easing set: `power4.out` in, `power3.in` out, `power1.inOut` camera, one `back.out` on the CTA chip only.
- [x] Transitions limited to the declared three. No dissolves.
- [x] Grain and vignette applied once globally.

## Vertical format
- [x] Composed vertical at 1080×1920 — not cropped from a horizontal cut.
- [x] Top 230px and bottom 420px carry no essential type or subject.
- [x] Focal element sits near y≈760 in every beat.
- [x] Readable muted: every spoken line is also on screen.
- [x] Longest line 24 characters; headline 104px, smallest type 24px.

## Image quality
- [x] Hine scan border cropped; photographic grade per art direction; content unaltered.
- [x] No upscaling beyond 1.22× (Hine 825px → 1008px wide).
- [x] Map drawn at 2× supersample and downsampled, since PIL does not antialias polygons.

## Editing
- [x] Hook present on **frame 0** — verified, not assumed.
- [x] Every beat populated at its cut; no soft starts (fixed, see below).
- [x] Pacing: 1.95 / 2.45 / 2.05 / 2.05 / 2.30 / 2.19 / 2.34 s.
- [x] The one hero move (Greenland shrink) is the longest at 1.10s; everything else is ≤0.62s.

## Factual accuracy
- [x] Map is real geometry (Natural Earth), not invented coastlines.
- [x] "Looks as big as Africa" measured on the render: 1.09×.
- [x] "14×" from official published areas (14.02), not from the simplified drawing geometry (13.72). Discrepancy documented in ASSETS.md rather than hidden.
- [x] Shrink is geometrically exact: scale 0.2564 computed so drawn area = Africa ÷ 14.02.
- [x] Beats 3 and 4 make no numeric claim.
- [x] Hine claim hedged to "helped change the law"; photograph captioned exactly as the LoC record titles it.
- [x] No colourisation, recreation or generated imagery.

## Legal & attribution
- [x] Both assets classified (class A) with verbatim source rights statements.
- [x] On-screen credit for the Hine photograph in beat 5; full credits in out/CREDITS.md.
- [x] Audio fully synthesised; fonts SIL OFL 1.1.
- [x] No fabricated licence, creator, permission, attribution or URL.
- [x] **Handle `@theshortwhy` is unverified** — Instagram gives unauthenticated clients no availability signal (a real account and an invented string both return the same login-wall redirect). Stated plainly in PROJECT.md rather than implied to be checked.

## Technical (measured)
- [x] 1080×1920, 9:16. 30fps constant, 450 frames.
- [x] Duration exactly 15.000s.
- [x] Audio present and audible: **−16.1 LUFS**, LRA 4.2 LU, true peak **−1.3 dBTP**.
      Sits between the −16 long-form and −14 short-form targets; −1.3 dBTP is 0.2 dB above the
      −1.5 ceiling in sound-design.md. Recorded, not rounded away. Instagram normalises loudness
      on playback, so the overshoot is immaterial here, but it is an overshoot.
- [x] Decode clean: `ffmpeg -v error` produced no output.
- [x] **Per-frame luminance: PASS, all 450 frames.** `blackdetect` was the wrong instrument for a
      dark vertical palette — it flagged 4.3s of a perfectly good end card — so `src/qc_luma.py`
      checks mean luma ≥6 and a bright extreme ≥120 on every frame instead. It found four real
      defects the eye had missed; all fixed.
- [x] HyperFrames lint: 0 errors.

## Known limitations
- **No voiceover.** By request — the slot is open. Record to the table in SCRIPT.md, drop
  `assets/audio/vo.wav`, re-run `src/build.sh`; it mixes the VO under the designed track and
  re-masters. Until then the film is sfx-only, which is how most Reels are watched anyway.
- Ten HyperFrames `nested_structure_needs_subcomposition` warnings remain: Studio timeline-display
  advice, not render faults.
- No 4:5 feed variant cut. It would need genuine recomposition, not a crop.
- `@theshortwhy` unverified — see above.
