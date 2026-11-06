# Art Direction — THE SHORT WHY (page trailer)

## Concept
A night desk with one lamp on it. Deep cool field, blue structural graphics, and a single hot
amber that only ever marks the thing you are supposed to look at. Built for a phone held at
arm's length in daylight: high contrast, large type, one idea per frame.

## Palette
Split-complementary — blue-slate structure (hue ~212°) against an amber accent (~38°).

| Role | HEX | Purpose |
|---|---|---|
| bg-deep    | #0C1018 | base plate, sea |
| bg-raised  | #161C27 | panels, cards, chart ground |
| primary    | #31506F | landmasses, chart bodies, structure |
| secondary  | #6E7F94 | de-emphasised structure (Africa before the reveal) |
| accent     | #FFB020 | the single thing that matters now; ≤12% of frame |
| alert      | #E2513C | reserved; unused in this cut |
| text       | #FFFFFF | all headline type |
| muted      | #93A3B5 | credits, slugs, captions only |

Contrast on bg-deep: text 18.4:1 · accent 10.6:1 · muted 7.1:1. All ≥4.5:1.
Accent is brighter than the kite trailer's (#E8A33D → #FFB020) because Reels are watched
outdoors on auto-brightness screens.

## Typography
Headline: **Inter Display Bold**, −2.2% tracking, leading 0.98. Large — 96–124px at 1080 wide.
Supporting: **Inter SemiBold**, +12% tracking, uppercase, for slugs and chips.
Figures: **JetBrains Mono Bold**, tabular, so the 14× counter cannot jitter.

## Image treatment
Photographic (Hine, 1910): desaturate to 0, then split-tone shadows → #101722, highlights →
#D9D2C4. Black level lifted to 6%. Nothing is colourised; no content is altered.
Cartography: drawn natively in palette colours from Natural Earth geometry — never graded.

## Motion language
System **A editorial** + **C cartographic** (hook) + **E data-driven** (beat 2).
- Entrance 380ms, `power4.out`, 22px travel — faster than long-form, this is a Reel.
- Exit 200ms, `power3.in`, opacity only.
- Stagger 70ms. Camera drift ≤4%, `power1.inOut`.
- The Greenland shrink is the one hero move: 1.1s, `power3.inOut`, scale and translate together.

## Transition language
Three permitted, no others:
1. **hard cut** — default, between unrelated topic beats.
2. **graphic match** — Greenland's shrunken form becomes the first chart bar.
3. **shape mask** — the end card opens over the last beat.

## Texture, lighting, layout
Uniform 5% grain and a 12% vignette, applied once globally. Flat lighting; cards in beat 2 cast
one 0/14px 30%-black shadow. 60px side margins. **Top 230px and bottom 420px stay clear of
Instagram UI** — no essential type or subject enters those bands. The focal element sits at y≈760.

## Annotation design
Accent ring: 5px stroke. Label chips: bg-raised, 8px radius, 12/18px padding, uppercase
Inter SemiBold. Leader lines 4px. All annotation is original; none is traced from a source.

## Sound character
Dry, punchy, low-mid, mixed for phone speakers: more mid-band presence and less sub than the
long-form spec, because a phone speaker reproduces almost nothing below 200 Hz.
