#!/usr/bin/env bash
# Asset preparation: cutouts, depth layers, grades and collage cards.
# Recipes follow ART_DIRECTION.md. Originals in assets/raw/ are never edited in place.
set -euo pipefail
cd "$(dirname "$0")/.."
RAW=assets/raw; PREP=assets/prepared; mkdir -p "$PREP"

WG="-modulate 100,96 -brightness-contrast 0x6"                                   # woodblock
PG="-colorspace Gray -level 3%,97% +level-colors '#16120C','#D8C3A0'"            # photographic

# ---- Harunobu: trim the sheet edge, flood-cut the paper, split into depth layers ----
convert "$RAW/met54541_harunobu_kiteflying.jpg" -gravity center -crop 95%x96%+0+0 +repage "$PREP/har_sheet.png"
W=$(identify -format %w "$PREP/har_sheet.png"); H=$(identify -format %h "$PREP/har_sheet.png")
# fuzz 11% is the working tolerance: 8% leaves the sky, 14% eats the light robes.
convert "$PREP/har_sheet.png" -alpha set -channel RGBA -fuzz 11% \
  -fill none -draw "matte 8,8 floodfill"             -fill none -draw "matte $((W-8)),8 floodfill" \
  -fill none -draw "matte 8,$((H-8)) floodfill"      -fill none -draw "matte $((W-8)),$((H-8)) floodfill" \
  +channel -channel A -blur 0x0.6 -level 25%,75% +channel "$PREP/har_cut.png"

mkrect () { convert -size "${W}x${H}" xc:black -fill white -draw "rectangle $1,$2 $(($1+$3)),$(($2+$4))" "$5"; }
mkrect 380 0  720 600 /tmp/m_kite.png          # distant kite
mkrect 980 0 1748 430 /tmp/m_willow.png        # willow, above the figures' heads
convert /tmp/m_kite.png /tmp/m_willow.png -compose Lighten -composite /tmp/m_top.png
convert /tmp/m_top.png -negate /tmp/m_group.png   # everything else: figures, water, lower willow

convert "$PREP/har_cut.png" -alpha extract /tmp/oa.png
for L in kite willow group; do
  convert /tmp/oa.png "/tmp/m_$L.png" -compose Multiply -composite /tmp/na.png
  eval convert "$PREP/har_cut.png" -alpha off $WG /tmp/na.png -alpha off \
       -compose CopyOpacity -composite "PNG32:$PREP/har_L_$L.png"
done
eval convert "$PREP/har_sheet.png" -blur 0x90 $WG -resize 1920x1080^ -gravity center -extent 1920x1080 "$PREP/har_plate.png"

# ---- Perkins 1910: crop the mount, grade, separate a ground band for parallax ----
convert "$RAW/loc2001705764_perkins_manlift.jpg" -crop 672x900+62+34 +repage "$PREP/perk_photo.png"
eval convert "$PREP/perk_photo.png" $PG -resize 1344x1800 "PNG24:$PREP/perk_plate.png"
convert "$PREP/perk_photo.png" -crop 672x216+0+684 +repage /tmp/gb.png
eval convert /tmp/gb.png $PG "PNG24:/tmp/gbg.png"
convert -size 672x216 xc:white -fill black -draw "rectangle 0,0 672,26" -blur 0x14 /tmp/gmask.png
convert /tmp/gbg.png /tmp/gmask.png -alpha off -compose CopyOpacity -composite -resize 1344x432 "PNG32:$PREP/perk_ground.png"

# ---- collage cards ----
card () { eval convert "$1" "$2" -resize 600x750^ -gravity "$4" -extent 600x750 "PNG24:$PREP/card_$3.png"; }
card "$RAW/loc2008660875_hokusai_asakusa.jpg"  "$WG" hokusai center
card "$RAW/met341621_downman_dyson.jpg"        "$WG" dyson   north
card "$RAW/loc2009617160_plummer_girlkite.jpg" "$WG" plummer center
card "$RAW/loc2017645646_perkins_broadst.jpg"  "$PG" broadst center
echo "prepared assets written to $PREP"
