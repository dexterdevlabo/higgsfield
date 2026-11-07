# Upstream

Source: `hyperframes` npm package v0.9.19 — https://github.com/heygen-com/hyperframes
Licence: **Apache-2.0** (declared in the package manifest; the npm dist ships no LICENSE file).

Installed by copying `dist/skills/hyperframes-cli` out of the installed package, which is what
`npx hyperframes skills update` writes. The CLI installer was not run: this session's
permission classifier blocks external code execution.

These three skills (`hyperframes`, `hyperframes-cli`, `media-use`) are a set and
cross-reference each other — `hyperframes-cli` and `media-use` cite files that live in
`hyperframes/references/`. Install or remove them together.
