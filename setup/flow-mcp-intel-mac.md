# flow-mcp on a 16GB Intel i7 Mac

Driving Google Flow (Veo) from Claude. **This runs on your Mac, not in a cloud session** — the
tool launches a real Chrome window and clicks Flow's interface through the DevTools Protocol.

## Why Intel is fine here

flow-mcp does **no local inference**. Google's servers generate the video; your machine only
drives a browser. So the Apple Silicon requirement that rules out every local video model
(LTX, Wan, HunyuanVideo — all MLX, all Apple-Silicon-only) simply does not apply. An i7 with
16GB is adequate.

What your machine does need: Node 22+, Chrome, a Google account, and **a screen that stays
on**. It cannot run headless or while the Mac sleeps.

## Before you start

- **Free Google account** = ~50 Flow credits/day. A paid Google AI plan adds more and unlocks
  1080p downloads.
- You sign in **by hand, once**, in a dedicated Chrome window. The tool never types your
  password and keeps its own Chrome profile, separate from your everyday browser. Nobody —
  including me — needs your credentials.
- The project's own README warns it automates Flow's web interface, may break when Google
  changes that interface, and **may conflict with Google's terms of service**. It names no
  software licence. Your account, your call.

## 1. Prerequisites

Check what you have:

```bash
node --version && which -a google-chrome 2>/dev/null; ls -d "/Applications/Google Chrome.app" 2>/dev/null
```

If Node is missing or below 22, install it. On an **Intel** Mac, Homebrew lives in
`/usr/local`, not `/opt/homebrew`:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
brew install node@22 ffmpeg && brew link --overwrite --force node@22
```

`ffmpeg` is optional but worth having — flow-mcp uses it to join clips, mix music and record
narration. (You already have ffmpeg habits from this repo.)

Google Chrome, if absent: https://www.google.com/chrome/ — the Intel build is served
automatically.

## 2. Where to put it

**Not** in `Desktop`, `Documents` or `Downloads`. macOS guards those folders with TCC
permission prompts, which breaks an automated Chrome profile. Use a plain directory:

```bash
mkdir -p ~/dev && cd ~/dev
```

## 3. Install

```bash
git clone https://github.com/GTAI-1/flow-mcp.git
```

```bash
cd ~/dev/flow-mcp && npm install && npm run build
```

```bash
npm run login
```

That last command opens the dedicated Chrome window. Sign into Google there by hand. The
session is stored in the tool's own profile and reused from then on.

## 4. Register it with Claude Code

```bash
claude mcp add --scope user flow -- node ~/dev/flow-mcp/dist/index.js
```

Use the **absolute** path — `claude mcp add` does not expand `~` reliably in every shell.
If in doubt:

```bash
cd ~/dev/flow-mcp && claude mcp add --scope user flow -- node "$PWD/dist/index.js"
```

Optional control panel, for watching runs and saving a Gemini key:

```bash
cd ~/dev/flow-mcp && npm run studio    # then open http://127.0.0.1:8787
```

Optional, only for Google's narration voices — a free Google AI Studio key:

```bash
export GEMINI_API_KEY=...   # or save it in the control panel
```

## 5. Keep the screen awake

The Chrome window is driven live, so the display must not sleep mid-render:

```bash
caffeinate -d
```

Leave that running in a terminal tab while you generate, or set
System Settings → Lock Screen → *Turn display off* to Never for the session.

Also: the tool clicks a real UI, so **don't steal focus from that Chrome window** while a run
is in progress.

## Fitting it to this repo

Generated footage is a different asset class from everything in `films/` so far — it is
neither verified public-domain archival nor original code-drawn graphics. If you bring Flow
clips into a film:

- add a class for them in that film's `ASSETS.md` (the register currently only has A–E
  licence classes for sourced material);
- **label synthetic footage on screen**, per the accuracy rules in
  `.claude/skills/vox-documentary-editor/references/copyright-and-attribution.md`;
- composite it through the normal pipeline — drop the clip into the HyperFrames composition as
  a `<video class="clip" data-start=… data-duration=…>` and let the existing grade and grain
  pass unify it with the drawn elements.

And the honest framing from the rest of this work: for maps, charts, kinetic type and
diagrams, code-drawn is sharper and editable, and exact where it needs to be. Generated video
earns its place for atmosphere and b-roll you cannot source or draw.

## If it breaks

- **Chrome won't launch / profile errors** → the folder is probably under `Desktop`,
  `Documents` or `Downloads`. Move it to `~/dev` and re-run `npm run build`.
- **Login doesn't stick** → the profile was reset; re-run `npm run login`.
- **Flow's UI changed** → this is the standing risk the author flags; check the repo's issues.
- **Claude can't see the tools** → confirm with `claude mcp list`, and that the path in the
  registration is absolute and points at `dist/index.js` (not `src/`).
