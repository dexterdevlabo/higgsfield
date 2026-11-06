# Why the Earth is not flat — THE SHORT WHY

10.0s · 9:16 · 1080×1920 · 30fps. Third piece for the page; reuses THE SHORT WHY art
direction unchanged, so no new art-direction cycle was needed.

## Editorial spine
Don't argue with flat-earthers — show the observation. The film opens on a real artefact
(Gleason's 1892 flat map), then spends its middle on a single demonstration: the same ship
receding on a flat plane and on a sphere. On the flat plane it only shrinks. On the sphere
the hull is occluded before the mast. That is the whole argument, and it is visual.

## Sourcing
The subject came from **The Public Domain Review**'s collection *"Earth Not a Globe":
Parallax's Zetetic Astronomy (1865)*. PDR labels that scan's **digital copy rights
"Unclear"** (possibly Internet Archive's CC BY-NC-SA default), which under
`copyright-and-attribution.md` is PENDING-REVIEW and cannot ship — so **none of PDR's image
files are used**. The underlying 1865 work is PD worldwide; the film instead uses a
rights-clean artefact of the same movement from Wikimedia Commons, and credits PDR for the
collection that led there. Same pattern as the kite film.

## Accuracy
- Gleason's map is captioned from the artefact itself, which prints "PATENT ALLOWED
  November 15, 1892".
- The ship demonstration is sound: on a sphere the line of sight is tangent to the surface,
  so a receding hull drops below the horizon before the mast. On a plane the ship subtends a
  smaller angle but is not occluded. This is precisely the observation Rowbotham's Bedford
  Level experiment tried to explain away; Alfred Russel Wallace's 1870 repeat with proper
  sighting showed the curvature.
- Both panels animate with **identical** shrink and travel. The only difference between them
  is the vertical settle behind the curved surface — so the comparison is fair, not rigged.

## Status / verification
Measured on the delivered file: 10.000s, 300 frames, decode clean, −16.4 LUFS, −2.1 dBTP,
per-frame luminance PASS on all 300 frames. HyperFrames lint 0 errors.

## Fixed during QC
- The ship first rendered as an indistinct blob at small scale and the "curved" sea read as
  flat. Ship redrawn with hull, mast, two sails and a flag; sea curvature tightened to a
  1700×820 arc so the dome is unmistakable.
- The sphere ship initially vanished completely, which made the on-screen note "the hull goes
  first" untrue of what was shown. The settle was reduced to 62px so the mast survives.
- The S1 caption collided with the foot of the map; the exhibit was scaled to 492×700
  (downscale only, never upscaled) to clear it.

## Known limitations
- No voiceover, consistent with the other pieces. Lines are on screen.
- The flat-map asset is 562×800 native, so it is shown as an exhibit card at reduced size
  rather than full-bleed. It is never upscaled.
- 8 HyperFrames `nested_structure_needs_subcomposition` warnings: Studio display advice only.
