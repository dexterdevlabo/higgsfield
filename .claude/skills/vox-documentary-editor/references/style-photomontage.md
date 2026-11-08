# Style preset — Archive Photomontage

Die-cut scrapbook collage: engraving and photographic cut-outs, each ringed in a cream
keyline, pinned to a saturated aged-ink ground, with a sunburst behind. Dada photomontage by
way of a propaganda poster. Sibling of `style-paper-collage.md` — same chassis, three
important differences.

Values measured from a nine-poster reference sheet, not estimated.

## Relationship to the paper-collage preset

**Shared chassis.** Torn cream banner holding a heavy uppercase headline · masking tape at
the corners · scattered confetti · print grain · nothing axis-aligned · one true black.

**What changes:**

| | Paper Collage | Archive Photomontage |
|---|---|---|
| Ground | one mustard `#DAA51E` for the whole set | **a different saturated ground per card** |
| Subject | flat black vector illustration on a big torn white mount | **die-cut cut-outs with a cream keyline, straight on the ground** |
| Paper share | ~22% of frame | **~7%** — banner only, no mount |
| Accent | red `#C23D38` at ~3% | **gold tag `#C29532` at ~0.1%** |
| Subtitle | humanist sans | **serif** |
| Extras | — | sunburst rays, rosette seal, bottom caption |

## Palette

| Role | HEX | Share |
|---|---|---|
| paper | `#EBE5D0` | ~7% — warmer/yellower than preset A's `#EBE8DE` |
| keyline | `#EFE9D6` | — the die-cut outline |
| ink | `#211F1B` / `#000000` | ~10% |
| gold tag | `#C29532` | **~0.1%** |

### Grounds — a rule, not a list

Nine measured: `#C03C24` vermilion · `#CA9E4F` ochre · `#1A595F` teal · `#211F1B` near-black ·
`#6F8484` slate · `#484E2C` olive · `#AF6238` sienna · `#2E529A` cobalt · `#3D3B37` charcoal.

Profile: **saturation 0.10–0.81 (mean 0.49), value 0.13–0.79 (mean 0.49)**. These are aged
printing inks — never a pure hue, never bright, never pale. Pick any hue; land it mid-sat and
mid-to-dark value. A clean `#FF0000` or a pastel breaks the set instantly.

Grounds vary **per card** while everything else holds. That is what makes a series read as a
series rather than nine unrelated posters.

## The signature device: the die-cut keyline

Every cut-out — photographic or vector — is ringed in a thick cream outline, as though
scissored from a sticker sheet. Get this wrong and the style collapses into generic collage.

**Vector elements** — stroke plus `paint-order`, so the stroke sits behind the fill:

```html
<g paint-order="stroke" stroke="#EFE9D6" stroke-width="13" stroke-linejoin="round">
  <path fill="#211F1B" d="…"/>
</g>
```

**Raster cut-outs** — dilate the alpha into a keyline and composite the art over it:

```bash
convert in.png -bordercolor none -border 30 p.png                 # room for the keyline
convert p.png -alpha extract -morphology Dilate Disk:13 \
        -blur 0x0.6 -level 40%,60% m.png                          # dilated, slightly softened
convert -size $(identify -format %wx%h p.png) xc:'#EFE9D6' \
        m.png -alpha off -compose CopyOpacity -composite s.png     # the keyline shape
convert s.png p.png -compose over -composite PNG32:out.png
```

Keyline 12–14px at 1080px width. Add a short drop shadow so stickers lift off the ground:
`drop-shadow(0 10px 16px rgba(0,0,0,.45))`.

## Choosing the right treatment for a source

This cost two rebuilds, so it is the most useful note here:

- **Continuous-tone photographs** (faces, brains, machinery) → **halftone**. See the recipe in
  `style-paper-collage.md`. This is what the reference uses throughout.
- **Line art — maps, engravings, diagrams** → **threshold, never halftone**. Line art has no
  midtones, so a dot screen renders it as sparse specks and the subject vanishes.

```bash
convert map.jpg -colorspace Gray -normalize -blur 0x0.6 -threshold 58% -negate out.png
```

The small blur before thresholding stops fine engraving lines breaking into noise. Negating
gives white detail on a black plate, which reads boldly against a dark ground.

## Sunburst

Tapered rays from behind the subject. **Low contrast is the whole point** — they organise the
composition, they do not decorate it.

- 26–30 rays, half-angle ~0.021 rad, origin at the subject's centre.
- Radius about 0.55 × frame height. Full-frame rays become a pinwheel and fight the subject.
- Alternating opacity `0.085 / 0.045` in the keyline cream. Above ~0.15 they take over.

## Typography

| Role | Face | Size @1080w |
|---|---|---|
| Headline | heavy grotesque, uppercase, usually interrogative | 72–84px |
| Subtitle | **serif**, lowercase, on the banner | 36–38px |
| Tag chips | bold sans, uppercase, +0.1em | 27px |
| Bottom caption | serif, cream at ~86% | 29px |

The reference's headlines are a question series — *WHO STEALS YOUR DATA? WHO CODES THE BIAS?*
A fixed interrogative stem is doing real work: it makes nine posters one campaign. Steal the
device, not the stem.

**The banner must contain the subtitle.** A two-line headline pushes it onto the ground where
dark serif text on a dark ground is unreadable. Size the torn rect to both lines together.

## Layout

- Banner top, inset ~60px, rotated −1°.
- Subject centred around 55% height, overlapping cut-outs flanking it.
- Tag chips in the lower third, one gold, one cream, rotated ±2.6°.
- Bottom caption centred, ~62px from the foot.
- Tape at four corners; two may sit on the left/right edges rotated ~85–95°.
- Vignette: `radial-gradient(…, transparent 52%, rgba(0,0,0,.42) 100%)` — the ground darkens
  at the edges like an old print.

## Motion language

Inherits the paper physics in `style-paper-collage.md` — stepped frame rate, drops not fades,
tape before card, no dissolves. Additional to this preset:

- **Rays rotate almost imperceptibly**, ~1.5°/s, or pulse opacity on a slow sine. Any faster
  and it becomes a hypnosis wheel.
- **Stickers land one at a time** with a small rotation settle, keyline and shadow arriving
  together, 70–90ms apart.
- **The gold tag is last in and gets the only overshoot** — it is the punchline.
- Halftone and threshold plates can **register-shift** by a pixel on alternate frames, like
  misaligned printing.

## Prohibited

A cut-out without a keyline · a pure or pastel ground · gold used as a fill rather than a tag ·
full-frame high-contrast rays · halftoning line art · a white mount behind everything (that is
preset A) · sans-serif subtitles (that is preset A).

## Worked example

`examples/photomontage-poster.html` renders a complete poster in this preset: teal ground,
sunburst, thresholded map plate with a raster keyline, keylined vector figures, gold tag,
rosette, bottom caption, tape and grain.
