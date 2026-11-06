# Typography & Graphic Design

Type is part of the art direction and often the primary graphic element. It carries facts, so
legibility outranks personality.

## Choosing families

Shortlist (all freely licensable; verify the specific licence):
Inter · Manrope · IBM Plex Sans / Plex Mono / Plex Serif · Source Sans 3 · Archivo (and
Archivo Expanded) · Space Grotesk · Libre Franklin · Public Sans · Playfair Display or
Source Serif 4 for editorial and historical registers. Helvetica/Neue Haas where licensed.

Match the family to the subject, not to taste: a grotesk with tight apertures reads
institutional and modern; a transitional serif reads archival and literary; a geometric sans
reads technical. Two families is the ceiling; one family across several weights is often stronger.

## The type system

Declare in `ART_DIRECTION.md`:

| Role | Family / weight | Size @1080p | Tracking | Line height | Case |
|---|---|---|---|---|---|
| Act title | Archivo 700 | 110px | -2% | 1.00 | upper |
| Headline / key stat | Archivo 700 | 72px | -1.5% | 1.05 | sentence |
| Subhead | Inter 600 | 40px | 0 | 1.20 | sentence |
| Label / map name | Inter 600 | 28px | +2% | 1.20 | upper |
| Lower third name | Inter 600 | 34px | 0 | 1.15 | sentence |
| Lower third role | Inter 400 | 24px | +1% | 1.25 | sentence |
| Caption / attribution | Inter 400 | 20px | +1% | 1.40 | sentence |
| Figures | Inter 600, tabular lining | per role | 0 | 1.0 | — |

Scale all sizes by resolution (×1.333 for 1440p, ×2 for 4K). Use tabular figures wherever a
number animates, or the layout will jitter as digits change width.

## Layout

12-column grid, 80px margins at 1080p. Title-safe inset 120px; action-safe 60px. Never place
type where a caption bar, subtitle track or platform UI will sit — for 9:16, keep the bottom
22% and top 12% clear. Align type to the grid and to the subject: label the thing, near the
thing, on the side it faces. Maximum line length 46 characters. Never more than two type
elements competing for attention in one frame.

## Type as storytelling

Oversized headlines for a single decisive fact · animated figures that count to their value ·
one highlighted keyword in accent colour inside a neutral sentence · editorial labels on map
regions · location markers · historical dates as a persistent corner slug · animated pull
quotes set in the editorial serif with the source attributed beneath · lower thirds that
appear 400ms after a speaker starts and leave after 4s.

## Kinetic type rules

- Enter with 24px travel and opacity, 420ms, project entrance easing. Never letter-by-letter
  typewriter effects except to depict actual typing.
- Word-level stagger at 50–70ms for a phrase that the narration is enumerating; otherwise
  animate the block as one object.
- Type lands 60–150ms **before** the word is spoken.
- Type is static while it is being read. Minimum dwell: 0.35s + 0.06s per word, and never less
  than 1.2s for anything the viewer must read.
- A keyword highlight animates its fill, not its position.
- Exit by opacity only, 240ms. Type that slides out draws attention away from the next shot.

## Subtitles

Burn-in only when the deliverable requires it; otherwise ship a sidecar `.srt`/`.vtt`. 40
characters per line, two lines maximum, 1.2s minimum duration, centred in the lower safe zone,
with a 70%-opacity plate behind if the background varies.

## Prohibited

Text on screen that the narration already said, with nothing added · more than two families ·
faux bold or faux italic · letter-spaced lowercase body text · drop shadows as a substitute
for contrast · type over a busy region of a photograph without a plate or scrim · centred
multi-line paragraphs · type smaller than 20px at 1080p.
