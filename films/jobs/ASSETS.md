# Asset register — films/jobs

Licence classes per `.claude/skills/vox-documentary-editor/references/copyright-and-attribution.md`.
**Every row verified at the holding institution, not on the aggregator's word.**

movingimagearchive.com states its material is "drawn from public-domain collections and is free
to reuse" but **names no licence and gives no per-item provenance**. That is weaker than the
standard applied to every other film in this repo, so it is used as a **shot-selection index
only** — its slug + in/out timecodes — and each film's rights are confirmed on archive.org,
where the holding collection publishes an explicit per-item licence.

## Class A — public domain, verified at source

| Source slug | Film | Year | archive.org item | Licence (as published) | Native res |
|---|---|---|---|---|---|
| `master-hands` | Master Hands | 1936 | `MasterHa1936_2` | CC Public Domain dedication (`creativecommons.org/licenses/publicdomain/`), collection `prelinger` | 1920×1080 |
| `learning-to-set-type` | Learning to Set Type | 1959 | `Learning1959` | CC Public Domain dedication, collection `prelinger` | 320×240 |
| `how-to-be-well-groomed` | How to Be Well Groomed | 1949 | `HowtoBeW1949` | CC Public Domain dedication, collection `prelinger` | 640×480 |
| `sf-general-strike-i/ii` | [San Francisco General Strike] | 1934 | `SanFranc1934`, `SanFranc1934_2` | CC Public Domain dedication, collection `prelinger` | 320×240 |
| `california-cotton-mills` | [California Cotton Mills] | 1924 | `Californ1924` | CC Public Domain dedication, collection `prelinger` | 320×240 |
| `16mm-projector-care` | The 16mm Motion Picture Projector: Care and Maintenance | 1961 | `16mmMoti1961` | CC Public Domain dedication, collection `prelinger` | 640×480 |
| `trip-down-market-street` | [A Trip Down Market Street Before the Fire] | 1906 | `ATripDownMarketStreet_HD` | CC0 1.0, collections `prelinger`, `sanfranciscobayareahistoricalimages` | 640×480 |

**Note on duplicate uploads:** the same titles also exist on archive.org under *restrictive*
licences from other uploaders — e.g. the 16mm projector film is CC BY-NC-ND 4.0 in the
`PeriscopeFilm` collection. The licence attaches to the **item**, not the title. Only the
Prelinger items above are relied on, and only those identifiers may be cited.

## Pending verification — not yet cleared for use

| Source slug | Film | Why pending |
|---|---|---|
| `verkade-fabrieken-te-zaandam` | Verkade's fabrieken te Zaandam (1930) | Not on archive.org. Almost certainly Eye Filmmuseum via Open Images (openbeelden.nl), typically **CC BY-SA with mandatory attribution** — a different licence class with obligations. Must be confirmed before use. |
| `oud-amsterdam` | Oud-Amsterdam (1923) | Same. A CC0 copy of a *differently titled* cut exists (`59464_1411107072_s01_Schilderachtig_Oud_Amster`) but has not been confirmed as the same material. |
| `indisch-allerlei` | Indisch allerlei (1920) | Same. Also colonial-era Dutch East Indies footage — needs an editorial decision, not only a licence one. Not used in the current cut. |
| `carolls-beauty-salon` | [Caroll's Beauty Salon, Hamtramck] (1941) | Prelinger-styled but not yet resolved to an identifier. |
| `twin-peaks-tunnel`, `redwood-lumber-mills`, `northwestern-pacific-rail-i`, `traveler-meets-air-traffic-control`, `space-navigation`, `five-artists`, `evolution-of-the-oil-industry`, `chevrolet-leader-news`, `spot-news`, `wonderful-world-of-wash-n-wear` | various | Resolvable the same way; not yet done. |

**The two 1080-native sources in Chapters 2 and 5 are both in the pending list.** If they do not
clear, the film loses two of its three full-bleed moments and `master-hands` has to carry them
alone — a real change to the look, flagged now rather than discovered at render.

## Measured resolution ceiling

| Tier | Sources | Treatment |
|---|---|---|
| 1920×1080 | `master-hands` only | full-bleed |
| 1440×1080 | `verkade`, `oud-amsterdam`, `indisch-allerlei` (all pending) | full-bleed |
| 640×480 | 8 sources | framed card ≤1024×768 (1.6× upscale) |
| 320×240 | the remaining ~168 sources | framed card ≤640×480 (2×) or grid tile |

The site's newer `/api/clips/<uuid>/download` endpoint and all `v4-conditional-luna-1` paths
serve **320×240 proxies**. Only the older slug-style R2 paths carry higher resolution. Measured
with `ffprobe` over HTTP across 19 sources; no source in the catalogue exceeds 1920×1080.
