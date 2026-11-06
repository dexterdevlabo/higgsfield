# Storyboard — The Art of Kite Flying (as cut)

10.000 s · 300 frames · 30 fps · 1920×1080. Four shots, three hard cuts, one shape-mask reveal.
Timings are the values in `src/index.html`; this document and the composition agree.

| Shot | Window | Visual | Layers | Motion | Transition out | On-screen text | Sound |
|---|---|---|---|---|---|---|---|
| **S1** | 0.00–2.70 | Harunobu 1766 cut into depth layers over a reconstructed paper plate; accent ring drawn on the kite | plate · figure-group · willow · kite · ring | camera 1.00→1.055 `power1.inOut`; parallax by depth — kite −26px, willow −54px, group −96px; headline words at 0.22/0.28/0.34, 24px rise, `power4.out`; ring 0.92 | hard cut | FIVE / CENTURIES / **OF KITES** · Harunobu caption + CC0 credit | sub impact + swell 0.00; three ticks on the word stagger; swell on the ring |
| **S2** | 2.60–5.30 | Perkins 1910 photograph right, type block left; ring on the suspended man, leader line, accent chip | plate · ground band · ring · leader · chip | camera 1.00→1.05; ground band +22px parallax; 1910 at 2.78; ring 3.46 (scale 2.2→1), leader 3.74, chip 3.92 | hard cut | **1910** / Harvard Aviation Field · "One man. Five kites." · LoC credit | whoosh 2.44 (leads the cut); sub impact on 1910; ticks on ring / leader / chip |
| **S3** | 5.20–8.15 | Four archival cards, alternating heights, with cast shadows; dated; a rule draws under them | 4 cards · 4 date slugs · rule · label | cards stagger 85ms from 5.21, alternating ±40px, scale .94→1; dates +220ms behind each card; rule 5.84; camera 1.00→1.035 | **shape mask** | ca. 1830–33 · 1787 · ca. 1917 · 1910 · "One gesture · four media · four archives" | whoosh 5.04; four paper movements; four ticks; swell on the rule |
| **S4** | 7.45–10.00 | Circular mask opens over the collage onto the title card | mask · title · rule · invocation · credits | mask 0→5200px over 0.62s `power4.out`; title already opaque inside the mask so it is *revealed*, not faded; rule 7.92, invocation 8.14, credits 8.44 | — | VOX DOCUMENTARY EDITOR · /vox-documentary-editor · source credits | whoosh 7.29; sub impact 7.45; tick 8.06; tail swell |

**Continuity.** The corner slug ("THE ART OF KITE FLYING" + shot number 01/02/03) persists from
0.00 and fades at 7.45. Grain and vignette are global, applied once over everything.

**Why these transitions.** Three hard cuts, because each shot asserts a new fact rather than a
relationship. The one mask reveal is earned: it is the move from the subject to the tool that
made the film, so the collage is literally opened to show the title underneath.

**Changed during the cut** (recorded because the first pass was wrong):
- S1 was reframed so the kite — at the very top of the portrait sheet — stays in shot.
- S2's photograph moved right by 304px after the headline landed on bright sky.
- Scene-level opacity fades were removed in favour of z-order; they were leaving black frames.
- The title was moved inside the mask after `blackdetect` found a 0.4s black hole at 7.5.
