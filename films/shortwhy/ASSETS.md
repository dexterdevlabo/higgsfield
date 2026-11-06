# Asset register — THE SHORT WHY

Licence class: A public domain · B openly licensed · C licensed/permission · D exception, needs review · E reference-only.

| ID | Item | Creator | Date | Source + record | Class | Rights (verbatim from source) | Status | Use |
|----|------|---------|------|-----------------|-------|-------------------------------|--------|-----|
| A01 | "Addie Card, 12 years. Spinner in North Pownal Cotton Mill, Vt." | Lewis W. Hine | February 1910 | Library of Congress P&P, National Child Labor Committee collection, 2018675335 — loc.gov/item/2018675335 | A | "No known restrictions on publication. For information see: National Child Labor Committee (Lewis Hine photographs), https://hdl.loc.gov/loc.pnp/res.097.hine" | APPROVED | Beat 5, full shot |
| A02 | `ne_110m_admin_0_countries` country geometry | Natural Earth | 110m release | naturalearthdata.com via nvkelso/natural-earth-vector | A | Natural Earth is in the public domain; no permission needed | APPROVED | Beat 1–2 map, drawn in palette |

## Considered and not used
| Item | Reason |
|---|---|
| Colton's *Illustrated & Embellished Steel Plate Map of the World on Mercator's Projection*, 1854 (LoC 2009579466, "free to use and reuse") | Greenland's interior is overprinted with printed distance tables, so a clean Greenland cutout was impossible. Rights were fine; the image was wrong for the shot. |
| Lewis Hine, Merrimack Mill street scene, 1913 (LoC 2018677667) | Too wide to read on a phone in two seconds. |

## Generated, nothing to licence
- All cartography is **drawn** from A02's coordinates by `src/make_map.py` in the project palette.
  No scanned map is reproduced.
- The cost-stack chart, the decaying-name diagram, all annotation, type and layout are original.
- All audio is synthesised in `src/audio.py` (numpy). No sourced music or sound effects.

## Fonts (rasterised into frames, not redistributed)
Inter / Inter Display and JetBrains Mono — both SIL Open Font License 1.1.

## On-screen claims and their basis
| Claim | Basis |
|---|---|
| "Greenland looks as big as Africa" | Measured on the rendered map: Greenland 185,745 px vs Africa 171,176 px = 1.09×. |
| "14× smaller" | Greenland 2,166,086 km² (Statistics Greenland) ÷ Africa ≈30,370,000 km² = 14.02. Not taken from the simplified drawing geometry, which gives 13.72. |
| "How these photographs changed the law" | Hine's NCLC photographs are documented as instrumental in US child-labour reform. Wording hedged: Keating–Owen (1916) was struck down in 1918; federal limits arrived with the Fair Labor Standards Act, 1938. |
| Beats 3 and 4 | Questions, not claims. No statistic is shown. |
