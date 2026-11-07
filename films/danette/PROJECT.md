# Danette — concept film

15.0s · 16:9 · 1920×1080 · 30fps. A **spec/concept** film for Danone's Danette brand,
made to demonstrate the pipeline. Not an official Danone production, and marked as such
on the final frame.

## Idea
Danette's own historic slogan is *"On se lève tous pour Danette!"* — "let's all stand up for
Danette". That is a gift: the film's hero move is **type that physically stands up**. Four
words hinge upright off a caramel rule, and the whole film builds to them.

## Structure
| Beat | Window | What |
|---|---|---|
| 1 | 0.00–3.30 | A cream swirl pipes itself onto a chocolate field. *Depuis 1970 / Une cuillère qui fait lever la France.* |
| 2 | 3.30–6.45 | Three flavour fields rise — Chocolat, Caramel, Vanille. |
| 3 | 6.40–9.45 | *En France · 1 sur 2 · en mange.* |
| 4 | 9.40–12.75 | **On se lève tous** — each word stands up off the rule. |
| 5 | 12.60–15.00 | *pour Danette.* · Depuis 1970, opened by a shape mask. |

## What I deliberately did not do
- **No Danone logo, wordmark or packaging.** Those are trademarks; the film sets the brand
  name in a licensed typeface and never reproduces their identity assets.
- **No product photography.** Danone's site imagery is copyrighted. Nothing was scraped.
  The hero visual is an Archimedean spiral generated in the composition — original geometry.
- **No invented claims.** Every statement on screen is traceable to Danone's own brand page
  (see ASSETS.md). No nutrition, ingredient, award or comparative claim appears.
- **Palette is sampled from the dessert**, not from Danone's brand guidelines, which the page
  does not publish. Chocolate / caramel / vanilla / cream.

## Facts used, and where they come from
All from danone.com's Danette brand page:
- launched **1970** → "Depuis 1970"
- flavours **chocolate, caramel, vanilla** → "Trois classiques"
- "**one in two French people** consume Danette products" → "En France · 1 sur 2 · en mange"
- historic slogan "**On se lève tous pour Danette!**" → beats 4–5

## Verification
Measured on the delivered file: 15.000s, 450 frames, decode clean, −16.9 LUFS, −1.8 dBTP,
per-frame luminance PASS on all 450. HyperFrames lint 0 errors.

## Fixed during QC
The luminance check caught four scene openings that carried nothing on their first frames —
beats 2, 3 and 4 each cut to an effectively empty frame for 0.1–0.2s. Rather than loosen the
threshold, the shots were strengthened: the kickers are now present on the cut, and the
slogan's first word starts already lying on the rule and rises, instead of fading in.

## If this goes forward
Real production would swap in Danone's official brand assets — logo lockup, approved type,
brand colour values and product photography — and legal would review the slogan use. The
film is built so those are drop-in: colours are CSS custom properties, and the end card's
strings are three lines of HTML.

## Formats
16:9 as delivered. A 9:16 Reels cut is a recomposition, not a crop — the three flavour
fields would stack and the slogan would re-break to two lines.
