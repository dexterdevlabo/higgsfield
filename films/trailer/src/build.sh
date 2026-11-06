#!/usr/bin/env bash
# Deterministic end-to-end build: sources -> prepared assets -> audio -> render.
# Requires: node 22+, ffmpeg, ImageMagick, python3 with numpy + Pillow.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD; HF=build/hf; PROJ=$HF/kites

python3 -I src/fetch_sources.py
bash src/prepare_assets.sh

# audio: synthesise, then master to the delivery level (see QC.md for measured values)
mkdir -p assets/audio
python3 -I src/audio.py
ffmpeg -v error -y -i assets/audio/mix.wav \
  -af "volume=10dB,alimiter=limit=0.74:level=disabled:attack=1:release=80" \
  -ar 48000 -c:a pcm_s16le assets/audio/mix_norm.wav

# assemble the HyperFrames project (kept under build/, which the repo gitignores)
mkdir -p "$PROJ/assets/fonts"
cp src/index.html "$PROJ/index.html"
for f in har_plate har_L_kite har_L_willow har_L_group perk_plate perk_ground \
         card_hokusai card_dyson card_plummer card_broadst; do
  cp "assets/prepared/$f.png" "$PROJ/assets/$f.png"
done
# downscale to render size — full-canvas layers are ~15 MB each and choke the browser
for L in kite willow group; do convert "$PROJ/assets/har_L_$L.png" -resize 1200x1600 -strip "PNG32:$PROJ/assets/har_L_$L.png"; done
convert "$PROJ/assets/perk_plate.png"  -resize 1008x1350 -strip "PNG24:$PROJ/assets/perk_plate.png"
convert "$PROJ/assets/perk_ground.png" -resize 1008x324  -strip "PNG32:$PROJ/assets/perk_ground.png"
for c in hokusai dyson plummer broadst; do convert "$PROJ/assets/card_$c.png" -resize 480x600 -strip "PNG24:$PROJ/assets/card_$c.png"; done
cp assets/audio/mix_norm.wav "$PROJ/assets/mix.wav"
cp /usr/share/fonts/opentype/inter/{Inter-Regular,Inter-SemiBold,Inter-Bold,InterDisplay-Bold}.otf \
   /usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Bold.ttf "$PROJ/assets/fonts/"

[ -d "$HF/node_modules/hyperframes" ] || (cd "$HF" && npm install --ignore-scripts --no-audit --no-fund hyperframes)
"$HF/node_modules/.bin/hyperframes" telemetry disable || true
"$HF/node_modules/.bin/hyperframes" lint   kites --help >/dev/null 2>&1 || true
(cd "$HF" && ./node_modules/.bin/hyperframes lint kites)
(cd "$HF" && ./node_modules/.bin/hyperframes render kites \
    -o "$ROOT/out/trailer_1080p.mp4" --fps 30 --quality delivery)

# verification gate
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 out/trailer_1080p.mp4
ffmpeg -v error -i out/trailer_1080p.mp4 -f null -
ffmpeg -nostats -i out/trailer_1080p.mp4 -vf blackdetect=d=0.1:pic_th=0.97 -f null - 2>&1 | grep blackdetect && echo "FAIL: black frames" && exit 1
echo "build OK"
