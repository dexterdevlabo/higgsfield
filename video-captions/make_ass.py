import sys

SRC, OUT = sys.argv[1], sys.argv[2]
Y = int(sys.argv[3]) if len(sys.argv) > 3 else 1000   # vertical anchor (1080x1920 canvas)
END = float(sys.argv[4]) if len(sys.argv) > 4 else 111.4
X = 540

rows = []
for line in open(SRC, encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    t, st, txt = [p.strip() for p in line.split("|", 2)]
    rows.append((float(t), st, txt))

def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

POP = r"\fscx82\fscy82\t(0,110,\fscx100\fscy100)\fad(50,40)"
STY = {
    "n": (r"\fnInter\b1\fs64", "&HFFFFFF&"),
    "c": (r"\fnInter\b1\fs66", "&HFFFFFF&"),
    "b": (r"\fnInter\b1\fs128", "&HFFFFFF&"),
    "g": (r"\fnInter\b1\fs128", "&H7CCDF4&"),
    "s": (r"\fnInstrument Serif\i1\b0\fs116", "&HFFFFFF&"),
}
SMALL = r"\fnInter\b1\fs56"

def emit(ev, layer_tags, x, y, text, start, end, color, move=None):
    pos = rf"\move({move[0]},{move[1]},{x},{y},0,110)" if move else rf"\pos({x},{y})"
    shadow = rf"{{\an5{pos}{layer_tags}{POP}\1c&H000000&\1a&H40&\bord0\shad0\blur12}}"
    fill = rf"{{\an5{pos}{layer_tags}{POP}\1c{color}\bord0\shad0}}"
    ev.append(f"Dialogue: 0,{ts(start)},{ts(end)},Cap,,0,0,0,,{shadow}{text}")
    ev.append(f"Dialogue: 1,{ts(start)},{ts(end)},Cap,,0,0,0,,{fill}{text}")

events = []
for i, (t, st, txt) in enumerate(rows):
    nxt = rows[i + 1][0] if i + 1 < len(rows) else END
    end = min(nxt, t + 2.2)
    tags, color = STY[st]
    if st in "bg" and i > 0 and rows[i - 1][1] == "n" and t - rows[i - 1][0] < 1.2:
        # stack: previous small chunk slides up, big word lands under it
        prev = rows[i - 1][2]
        emit(events, SMALL, X, Y - 74, prev, t, end, "&HFFFFFF&", move=(X, Y))
        emit(events, tags, X, Y + 14, txt, t, end, color)
    else:
        emit(events, tags, X, Y, txt, t, end, color)

head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,-1,0,1,0,0,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
open(OUT, "w", encoding="utf-8").write(head + "\n".join(events) + "\n")
print(len(rows), "chunks ->", OUT)
