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

31 of its 192, chosen for what this repo actually does — video, motion, diagrams, design
tokens. The full kit stays unvendored; the rest is one `cp` away.

Deliberately NOT installed, because they collide with skills already active in this
environment: `canvas-design` `frontend-design` `pptx` `pdf` `docx` `slides`
`artifacts-builder`.

## Not installed at all

| Repo | Why |
|---|---|
| [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | **Licensing.** Its own `NOTICE.md` states that much of what it ships is Anthropic's material — Artifact-type SKILL.md files, reference docs, reconstructed editors, Anthropicons fonts — that "Anthropic has published no license for" and "this project grants none". The MIT licence covers only the maintainer's own tooling. Vendoring it would commit unlicensed third-party material into this repo's history. The user's call, not a default. |
| [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | **Needs a runtime.** A 90MB pnpm monorepo (website + apps + packages) with a root `postinstall` hook, husky, and changesets. It is an application to run, not a skill to read, and `npm install` with scripts is blocked in this container. Belongs on the user's Mac. |
