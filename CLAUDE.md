# filmskill — working context

State of this repo and the decisions behind it, so a compacted or fresh session can pick up
without re-deriving anything. Written 7 Nov 2026.

## What this repo is

A **fork of the `higgsfield` ML framework** that is being used to host video-production work.
The two are unrelated and deliberately kept apart.

- `higgsfield/`, `pyproject.toml`, `docs/`, `tutorials/`, `.github/` — **the fork. Do not touch.**
  It is someone else's Apache-2.0 project (Yerzat Dulat, Anwar Omar @higgsfield.ai), a
  GPU-orchestration framework with nothing to do with video. The user explicitly chose to leave
  it alone when asked about renaming.
- `films/` — the video work (was `projects/`, renamed).
- `.claude/skills/` — one authored skill plus vendored third-party ones.
- `vendor/` — self-ignoring; clones of upstream repos, not committed, not persistent.

The local directory is `/home/user/filmskill`; `/home/user/higgsfield` is a back-compat symlink.
**The GitHub repo is still `dexterdevlabo/higgsfield`** — renaming it is the user's to do in
Settings, and they haven't.

## Open PR

[dexterdevlabo/higgsfield#1](https://github.com/dexterdevlabo/higgsfield/pull/1) — branch
`claude/kind-heisenberg-wu24rf`, **draft**, mergeable_state clean, zero check runs (the repo's
`publish.yml` / `smoketest.yml` don't trigger on these paths). It can't merge until the user
marks it ready. Keep its title/body current — it has drifted stale three times.

A safety-net check-in cycle runs via `send_later`; it re-arms silently on no change and stops
after 3 consecutive quiet checks.

## The four films

All 16:9 or 9:16, rendered with HyperFrames, each with `src/build.sh` going fetch → verified
render, and a `QC.md` with **measured** values.

| Dir | Film | Spec |
|---|---|---|
| `films/trailer` | The Art of Kite Flying | 10.000s 16:9 · −17.7 LUFS · −1.8 dBTP |
| `films/shortwhy` | THE SHORT WHY (Reels trailer) | 15.000s 9:16 · −16.1 LUFS · −1.3 dBTP |
| `films/flatearth` | Why the Earth is not flat | 10.000s 9:16 · −16.4 LUFS · −2.1 dBTP |
| `films/danette` | Danette (spec ad) | 15.000s 16:9 · −16.9 LUFS · −1.8 dBTP |

## Hard-won lessons — do not relearn these

**HyperFrames** (also now documented in its own vendored skill, which existed all along and
would have saved the trouble):
- A film's length comes from the **GSAP timeline**, not clip extents. End with a terminal hold.
- A media element **without an `id` renders silent** while still producing an AAC stream.
- Run `lint` before every render. It catches both of the above plus missing `@font-face`.
- A mask reveal must open *over* the outgoing shot with incoming content already opaque.
- A `fromTo` from opacity 0 is still 0 at t=0 — frame 0 will be empty.

**QC**: `blackdetect` is the wrong instrument for a dark palette; it flagged 4.3s of a correct
end card. `films/shortwhy/src/qc_luma.py` checks per-frame mean luma + a bright extreme instead,
and found nine real defects across the films. Copy it into every new project.

**Treatment follows the source, not the style**: photographs halftone; line art (maps,
engravings) must be blur-then-thresholded or it renders as sparse specks.

## Standing rules the user has endorsed

- Verify every archival asset **at its source institution**, never on an aggregator's word.
  Drop anything unverifiable (AIC was dropped for a Cloudflare 403; PDR's Zetetic Astronomy
  scan was dropped for "Unclear" digital-copy rights).
- State missed targets rather than rounding them away; QC.md records real numbers.
- Don't invent statistics to fill a beat — use a question instead.
- No brand logos, packaging or product photography in spec work.

## Standing tool rules

- **Always use ponytail.** Lazy-senior mode: smallest complete change, no unasked-for
  abstraction, end each reply with what was skipped and any risk. Active now.
- **Always use graphify** for questions about this codebase — **currently impossible.** Its
  skill invokes a `graphify` CLI 33 times and that CLI is not installed; `pip install
  graphifyy` has been denied twice by the permission classifier (plain install and
  `--target`, both wheel-only). Honour this rule as soon as the CLI exists; until then say so
  rather than pretending to use it.

## Environment constraints

- **The permission classifier blocks external code execution**: `npx`, `npm install` with
  scripts, `pip install`, running downloaded binaries. Declarative skills install fine by
  cloning and copying; anything with a runtime does not. A single Bash permission rule would
  unblock it — offered, not yet granted.
- Present: ffmpeg 6.1.1, ImageMagick 6 (**no SVG delegate**), Python 3.13 + PIL/numpy, Node 22,
  Playwright + Chromium (Node, not Python).
- Fonts: Inter, JetBrains Mono system-wide; a large OFL set at
  `/mnt/skills/examples/canvas-design/canvas-fonts/`.

## Known-incomplete installs

- **graphify** — skill files only; its CLI (invoked 33× by the skill) is absent, `pip install` denied.
- **REA** — `rea-agents` installed locally, but needs Ghidra/IDA/tshark and an MCP registration.
- **OmniRoute** (`cheaper-inference/OmniRoute`, MIT) — **not installed, deliberately.** It is a
  self-hosted gateway serving `localhost:20128`; `npm install -g` and running a server are both
  blocked here, and a localhost server dies with this container anyway. It belongs on the
  user's Mac. Note it is a *router*, not credits: "bring your own provider accounts".
- **flow-mcp** — not installed; cannot run in this Linux container (needs macOS/Windows, a
  visible screen, and the user's Google login). It *would* run on the user's own Mac.

## Credentials — standing rule

The user has supplied a **Higgsfield API key**. Its value is deliberately **not recorded in
this repo, in any file, or in any commit** — only the rule is.

**Do not use it without explicit, per-use approval from the user.** They granted no standing
permission; one approval does not carry to the next use. Higgsfield generations also spend
real credits (`unlim.available: false` when last checked), so quote the cost and get a yes
before any `generate_*` call regardless.

If it ever needs to be made available to tooling, route it through the environment's secret
store (`request_credential`), which injects it at the proxy and never exposes the value to
the session. Never put it in a file, an env var committed to the repo, or a chat message.

## The user's machine

**16GB Intel i7 Mac.** This matters: Intel means **no Apple Silicon, no MLX**, so local video
generation is not viable — every current Mac video tool (LTX-2.3, Phosphene, ltx-video-mac,
Rapid-MLX) is Apple-Silicon-only, and 16GB is below every model's floor regardless.

What *does* run on that machine is this repo's own pipeline — HyperFrames is headless Chrome +
ffmpeg + Node, no GPU and no weights. For AI video the realistic routes are remote: the
Higgsfield MCP (connected here, costs credits) or flow-mcp on their Mac (browser automation
against Google Flow, so Intel is fine).

## Style presets

`.claude/skills/vox-documentary-editor/references/style-paper-collage.md` and
`style-photomontage.md` — two art directions measured from reference sheets, with rendering
examples in `examples/`. Both motion languages are **specified but unproven**; nothing has been
rendered as video in either style yet.
