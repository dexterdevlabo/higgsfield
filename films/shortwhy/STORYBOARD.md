# Storyboard — THE SHORT WHY (as cut)

15.000s · 450 frames · 30fps · 1080×1920. Four hard cuts, one graphic payoff, one shape mask.

| Beat | Window | Visual | Motion | Text | Sound |
|---|---|---|---|---|---|
| **1 Hook** | 0.00–1.95 | Mercator world map, Greenland ignites amber | camera 1.06→1.00 over 2.0s; "Every map" present on **frame 0**; lines 2–3 at 0.07/0.14; Greenland opacity at 1.05 | Every map / you've seen / **is lying to you.** | sub + swell at 0.00; three ticks on the lines |
| **2 Payoff** | 1.95–4.40 | Africa lifts to secondary grey; Greenland shrinks and flies into it | `#mapgl` scale→**0.2564**, translate **(470.4, 946.6)** over 1.10s `power3.inOut` — all three values measured by `src/make_map.py`, not eyeballed | Greenland looks as big as Africa. · **14×** smaller. | descending whoosh under the travel; sub impact as 14× lands |
| **3 Economics** | 4.40–6.45 | Five-bar cost stack builds, one bar accented | bars stagger 55ms from 4.46, `power4.out`; baseline rule draws 4.42 | ECONOMICS · Why your coffee costs what it does. | whoosh 4.26; five paper hits |
| **4 Psychology** | 6.40–8.45 | A name sets in mono, then decays letter by letter in scrambled order | glyphs in at 30ms stagger from 6.48; decay from 7.36 in order 3,6,1,7,0,4,2,5 so it reads as forgetting, not a wipe | PSYCHOLOGY · Why you forget a name the second you hear it. | 8 rising ticks in, 8 falling ticks out |
| **5 History** | 8.40–10.70 | Hine's Addie Card, 1910; slow push; accent ring | camera 1.00→1.055 over 2.3s; ring 8.96 scale 1.9→1 | HISTORY · How these photographs changed the law. · full credit line | whoosh 8.26; sub 8.52; tick on the ring |
| **6 Promise** | 10.65–12.84 | Circular mask opens over the photograph | mask 0→4600px in 0.62s; "One idea." already opaque **inside** the mask so it is revealed, not faded in | One idea. / Ninety seconds. / **Every week.** | whoosh 10.49; sub as the mask opens |
| **7 CTA** | 12.66–15.00 | Wordmark, accent rule, handle, follow chip | wordmark 12.66, rule 12.98, handle 13.20, chip 13.48 `back.out(1.6)` | THE SHORT WHY · @theshortwhy · FOLLOW | sub on the wordmark; tick on the chip |

**Continuity.** Four progress ticks at the foot of the safe area light amber as each topic
opens, then fade with the mask. Grain and vignette are global, applied once.

**Safe areas.** Nothing essential enters the top 230px or bottom 420px — Instagram's UI sits there.

**Fixed during QC** (found by `src/qc_luma.py`, not by eye):
- Frame 0 had no type: a `fromTo` from opacity 0 is still 0 at t=0, so the first frame of the
  most important second in the film was bare map. The first line is now simply present.
- 10.87–10.97 was a blank dark frame — the mask had covered the screen before the promise text
  arrived. The text is now opaque inside the mask.
- 12.77–12.83 was a gap between the promise leaving and the wordmark arriving. Overlapped.
- Beats 3 and 4 opened nearly empty; their content now lands on the cut.
