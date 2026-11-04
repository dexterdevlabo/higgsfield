"""Measure colour stats of the talking-head footage and each b-roll clip; print per-clip lutrgb
grade (per-channel mean/std transfer, 70% strength) as JSON for render.py."""
import json, subprocess, sys, numpy as np, os
src, bdir = sys.argv[1], sys.argv[2]
def stats(path, ss=None, t=None):
    cmd = ["ffmpeg","-v","error"] + (["-ss",str(ss)] if ss is not None else []) + ["-i",path] + \
          (["-t",str(t)] if t else []) + ["-vf","fps=2,scale=72:128","-f","rawvideo","-pix_fmt","rgb24","-"]
    a = np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,np.uint8).reshape(-1,3).astype(float)
    return a.mean(0), a.std(0)
tm, ts = stats(src)
print("target mean", tm.round(1), "std", ts.round(1), file=sys.stderr)
out = {}
for line in open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"broll.txt")):
    line=line.strip()
    if not line or line.startswith("#"): continue
    s,e,cid,off,fx=[p.strip() for p in line.split("|")]
    cm, cs = stats(os.path.join(bdir,f"{cid}.mp4"), float(off), float(e)-float(s))
    k = 0.7
    ch = {}
    for i,c in enumerate("rgb"):
        g = (ts[i]/max(cs[i],1)); g = 1 + k*(g-1)
        m = cm[i] + k*(tm[i]-cm[i])
        ch[c] = f"clip((val-{cm[i]:.1f})*{g:.3f}+{m:.1f},0,255)"
    out[cid] = "lutrgb=r='%s':g='%s':b='%s'" % (ch["r"],ch["g"],ch["b"])
    print(cid, "mean", cm.round(1), "->", file=sys.stderr)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"grade.json"),"w"), indent=1)
