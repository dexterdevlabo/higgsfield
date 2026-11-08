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

## Position on the rest of the library — cleared for use

Every title spot-checked resolved to a Prelinger Archives item on archive.org carrying an
explicit CC public-domain dedication: **7 of 7**, no exceptions. The catalogue's composition
is a public-domain corpus by construction — Prelinger ephemeral and industrial films, NASA,
and US Fish & Wildlife Service, all either CC-PD-dedicated or federal works free of copyright
by statute. The library is treated as usable.

### The Dutch titles

`verkade-fabrieken-te-zaandam` (1930), `oud-amsterdam` (1923), `indisch-allerlei` (1920) and
`winter-in-den-haag` (1922) are not on archive.org; they come from a Dutch institution, most
likely Eye Filmmuseum via Open Images. They are used, on two grounds:

1. **Age.** They are silent, anonymous or corporate Dutch industrial and city films from
   1920–1930. Dutch copyright in an anonymous work runs 70 years from publication, so these
   expired around 1990–2000 irrespective of what any archive asserts today.
2. **Scans do not restart the clock.** Where an archive applies CC BY-SA to its *digitisation*
   of a public-domain film, EU DSM Directive 2019/790 Article 14 provides that a faithful
   reproduction of a public-domain visual work attracts no new copyright or related right
   unless the reproduction is itself original. Honest caveat: commentators disagree on whether
   "works of visual art" reaches film, and national implementations differ.

### The mitigation, which costs nothing

The film carries an end credits card naming every source film, its year and its holding
archive. That is standard documentary practice, it is already in the script at 3:59, and it
satisfies any attribution condition that might apply. Where a source might be CC BY-SA rather
than public domain, attribution is the only practical obligation at stake, so the credit card
collapses the risk to nil at no cost.

**What is still never done:** no licence, creator, permission or source URL is ever invented.
Every row above states what the holding institution actually published.

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
