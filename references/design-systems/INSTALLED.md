# Vendored design material

## `references/design-systems/` — 199 design systems

From [feimacode/open-design-agent-kit](https://github.com/feimacode/open-design-agent-kit), MIT.
Each entry is a `DESIGN.md`-style system (palette, type, spacing, component rules) that the
`design-md` and `style-tile` skills can consume.

**These describe real companies' brands** — Apple, Airbnb, Stripe, Vercel and so on. Fine as
study and as a starting point to diverge from. Cloning one wholesale for client or spec work
is a trademark problem, and it cuts against this repo's standing rule: no brand logos,
packaging or product photography in spec work.

## `references/design-systems-index/` — a link index, not content

From [VoltAgent/awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design), MIT.
Despite the description, the repo holds **no `DESIGN.md` files**: all 68 live on the external
site `getdesign.md` and are only linked. The README is kept here as a bookmark list. It is not
a skill and nothing was installed from it.

## Skills installed from open-design-agent-kit

**All 185 installable skills**, on the user's instruction after the trade-off was put to them.

Held back: 7 whose names collide with skills already active in this environment, where a
second copy shadows the first — `canvas-design` `frontend-design` `pptx` `pdf` `docx`
`slides` `artifacts-builder`. They remain in the clone if ever wanted.

## Also installed, on the user's instruction

### JimLiu/baoyu-design — 7 skills

`claude-design` `claude-design-system` `claude-slides` `claude-dashboard` `claude-motion`
`motion-director` `baoyu-dataviz` (renamed from `dataviz`, which would otherwise shadow the
built-in). `LICENSE` and `NOTICE.md` are kept inside `.claude/skills/claude-design/`.

**The licensing caveat stands and is the repo's own.** `NOTICE.md` states that much of this
material is Anthropic's — the Artifact-type SKILL.md files, reference docs, reconstructed
editors, Anthropicons fonts — that "Anthropic has published no license for" and that "this
project grants none". MIT covers only the maintainer's local tooling. It was raised before
installing and the user chose to proceed; recorded here so the decision is not lost.

`motion-director` + `claude-motion` are the pair worth knowing about: scripted, narrated
motion films with scene timing driven by the voice track.

### OpenCoworkAI/open-codesign — vendored, not runnable here

At `vendor/open-codesign/` (gitignored, so it does not survive the container). A pnpm
monorepo with a root `postinstall` hook — an app to run, not a skill to read, and
`npm install` with scripts is blocked in this container. See its `INSTALL-NOTES.md`.
