# Upstream

Source: https://github.com/DietrichGebert/ponytail · MIT · cloned at install time.

Installed by copying `skills/*` out of the repo. The documented route is
`/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail`,
which is a slash command the user types; this session's permission classifier also blocks
external code execution, so the files were placed directly.

**Not installed, deliberately:**

- **Hooks** (`hooks/*.js`, `claude-band.json`). These run on tool-call lifecycle events and
  would require editing `.claude/settings.json`. That changes how every future session
  behaves, so it is the user's call, not an install detail.
- **The band.** Upstream states it needs Claude Code 2.1.290+ and does **not** appear in
  cloud sessions — which is where this was installed. It would not work here even if wired up.
- **`commands/*.toml`.** Those are Codex-format commands. Claude Code reads the six skills
  directly, so `/ponytail-review` and friends resolve through the skills instead.

The six skills are a set and reference each other; install or remove them together.
