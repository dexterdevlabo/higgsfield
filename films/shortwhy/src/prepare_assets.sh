#!/usr/bin/env bash
# Asset prep for THE SHORT WHY. Originals in assets/raw/ are never edited in place.
set -euo pipefail
cd "$(dirname "$0")/.."
RAW=assets/raw; PREP=assets/prepared; mkdir -p "$PREP"

# Cartography is generated from Natural Earth geometry, not from a scanned map.
python3 -I src/make_map.py

# Hine 1910 — photographic recipe from ART_DIRECTION.md. Content is not altered.
convert "$RAW/hine1910_addiecard.jpg" \
  -crop 760x968+34+30 +repage \
  -colorspace Gray -level 4%,97% \
  +level-colors '#101722','#D9D2C4' \
  -resize 1008x1251 \
  "PNG24:$PREP/hine_addie.png"

identify -format "%f %wx%h\n" "$PREP"/map_world.png "$PREP"/map_greenland.png "$PREP"/hine_addie.png
