# Motion Design Engine

Animation is a storytelling element, not decoration. Every movement must be justifiable in
one sentence: *what does this motion tell the viewer?* If there is no answer, it is a cut.

## Principles in use

Ease-in/ease-out · anticipation · follow-through · overlapping action · staggered entrances ·
controlled acceleration · momentum · depth · parallax · mask reveals · motion tracking ·
camera movement · scale / position / opacity transitions · motion blur where physically implied.

Banned: random bounce · gratuitous zooming · decorative rotation · stock preset animations ·
inconsistent easing within one film · aggressive transitions · everything moving at once.

## Choose one animation system per project

**A. Editorial motion graphics** — precise moves, clean type, smooth reveals, controlled
transitions, minimal decorative motion. The default for explanation-heavy films.

**B. Cinematic documentary** — slow camera moves, layered photography, depth and parallax,
atmospheric transitions, subtle motion. For emotional and place-driven films.

**C. Cartographic** — animated routes, moving highlights, map zooms, region reveals, animated
boundaries and labels. For geography, geopolitics, logistics, migration.

**D. Archival collage** — photographic cutouts, paper texture, layered documents, elements
moving independently, animated historical artifacts. For history and biography.

**E. Data-driven** — charts, graphs, counting numbers, timelines, animated comparisons,
dynamic labels. For economics and science.

Combine only when compatible (A+C and A+E are natural; B+E usually fights itself). Declare
the combination and which system owns which act.

## Easing vocabulary

Pick these once per project and never deviate.

| Role | Curve | Duration |
|---|---|---|
| Entrance (standard) | `cubic-bezier(0.16, 1, 0.3, 1)` | 380–460ms |
| Exit | `cubic-bezier(0.7, 0, 0.84, 0)` | 220–280ms |
| Emphasis / pop | `cubic-bezier(0.34, 1.3, 0.64, 1)` | 300ms, overshoot ≤6% |
| Camera push / drift | `cubic-bezier(0.4, 0, 0.6, 1)` | 2.5–8s |
| Map zoom | `cubic-bezier(0.22, 1, 0.36, 1)` | 900–1400ms |
| Counting number | linear with 200ms ease-out tail | match VO length |

Stagger: 50–80ms per sibling element; cap a stagger group at 7 items, then batch the rest.
Travel distance: 16–32px at 1080p. Longer travel reads as sloppy, not dramatic.

## Specification format

Never write "animate this image." Write:

```
SHOT 14 — Suez chokepoint
  Layer 1 bg-map        hold, scale 1.00→1.04, 0→6000ms, (0.4,0,0.6,1)
  Layer 2 canal-stroke  mask reveal L→R, 0→1200ms, (0.16,1,0.3,1), 3px accent stroke
  Layer 3 ship-cutout   x -120px→+1240px, 800→5600ms, linear, 6px motion blur
  Layer 4 label "SUEZ"  y +24→0px, opacity 0→1, 1100→1500ms, (0.16,1,0.3,1)
  Layer 5 figure "12%"  count 0→12, 2400→3000ms, tabular numerals, accent fill
  VO sync   "twelve percent of global trade" lands at 2400ms
  SFX       low whoosh at 0ms (-18 LUFS); soft tick at 1100ms; sub impact at 2400ms
  Out       hold final frame 400ms before cut
```

Every movement states: start, end, duration, easing, direction, scale, opacity, rotation (if
any), stagger, relationship to VO, relationship to SFX. Build this per shot into
`STORYBOARD.md`; for complex sequences write a separate keyframe plan file in `build/`.

## Timing against narration

- A graphic element appears **60–150ms before** the word it illustrates, so the viewer has
  found it by the time the word lands. Never after.
- A number finishes counting **on** the stressed syllable of its spoken value.
- A map finishes its zoom **before** the next clause begins; motion under speech competes with it.
- Hold the final state ≥400ms before cutting. Cutting on motion reads as an error.
- Nothing new enters during the last 300ms of a shot.

## Implementation notes

Use `technical-production.md` for the mechanics. In short: express easing as an ffmpeg
expression or a Remotion `interpolate` with a bezier, generate per-frame PNGs from Python/PIL
or SVG when the move is geometric, and reserve Remotion for timelines with many synchronized
typographic layers. Motion blur: only on objects crossing >25% of frame width per second.
