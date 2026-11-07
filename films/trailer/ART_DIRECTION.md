# Art Direction — Capability Trailer

## Concept
An archive table at night. A dark field, a cold blue structure of rules and labels, and the
warm ochre of old paper lit from above. The accent is not invented: it is sampled from the
ochre sky of the 1766 Harunobu print (srgb 182,161,128 → warmed to #E8A33D), so the graphics
and the artefacts share one light.

## Palette
Split-complementary: blue-slate base (hue ~212°) against amber accent (~38°), with one
desaturated red reserved for a single swatch.

| Role | HEX | Purpose | Where |
|---|---|---|---|
| bg-deep    | #0B0E13 | base plate | full-frame background |
| bg-raised  | #141A23 | panels, layer cards | inset surfaces |
| primary    | #2E4F72 | structural graphics | graticule, bar bodies, rules |
| secondary  | #7D8CA0 | secondary structure | inactive bars, minor lines |
| accent     | #E8A33D | the one thing that matters now | ≤12% of frame, never two at once |
| alert      | #C8503C | reserved | palette swatch row only |
| text       | #F4F7FA | all readable type | headline, labels |
| text-muted | #8E9BAA | slugs, captions | small type only |

Contrast on bg-deep: text 16.1:1 · accent 8.4:1 · text-muted 6.2:1. All ≥4.5:1.
Greyscale check: luminance ladder bg-deep < bg-raised < primary < secondary < accent < text. Passes.

## Typography
Headline: **Inter Display Bold**, tracking −2%, leading 1.00, uppercase for titles.
Supporting: **Inter SemiBold**, tracking +6% for small uppercase labels and slugs.
Figures: **JetBrains Mono Bold** — monospaced, so animated digits cannot jitter.

## Image treatment
Two asset classes, two recipes, resolving to one black level and one grain:
- **Woodblock (Harunobu, Hokusai)** — preserve the ochre; lift black to 6%, contrast +6%,
  saturation 96%. These are colour artefacts and must not be neutralised.
- **Photographic (LoC, 1910–17)** — desaturate to 0, then split-tone: shadows to #16120C,
  highlights to #D8C3A0, so the silver prints sit in the same light as the paper.
Neither recipe alters content. No colourisation; nothing is presented as other than what the
catalogue record says it is.

## Illustration style
2px strokes at 1080p (4px at the 2× render), flat fills, no gradients except one 10% radial
falloff on the base plate. 6px corner radius. Geometric, drafting-table, not sketchy.

## Motion language
System: **A editorial motion graphics** + **C cartographic** (shot 2) + **E data-driven** (shot 3).
- Entrance: 420ms, ease-out quint `1−(1−p)^5`, 24px travel, opacity 0→1
- Exit: 260ms, ease-in cubic `p^3`, opacity only
- Stagger: 60ms (≈1.5 frames @24fps, quantised to 2)
- Camera drift: ≤4% scale, smoothstep
- Sphere rotation: constant rate, no easing — machinery does not ease

## Transition language
Exactly four, each asserting a relationship:
1. **graphic match** S1→S2 — the annotation circle *is* the sphere (this is that)
2. **push** S2→S3 — scale/place change, left
3. **graphic match** S3→S4 — the tallest bar *is* the layer stack's edge
4. **shape mask** S4→S5 — the collapsed composite opens into the title
Nothing else. No dissolves.

## Texture & grain
Uniform 2% luma grain + PI/5 vignette, applied once at the final encode — never per shot.

## Lighting & shadows
Flat. One exception: the layer cards in shot 4 cast 0/18px 28%-black shadows, because the
whole point of that shot is depth.

## Layout
12-column grid, 80px margins at 1080p. Corner slug lives at (80, 980) and persists for the
whole film as continuity. Title-safe 120px.

## Annotation design
Accent circles: 4px stroke, drawn-on. Node dots: 8px filled accent with a 2px halo ring.
Label chips: bg-raised fill, 6px radius, 10/14px padding, Inter SemiBold uppercase.

## Sound character
Dry, low-mid, mechanical. Short dark whooshes (<300ms). One sub impact per shot boundary,
never two in 500ms. A near-inaudible filtered drone under everything.
