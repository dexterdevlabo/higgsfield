# Color Theory & Palette Construction

Color is a storytelling instrument. Choosing it is a creative decision made before
production, from the subject — never sampled from whatever image happens to be on screen.

## Method

1. **Read the subject.** Era, geography, material culture, emotional register, and the
   dominant color that already exists in its authentic imagery.
2. **Choose a scheme.** One of:
   - *Complementary* — two opposed hues. Strong for conflict, two-sided comparisons, before/after.
   - *Analogous* — neighbouring hues. Cohesive, calm; good for one continuous process.
   - *Split-complementary* — a base plus the two neighbours of its complement. Rich without clashing; the safest expressive choice.
   - *Monochromatic* — one hue, varied in luminance and saturation, plus one foreign accent. Extremely disciplined; excellent for data-heavy films.
   - *Triadic* — three evenly spaced hues. Use only with one dominant and two subordinate.
3. **Set a temperature contrast.** Decide what is warm and what is cool, and what that *means*
   in this film. Do not let it drift.
4. **Build a luminance ladder** before worrying about hue: background darkest, structure mid,
   accent brightest. If the palette fails in greyscale, it fails.
5. **Assign purpose per color** (table in `ART_DIRECTION.md`). A color with no job gets deleted.
6. **Verify contrast.** All type ≥ 4.5:1 against its background; ≥ 3:1 for ≥24px bold.
   Accents carrying information must also be distinguishable by position, shape or label —
   never by hue alone (≈8% of male viewers are red-green deficient).

## Historical and material references

Ground the palette in something real:
- Era-accurate print inks, propaganda posters, uniform dyes, flag specifications.
- The actual geology, vegetation or water of the region.
- Period film stock behaviour (Kodachrome warmth, Agfa greens, orthochromatic skies).
- Scientific convention (NASA false-color standards, geological map keys, IPCC warming stripes).

Cite the reference in `ART_DIRECTION.md`. "Looks nice" is not a reference.

## Color as narrative

A palette may evolve when the story justifies it, through a **declared** arc:

```
Act I  (origins)      analogous earth tones, saturation 70%
Act II (escalation)   accent shifts from #E0A31C to #C0392B as the conflict widens
Act III(consequence)  saturation drops to 45%, backgrounds darken two steps
```

Write the arc into `ART_DIRECTION.md` with the exact shot numbers where each shift lands, and
make the shift gradual across a transition — never as an unexplained jump between adjacent cuts.

Illustrative subject-specific logics (**adapt, never copy**):
- *Cold War* — muted archival tones; cold blue for geopolitics; red accent strictly for military escalation; neutral plates for factual explanation.
- *Climate* — natural greens and earths; warm orange→red only for anomaly magnitude; darker tones for consequence; clean neutral plates for the science.
- *Economics* — monochrome structure so that a single accent can carry the quantity being discussed.

## Image color treatment

Make every photograph, archival scan and illustration feel like part of one film:
grade, exposure, contrast, saturation, black level, highlight rolloff, grain, texture,
vignette, tonal separation. Define **separate recipes per asset class** (archival B/W,
archival color, modern photography, maps, documents) that all resolve to one black level,
one grain level and one highlight character.

Constraints:
- Preserve the documentary information in the frame. Do not crush detail out of evidence.
- Do not recolor archival material in a way that changes what it appears to show.
- Colorisation, if used at all, is labelled on screen as a recreation.

## Prohibited

Random palette changes between shots · saturation above what a calibrated display handles ·
more than two accents · unreadable type · gradients with no purpose · neon glow as a default ·
palette colors that compete with the subject of the photograph they frame.

## ImageMagick recipes

```bash
# Unified black level + contrast + slight desaturation (archival color)
convert in.jpg -modulate 100,75 -level 2%,98% -brightness-contrast 0x8 out.png
# Warm-highlight split tone on B/W archival
convert in.jpg -colorspace Gray +level-colors '#120E0A','#D8C3A0' out.png
# Film grain, uniform across the film (apply at render, not per asset)
convert in.png -attenuate 0.25 +noise Gaussian -colorspace sRGB out.png
# Vignette
convert in.png -background black -vignette 0x18+0+0 out.png
# Check greyscale legibility of a palette swatch sheet
convert palette.png -colorspace Gray gray_check.png
```
