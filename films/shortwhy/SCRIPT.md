# Script — THE SHORT WHY (15.0s page trailer)

No voiceover in the rendered cut: the user is recording it. Every line below is also burned in
as kinetic type, because Reels autoplay muted and the film has to work silent.

| # | In–Out | Line (VO + on-screen) | Why it earns its place |
|---|--------|-----------------------|------------------------|
| 1 | 0.00–2.00 | **"Every map you've seen is lying to you."** | The hook. An accusation about something the viewer owns and trusts. No branding yet — nothing is earned at 0.0s. |
| 2 | 2.00–4.40 | **"Greenland looks as big as Africa."** → **"It's 14× smaller."** | The payoff, delivered visually. This is the page's proof of value: a real, checkable fact in 2.4 seconds. |
| 3 | 4.40–6.40 | **"Why your coffee costs what it does."** | Range: economics. A question, not a statistic. |
| 4 | 6.40–8.40 | **"Why you forget a name the second you hear it."** | Range: psychology. |
| 5 | 8.40–10.60 | **"How these photographs changed the law."** | Range: history, and the one beat with emotional weight. Hine's NCLC photographs drove US child-labour reform. |
| 6 | 10.60–12.80 | **"One idea. Ninety seconds. Every week."** | The promise — format, length, cadence. The only "sales" line in the film. |
| 7 | 12.80–15.00 | **"THE SHORT WHY — @theshortwhy"** | CTA. |

~44 words. Trailer pace.

## Accuracy notes
- **"14× smaller"** uses the official published areas: Greenland 2,166,086 km² (Statistics
  Greenland) ÷ Africa ≈30,370,000 km² = 14.02. The drawing geometry (Natural Earth 110m) is
  simplified and yields 13.72; it is used to draw the map, never to source the claim.
- **"Looks as big as Africa"** is measured, not asserted: on the rendered Mercator window
  Greenland occupies 185,745 px against Africa's 171,176 px — 1.09×. The shrink animation
  scales Greenland by 0.2564 so its drawn area lands at exactly Africa ÷ 14.02.
- Beats 3 and 4 are **questions, not claims**. No invented statistic appears on screen.
- Beat 5 is a documented claim: Hine's National Child Labor Committee photographs are credited
  with advancing US child-labour legislation. The wording "helped change the law" is hedged
  deliberately — Keating–Owen (1916) was struck down in 1918, and federal limits arrived with
  the Fair Labor Standards Act in 1938.

## Voiceover recording guide
Record 44 words to these in-points; the composition's type is already timed to them.
Target −16 LUFS, high-passed at 80 Hz, dry (no room). Drop the file at
`assets/audio/vo.wav` and re-run `src/build.sh`.

| In | Line |
|------|------|
| 0.10 | Every map you've seen is lying to you. |
| 2.10 | Greenland looks as big as Africa. |
| 3.30 | It's fourteen times smaller. |
| 4.50 | Why your coffee costs what it does. |
| 6.50 | Why you forget a name the second you hear it. |
| 8.50 | How these photographs changed the law. |
| 10.70 | One idea. Ninety seconds. Every week. |
| 12.90 | The Short Why. |
