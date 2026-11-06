#!/usr/bin/env bash
# THE SHORT WHY — deterministic build: sources -> assets -> audio -> render -> verify.
# Requires node 22+, ffmpeg, ImageMagick, python3 (numpy + Pillow).
#
# To add the voiceover: record to the timings in SCRIPT.md, save assets/audio/vo.wav,
# and re-run. This script mixes it under the designed track automatically.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD; HF=build/hf; PROJ=$HF/show

# ---- 1. sources -------------------------------------------------------------
mkdir -p assets/raw
[ -f assets/raw/ne_110m_countries.geojson ] || curl -sS --max-time 180 \
  -o assets/raw/ne_110m_countries.geojson \
  "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
[ -f assets/raw/hine1910_addiecard.jpg ] || curl -sS --max-time 180 \
  -o assets/raw/hine1910_addiecard.jpg \
  "https://tile.loc.gov/storage-services/service/pnp/nclc/05200/05282v.jpg"

# ---- 2. assets --------------------------------------------------------------
bash src/prepare_assets.sh

# ---- 3. audio ---------------------------------------------------------------
mkdir -p assets/audio
python3 -I src/audio.py
if [ -f assets/audio/vo.wav ]; then
  echo "voiceover found — ducking the designed track under it"
  ffmpeg -v error -y -i assets/audio/mix.wav -i assets/audio/vo.wav -filter_complex \
    "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,highpass=f=80[vo];\
     [0:a][vo]sidechaincompress=threshold=0.04:ratio=9:attack=80:release=350[duck];\
     [duck][vo]amix=inputs=2:normalize=0:duration=first[m];\
     [m]volume=8dB,alimiter=limit=0.72:level=disabled:attack=1:release=90[out]" \
    -map "[out]" -ar 48000 -c:a pcm_s16le assets/audio/mix_norm.wav
else
  ffmpeg -v error -y -i assets/audio/mix.wav \
    -af "volume=13dB,alimiter=limit=0.72:level=disabled:attack=1:release=90" \
    -ar 48000 -c:a pcm_s16le assets/audio/mix_norm.wav
fi

# ---- 4. assemble the HyperFrames project ------------------------------------
mkdir -p "$PROJ/assets/fonts"
cp src/index.html "$PROJ/index.html"
cp assets/prepared/{map_world.png,map_greenland.png,map_africa.png,hine_addie.png} "$PROJ/assets/"
cp assets/audio/mix_norm.wav "$PROJ/assets/mix.wav"
cp /usr/share/fonts/opentype/inter/{Inter-Regular,Inter-SemiBold,Inter-Bold,InterDisplay-Bold}.otf \
   /usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Bold.ttf "$PROJ/assets/fonts/"
[ -d "$HF/node_modules/hyperframes" ] || (cd "$HF" && npm install --ignore-scripts --no-audit --no-fund hyperframes)
"$HF/node_modules/.bin/hyperframes" telemetry disable >/dev/null 2>&1 || true

# ---- 5. render --------------------------------------------------------------
(cd "$HF" && ./node_modules/.bin/hyperframes lint show)
(cd "$HF" && ./node_modules/.bin/hyperframes render show \
    -o "$ROOT/out/shortwhy_reel.mp4" --fps 30 --quality delivery)

# ---- 6. verification gate ---------------------------------------------------
ffmpeg -v error -i out/shortwhy_reel.mp4 -f null -
python3 -I src/qc_luma.py out/shortwhy_reel.mp4
ffmpeg -nostats -i out/shortwhy_reel.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -14 | grep -E "I: |Peak:"
echo "build OK"
