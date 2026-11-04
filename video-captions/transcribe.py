import json, sys
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[3] if len(sys.argv)>3 else "medium", device="cpu", compute_type="int8")
import wave, numpy as np
wf = wave.open(sys.argv[1]); a = np.frombuffer(wf.readframes(wf.getnframes()), np.int16).astype(np.float32)/32768
segs, info = m.transcribe(a, word_timestamps=True, vad_filter=True, beam_size=5, language="ar", initial_prompt="السلام عليكم، مرحبا بكم فحلقة جديدة. الدارجة المغربية: واحد الحاجة، كنشوفو، ديال، دابا، بزاف، السوشل ميديا، السكرول، الدوبامين، أنستغرام، إنفلوونسر.")
out = {"language": info.language, "words": [], "segments": []}
for s in segs:
    out["segments"].append({"start": s.start, "end": s.end, "text": s.text})
    for w in s.words:
        out["words"].append({"w": w.word, "s": round(w.start,3), "e": round(w.end,3), "p": round(w.probability,3)})
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(info.language, len(out["words"]))
for s in out["segments"]: print(f'{s["start"]:6.2f} {s["text"]}')
