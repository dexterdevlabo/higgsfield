#!/usr/bin/env bash
# Danette concept film — audio -> assemble -> render -> verify. No external assets to fetch.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD; HF=build/hf; PROJ=$HF/show
mkdir -p assets/audio out "$PROJ/assets/fonts"
python3 -I src/audio.py
ffmpeg -v error -y -i assets/audio/mix.wav \
  -af "volume=11dB,alimiter=limit=0.74:level=disabled:attack=2:release=110" \
  -ar 48000 -c:a pcm_s16le assets/audio/mix_norm.wav
cp src/index.html "$PROJ/index.html"
cp assets/fonts/*.ttf "$PROJ/assets/fonts/"
cp assets/audio/mix_norm.wav "$PROJ/assets/mix.wav"
[ -d "$HF/node_modules/hyperframes" ] || (cd "$HF" && npm install --ignore-scripts --no-audit --no-fund hyperframes)
"$HF/node_modules/.bin/hyperframes" telemetry disable >/dev/null 2>&1 || true
(cd "$HF" && ./node_modules/.bin/hyperframes lint show)
(cd "$HF" && ./node_modules/.bin/hyperframes render show -o "$ROOT/out/danette_concept.mp4" --fps 30 --quality delivery)
ffmpeg -v error -i out/danette_concept.mp4 -f null -
python3 -I src/qc_luma.py out/danette_concept.mp4
ffmpeg -nostats -i out/danette_concept.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -14 | grep -E "I: |Peak:"
echo "build OK"
