# THE SHORT WHY — Instagram page trailer

## Brief
A 15-second Reels trailer for an educational page covering geography, economics, psychology
and history. It must hook in under 2 seconds, prove the page is worth following with one real
fact, show range, state the promise, and ask for the follow.

## Specification
- 9:16, 1080×1920, 30fps, 15.000s — composed vertical, never cropped from a horizontal cut
- Works **muted**: every line is burned-in kinetic type, because Reels autoplay silent
- Voiceover: **slot left open** — the user is recording it. See the timing table in SCRIPT.md.
- Deliverable: `out/shortwhy_reel.mp4`

## Handle
`@theshortwhy` is a **suggestion, not a verified-available handle.** Instagram serves
unauthenticated requests nothing: a known-real account (`natgeo`) and a string I invented both
returned the identical 302 to the login wall, so no availability signal exists from here.
Check it in Instagram's signup form, which validates live. The handle and wordmark are two
strings in `src/index.html` (`#ct1`, `#ct3`) — swapping them is one edit plus a re-render.

I did **not** create the account: registration requires the holder's own email/phone and
identity, and automated signup breaches Instagram's terms.

## Status
| Stage | State |
|---|---|
| 1 Research & verification | done — areas cross-checked, Hine claim hedged |
| 2 Script & beats | done — SCRIPT.md |
| 3 Visual research | done — 1 photograph + Natural Earth geometry |
| 4 Art direction | done — ART_DIRECTION.md |
| 5 Storyboard | done — STORYBOARD.md |
| 6 Asset prep | done — src/prepare_assets.sh |
| 7 Graphics & animation | done — src/index.html (HyperFrames) |
| 8 Edit | done |
| 9 Sound & grade | done — src/audio.py |
| 10 QC | done — QC.md |
| 11 Export | done — out/shortwhy_reel.mp4 |

## Decisions log
| Decision | Reason |
|---|---|
| Map drawn from Natural Earth, not a scanned antique map | Colton's 1854 Mercator is beautiful but its Greenland is overprinted with distance tables, so the cutout would have been dirty. Real geometry also makes the shrink exact. |
| 14× sourced from published areas, not from the drawing geometry | NE 110m is simplified and yields 13.72; the official figures give 14.02. Draw with one, cite the other. |
| Beats 3 and 4 are questions, not statistics | I will not invent a coffee-price breakdown to fill two seconds. A trailer teases; the page delivers. |
| "helped change the law", not "ended child labour" | Keating–Owen (1916) was struck down in 1918; federal limits came with the FLSA in 1938. The hedge is deliberate. |
| Per-frame luminance check replaces blackdetect | On a #0C1018 vertical frame most pixels are legitimately dark, so blackdetect fired on a perfectly good end card. See src/qc_luma.py. |
| Brighter accent than the long-form palette (#FFB020) | Reels are watched outdoors on auto-brightness screens. |
