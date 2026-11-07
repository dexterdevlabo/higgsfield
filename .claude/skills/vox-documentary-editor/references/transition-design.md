# Transition Design Engine

A transition is an argument about the relationship between two ideas. If there is no
relationship to express, use a hard cut.

## Vocabulary

Match cut · graphic match · shape-based transition · mask reveal · whip pan · push · pull-back ·
camera-zoom transition · map-to-photograph · image-to-image · object-driven wipe · typographic
transition · parallax transition · morph (only when both forms genuinely share topology) ·
layered dissolve · motion-continuous cut.

## Selection rule

Choose by narrative logic, in this order of preference:

1. **Hard cut** — new idea, no claimed relationship. This is the default and should be the
   majority of the film.
2. **Motion-continuous cut** — the move continues across the cut. Use when the idea continues.
3. **Graphic match** — a shape in shot A is replaced by a matching shape in shot B. Use when
   you are asserting *this is like that*.
4. **Shape / mask reveal** — a form in A grows or shrinks to become B's frame. Use for
   zooming in on a part, or pulling out to a whole.
5. **Push / zoom** — spatial relationship. Use for geographic descent (continent→city) or
   scale change (macro→micro).
6. **Dissolve** — time passing, or two states of one thing. Never as a generic softener.
7. **Whip pan** — abrupt change of place with energy. Maximum once or twice per film.

A transition that could be swapped for any other transition without changing meaning is the
wrong transition. Delete it.

## Concept examples

Treat as concepts to adapt, not templates:

- A map zooms into a country and the final frame of the zoom resolves into a photograph of its capital.
- A circular annotation drawn around a detail expands until its interior *is* the next scene.
- A newspaper headline scales up until the halftone grain fills frame, revealing the photograph the story described.
- A photograph pulls back to show it was one card in a larger collage of the same event.
- A highlighted national border detaches and becomes the baseline of the next bar chart.
- An object crossing frame (train, ship, aircraft) wipes to the next shot as it passes.
- A single spoken word sets as type, then expands into the act title.

## Specification format

For every non-cut transition, record in `STORYBOARD.md`:

1. Outgoing shot (and its last visual state)
2. Incoming shot (and its first visual state)
3. Mechanism (from the vocabulary above)
4. Motion direction
5. Duration (frames and ms)
6. Easing
7. Mask / shape, with geometry
8. Sound effect and its offset
9. Continuity requirements (what must align: scale, position, color, luminance, subject eyeline)

Example:

```
T-07  shot 12 → shot 13
  mechanism   mask reveal (circle)
  out state   annotation circle, center (1180, 460), r=96px, accent stroke
  in state    photograph of the dam, framed so the spillway sits at (1180, 460)
  direction   radial outward
  duration    14 frames @24fps (583ms)
  easing      cubic-bezier(0.22, 1, 0.36, 1)
  mask        circle, r 96→1420px, feather 2px
  sfx         soft air-swell, -20 LUFS, starts 80ms before the reveal
  continuity  spillway must land within 12px of circle center; luminance matched ±5%
```

## Consistency

Each film declares 3–5 permitted transitions in `ART_DIRECTION.md` and uses no others. The
same relationship always gets the same transition, so the viewer learns the grammar. Reserve
one heavier device (act-break dip, whip pan) for structural boundaries only.

## Prohibited

Preset wipes, page curls, star irises, light-leak packs, randomised "transition packs" ·
transitions on every cut · transitions longer than 700ms outside act breaks · morphs between
unrelated shapes · effects that make the film read as a slideshow or a product advertisement.
