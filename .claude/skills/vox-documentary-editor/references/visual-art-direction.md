# Visual Art Direction

Stage 4. Nothing is produced before this document exists. Output: `ART_DIRECTION.md` in the
project directory, with concrete values — not adjectives.

## The fourteen declarations

Every project declares all fourteen. "Default" is not an answer.

1. **Primary palette** — 2–3 HEX values carrying most of the screen.
2. **Secondary palette** — 2–3 HEX values for supporting structure.
3. **Accent colors** — 1–2 HEX values, reserved for meaning (see `color-theory.md`).
4. **Backgrounds** — the base plate(s) everything sits on, plus any gradient/texture rule.
5. **Typography** — headline / supporting / body families, weights, tracking, line height.
6. **Image treatment** — the grade recipe applied to photography so all stills belong together.
7. **Illustration style** — line weight, fill behaviour, corner radius, level of abstraction.
8. **Motion language** — one of the five systems in `animation-principles.md`, with durations and easing curves.
9. **Transition language** — the 3–5 transitions this film is allowed to use, and when.
10. **Texture & grain** — grain strength, paper/print texture, halftone, scanline — or explicitly none.
11. **Lighting & shadows** — shadow direction, softness, opacity; or flat with no shadows.
12. **Composition & layout** — grid, margins, safe areas, where text lives, where subjects sit.
13. **Annotation design** — arrows, circles, brackets, callout lines, label chips, highlight fills.
14. **Sound design character** — the sonic palette (see `sound-design.md`).

## Writing the document

Template:

```markdown
# Art Direction — <project>

## Concept
One paragraph: what this film *feels* like and why that serves the subject.
e.g. "A declassified file being opened on a cold desk." Everything below descends from this.

## Palette
| Role | HEX | Purpose | Where it may appear |
|---|---|---|---|
| bg-deep      | #0E1116 | base plate                | full-frame backgrounds |
| bg-raised    | #171C24 | panels, cards, map seas   | inset surfaces |
| primary      | #2B4C6F | structural graphics, landmasses | shapes, chart bodies |
| secondary    | #8C9BAB | secondary data, inactive regions | de-emphasised elements |
| accent       | #E0A31C | the single fact that matters now | ≤12% of frame |
| alert        | #C0392B | escalation, danger, loss  | sparingly, never decoratively |
| text         | #F2F5F8 | all readable type         | headlines, labels |
| text-muted   | #93A0AE | captions, attribution      | small type only |

Contrast checks: text on bg-deep = 15.4:1. accent on bg-deep = 8.1:1. All ≥ 4.5:1.

## Typography
Headline: Archivo 700, tracking -2%, line-height 1.02, uppercase for titles only.
Supporting: Inter 600, tracking 0, line-height 1.25 — labels, lower thirds, map names.
Body/caption: Inter 400, tracking +1%, line-height 1.45 — attribution, footnotes.
Numerals: tabular lining everywhere a number animates.

## Image treatment
Archival B/W: lift blacks to 6%, warm highlights +4 toward #D8C3A0, grain 2.5%, vignette 12%.
Archival color: desaturate 25%, contrast +8%, cool shadows toward primary.
Modern photo: neutral grade, saturation 95%, grain 1.5%, matched black level 6%.
Maps/diagrams: never graded — rendered natively in palette colors.

## Illustration style
2px strokes at 1080p (scale with resolution), flat fills, no gradients except one 8%
top-down vignette on full-frame plates. 4px corner radius. Geometric, not sketchy.

## Motion language
System: editorial motion graphics (A) with cartographic sequences (C) for geography beats.
Entrances: 420ms, cubic-bezier(0.16, 1, 0.3, 1), 60ms stagger, 24px travel, opacity 0→1.
Exits: 260ms, cubic-bezier(0.7, 0, 0.84, 0), no travel, opacity 1→0.
Camera pushes: ≤4% scale over ≥3s, linear-ish (0.4,0,0.6,1).

## Transition language
Allowed: hard cut (default), 300ms map-zoom push, shape-mask wipe on accent circles,
graphic match on repeated forms, 8-frame dip for act breaks. Nothing else.

## Texture & grain
Uniform 2% luma grain over the whole film, applied at render, not per asset.

## Lighting & shadows
Cutouts cast one shadow: 0px x / 18px y, 32px blur, 28% black. One light direction, top.

## Layout
12-column grid, 80px side margins at 1080p. Title safe 120px. Lower third baseline at y=880.
Narration-synced labels enter from the side the subject faces.

## Annotation design
Accent circles: 3px stroke, dashed 8/6, drawn-on over 500ms. Arrows: 3px, 12px arrowhead,
always curved with one control point. Label chips: bg-raised, 6px radius, 10/14px padding.

## Sound character
Dry, close, low-mid. Transition whooshes short (<300ms) and dark. One sub impact per act.
