# Style preset — Mustard Paper Collage

A named art-direction preset: torn-paper, screen-print, cut-collage editorial posters.
Riso/newsprint feel, two flat inks plus photographic halftone, everything slightly askew and
taped to the wall. Use it when a project wants handmade authority rather than clean
institutional polish.

All values below were **measured from a reference sheet**, not estimated. Proportions are the
share of frame each colour occupied across nine posters.

## Palette

| Role | HEX | Share | Use |
|---|---|---|---|
| ground | `#DAA51E` | ~24% | the card itself; the dominant field |
| paper | `#EBE8DE` | ~22% | torn banners, cut mounts, the backdrop behind the card |
| ink | `#000000` | ~9% | headlines, illustration, silhouettes — a true black, not a soft one |
| accent | `#C23D38` | ~3% | targets, arrows, alerts, one chip, caution strips |
| tape | `rgba(226,208,160,.72)` | — | translucent masking tape |
| halftone grey | emergent | — | not a colour; the dot screen reading as grey at distance |

**The 3% rule.** Red is an accent in the strict sense: it occupied about three percent of the
reference frames. Two or three red incidents per poster, never a red region. If red is
carrying an area rather than a point, the palette is already broken.

The ground does not have to be mustard. Swap it for the project's hue and keep the
*relationships*: one saturated mid-value field, one near-white paper, true black ink, one hot
accent at ~3%.

## Hierarchy — the thing most easily got wrong

**Flat black graphic illustration is the subject. Halftone photography is texture.**

The reference's hero elements are bold cut-paper/vector forms — a keyboard, an oil derrick,
a pair of scales, a slot machine. Photographs appear halftoned and *secondary*: a face, a
globe's shading, a figure. Leading with a halftoned photograph produces a grey mush with no
focal point. Build the subject in flat black first; add halftone only where a surface needs
grain or a human face is required.

## Element vocabulary

Nine devices. Use five or six per composition, never all nine.

1. **Torn banner** — the headline sits on a strip of paper with a *torn* edge.
2. **Masking tape** — two to four translucent pieces, rotated 14–26°, pinning the card down.
3. **Halftone patch** — an angled dot screen, usually at reduced opacity, behind or beside the subject.
4. **Cut mount** — a torn paper rectangle the illustration sits on.
5. **Label chips** — small paper rectangles with tight uppercase text; one may be red-filled.
6. **Stamped target** — concentric accent rings with a filled centre, rotated, overlapping an edge.
7. **Confetti** — small black / red / cream triangles and rectangles at random rotations.
8. **Repeated strip** — `CAUTION // CAUTION //` or similar, running off both edges.
9. **Breakout** — one element crossing its container's boundary. Without this the page feels contained and dead.

## Geometry

- **Nothing is square.** Card −0.5°, banner −1.3°, mount +0.8°, chips ±1.5–3°, tape 14–26°, stamp −8°.
  Rotations stay under 4° for anything holding text.
- **Tear amplitude** ~9px on a banner, ~11px on a large mount, at 1080px width. Larger reads as sawtooth.
- Drop shadows are short and warm: `0 7px 10px rgba(60,40,10,.34)`.

### Torn edges

A uniform zigzag reads as cut card, not torn paper. Paper tears **mostly straight with
occasional deeper bites**, at irregular intervals:

```js
const edge=(len,fn)=>{let d=0;while(d<len){d=Math.min(len,d+7+r()*17);
  const bite=(r()<0.22? amp : amp*0.30)*(r()-0.5)*2; p.push(fn(d,bite));}};
```

Seed the PRNG so the tear renders identically every frame — a tear that reshuffles per frame
boils distractingly.

## Typography

| Role | Face | Size @1080w | Notes |
|---|---|---|---|
| Headline | heavy grotesque, uppercase | 90–100px | ideal: Archivo Black or Anton. Installed fallback: **Boldonse** (closest weight). BigShoulders is too condensed; Outfit and Work Sans are too light. |
| Subtitle | humanist sans, regular, lowercase | 32–34px | Work Sans Regular. Sits ~14px under the headline, centred. |
| Chips / strips | humanist sans, bold, uppercase | 19–26px | tracking +0.09em to +0.22em |

Headline tracking −1.2%. Headlines are centred on the banner and share its rotation.

## Halftone recipe

ImageMagick 6. The downsample width sets dot size — smaller input, chunkier dots.

```bash
# angled newsprint screen (the default)
convert in.jpg -colorspace Gray -normalize -brightness-contrast 4x14 \
  -resize 150x -ordered-dither h8x8a -resize 760x -filter point PNG24:out.png

# chunkier circular screen
convert in.jpg -colorspace Gray -normalize -resize 150x -ordered-dither c7x7b \
  -resize 720x -filter point PNG24:out.png

# knock the white out so it reads as a cut element rather than a photo print
convert out.png -transparent white PNG32:out_cut.png
```

IM6 requires suffixed map names (`h8x8a`, `h6x6a`, `c7x7b`). Plain `h8x8` is rejected.
**Normalise and add contrast before dithering** — an un-normalised source halftones to mush.

## Motion language

The style is cut paper, so it must move like cut paper, not like vector UI.

- **Step the frame rate.** Hold elements on 2s or 3s (effectively 10–15fps) while the camera
  and grain stay at full rate. Smooth 30fps easing destroys the handmade read.
- **Entrances are drops, not fades.** An element falls 20–40px with a 4–8° rotation settling to
  its rest angle, `back.out(1.6)`, 260–360ms. Paper has weight and overshoots slightly.
- **Tape first, then the card.** Then banner, then subject, then labels, then confetti.
  60–90ms stagger.
- **Confetti bursts** on an impact beat and settles; it does not drift.
- **Halftone boil**: nudge the dot-screen phase every 3rd frame for a living print texture.
  Keep it subtle — one or two pixels.
- **Transitions**: a new card slides in over the old one, or a torn strip wipes across. No
  dissolves; paper does not cross-fade.
- **Sound**: paper movement, tape pull, a stamp thud on the target, a short riso-roller hiss
  under transitions.

## Prohibited

Gradients on the ground beyond a faint uneven-ink mottle · soft pastel tints · drop shadows
longer than ~12px · more than one red region · perfectly axis-aligned elements · smooth
30fps eases on paper elements · halftone as the hero · a fourth flat colour.

## Worked example

`examples/paper-collage-poster.html` renders a complete poster in this preset: measured
palette, torn banner, flat-black subject with halftone behind, stamped target, chips,
confetti, breakout arrow and grain. Screenshot it with Playwright at 1080×1440, or mount it
as a HyperFrames composition and animate it with the motion rules above.
