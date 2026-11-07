#!/usr/bin/env bash
# "Why the Earth is not flat" — fetch -> assets -> audio -> render -> verify.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD; HF=build/hf; PROJ=$HF/show
GLEASON='https://upload.wikimedia.org/wikipedia/commons/3/30/Gleason%27s_new_standard_map_of_the_world_-_on_the_projection_of_J._S._Christopher%2C_Modern_College%2C_Blackheath%2C_England%3B_scientifically_and_practically_correct%3B_as_%22it_is.%22_%2810143175716%29.jpg'

mkdir -p assets/raw assets/prepared assets/audio out "$PROJ/assets/fonts"
[ -f assets/raw/gleason_flatmap.jpg ] || curl -sS --max-time 180 -A 'documentary-research/1.0' -o assets/raw/gleason_flatmap.jpg "$GLEASON"
convert assets/raw/gleason_flatmap.jpg -modulate 100,92 -brightness-contrast 2x6 PNG24:assets/prepared/gleason.png

python3 -I src/audio.py
ffmpeg -v error -y -i assets/audio/mix.wav \
  -af "volume=13dB,alimiter=limit=0.72:level=disabled:attack=1:release=90" \
  -ar 48000 -c:a pcm_s16le assets/audio/mix_norm.wav

cp src/index.html "$PROJ/index.html"
cp assets/prepared/gleason.png "$PROJ/assets/"
cp assets/audio/mix_norm.wav "$PROJ/assets/mix.wav"
cp /usr/share/fonts/opentype/inter/{Inter-Regular,Inter-SemiBold,Inter-Bold,InterDisplay-Bold}.otf \
   /usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Bold.ttf "$PROJ/assets/fonts/"
[ -d "$HF/node_modules/hyperframes" ] || (cd "$HF" && npm install --ignore-scripts --no-audit --no-fund hyperframes)
"$HF/node_modules/.bin/hyperframes" telemetry disable >/dev/null 2>&1 || true

(cd "$HF" && ./node_modules/.bin/hyperframes lint show)
(cd "$HF" && ./node_modules/.bin/hyperframes render show -o "$ROOT/out/flatearth.mp4" --fps 30 --quality delivery)

ffmpeg -v error -i out/flatearth.mp4 -f null -
python3 -I src/qc_luma.py out/flatearth.mp4
ffmpeg -nostats -i out/flatearth.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -14 | grep -E "I: |Peak:"
echo "build OK"
