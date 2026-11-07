#!/usr/bin/env bash
# Kids short — assemble, render, verify. Assumes generated assets are already in
# assets/generated/ and the voiceover in assets/vo.wav; this script spends nothing.
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$PWD; HF=build/hf; PROJ=$HF/show

mkdir -p out "$PROJ/assets/fonts" "$PROJ/assets/generated"

# 1. sound design (synthesised, free) and VO mix if a voiceover is present
python3 -I src/audio.py
if [ -f assets/vo.wav ]; then
  ffmpeg -v error -y -i assets/mix_bed.wav -i assets/vo.wav -filter_complex \
    "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,highpass=f=90[vo];\
     [0:a][vo]sidechaincompress=threshold=0.05:ratio=9:attack=90:release=380[duck];\
     [duck][vo]amix=inputs=2:normalize=0:duration=first[m];\
     [m]volume=6dB,alimiter=limit=0.70:level=disabled:attack=2:release=100[o]" \
    -map "[o]" -ar 48000 -c:a pcm_s16le assets/mix.wav
else
  # quieter master than adult short-form: children often use headphones
  ffmpeg -v error -y -i assets/mix_bed.wav \
    -af "volume=9dB,alimiter=limit=0.70:level=disabled:attack=2:release=100" \
    -ar 48000 -c:a pcm_s16le assets/mix.wav
fi

# 2. assemble, with the safe-area guides off for delivery
sed 's/data-guides="on"/data-guides="off"/' src/index.html > "$PROJ/index.html"
cp assets/generated/*.png "$PROJ/assets/generated/" 2>/dev/null || true
cp assets/mix.wav "$PROJ/assets/mix.wav"
cp assets/fonts/*.ttf "$PROJ/assets/fonts/"

# 3. render
(cd "$HF" && ./node_modules/.bin/hyperframes lint show)
(cd "$HF" && ./node_modules/.bin/hyperframes render show \
    -o "$ROOT/out/short.mp4" --fps 30 --quality delivery)

# 4. verify
ffmpeg -v error -i out/short.mp4 -f null -
python3 -I src/qc_luma.py out/short.mp4
ffmpeg -nostats -i out/short.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -14 | grep -E "I: |Peak:"
echo "target for kids: around -18 LUFS, true peak <= -1.5 dBTP"

# 5. a guides-on reference frame, for checking safe areas against a real phone
sed 's/data-guides="off"/data-guides="on"/' "$PROJ/index.html" > "$PROJ/_guides.html"
echo "build OK — out/short.mp4"
