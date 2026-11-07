# Visual Research Engine

Search for the **actual subject of the scene**, not a generic keyword. "1956 Suez Canal
blockship Port Said" finds something; "canal" finds stock photography.

## Sources

Archives and primary collections:
Public Domain Review · Wikimedia Commons · Library of Congress (Prints & Photographs, Chronicling
America) · Europeana · Internet Archive · NASA image libraries (NASA/JPL, Earth Observatory,
SVS) · NOAA · USGS · Smithsonian Open Access · national archives and national libraries ·
museum open-access collections (Rijksmuseum, Met, Getty Open Content, Yale) · university
special collections · David Rumsey Map Collection · Old Maps Online · OpenStreetMap and
Natural Earth for cartography · government statistical agencies for data · historical
newspaper archives · scientific journals and preprints for diagrams · reputable editorial
publications (for reference, usually not reuse).

Do **not** restrict research to royalty-free stock sites. They produce generic films.

## What to look for, per scene

Historical photographs · contemporary photographs · maps (period and modern) · documents,
treaties, letters, ledgers · newspaper pages · illustrations and engravings · scientific
diagrams and cross-sections · architectural plans, elevations, sections · satellite and
aerial imagery · artwork · objects and artifacts · visual metaphors when nothing literal exists.

When no authentic image exists, that is a signal to build an original graphic — not to
substitute a vaguely related photograph. A viewer shown an unrelated image learns something false.

## Research log

Every useful result goes into `ASSETS.md` immediately, with all fields filled:

```markdown
| ID | Title | URL | Creator | Source | Date | License | Status | Intended use | Crop/element | Attribution string |
|----|-------|-----|---------|--------|------|---------|--------|--------------|--------------|--------------------|
| A014 | Port Said blockships | https://… | US Navy photographer (unattributed) | NARA via Wikimedia Commons | 1956-11 | Public domain (US Gov work) | APPROVED | shot 22 plate | crop to right third; isolate near blockship | "US Navy, National Archives, public domain" |
| A015 | Canal aerial 1869 | https://… | unknown | Getty Open Content | 1869 | Open content | APPROVED | shot 9 | full frame, graded | "Getty Open Content Program" |
| A016 | Modern transit photo | https://… | named photographer | editorial publication | 2021 | All rights reserved | REFERENCE-ONLY | composition study for shot 31 original graphic | n/a | n/a |
```

Status is exactly one of: `APPROVED` · `REFERENCE-ONLY` · `PENDING-REVIEW`. Nothing enters
the timeline with status `PENDING-REVIEW`.

## Verification

An image is not usable until you can answer: what is it, where, when, who made it, and how do
you know. Check the archive's own catalogue record, not a blog's caption — misattributed
"famous" photographs are endemic online. Cross-check at least two independent records for any
image that carries a factual claim (a named person, a dated event, an identified place).

If identification is uncertain, either caption it honestly ("believed to show…") or don't use it.

## Cartographic sourcing

Build maps from data, not from screenshots of other people's maps: Natural Earth (coastlines,
borders, bathymetry), OpenStreetMap extracts, GADM, government shapefiles, historical GIS
projects. Render with QGIS if available, otherwise generate SVG directly from GeoJSON in
Python. This guarantees the map is in the project palette, is at the right projection, and is
yours. Record the projection used and the border-vintage you chose; historical borders must
match the year the narration describes.

## Technique

- Search in the language of the place and period, and in the terminology of the period.
- Search archive catalogues directly; their internal search beats a general web search.
- Follow citations in scholarly work to the original plates.
- For any statistic, find the issuing body's own publication, not a secondary chart.
- Download originals at maximum available resolution into `assets/raw/` and never edit in place.
- Capture the full catalogue record alongside the file (a sidecar `.txt` or the ASSETS row).
