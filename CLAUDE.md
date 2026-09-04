---
type: Agent Guide
title: Claude Code Guidance — Ahrensburg mdBook
description: Build/deploy commands and content conventions for this repository, for Claude Code.
tags:
  - claude-code
  - mdbook
  - build
  - deploy
  - conventions
audience: Claude Code / coding agents
---

# Claude Code Guidance

Meta-docs (this file, [`AGENTS.md`](AGENTS.md), [`openwiki/`](openwiki/)) share one shape:
OKF-compatible frontmatter (`type` at minimum), named sections, a **Related pages** section.
Format rationale: OKF section in [`README.md`](README.md).

## What this is

A German-language [mdBook](https://rust-lang.github.io/mdBook/) knowledge base about the town of Ahrensburg (Schleswig-Holstein). Pure content — Markdown pages, no application code. AI-assisted, editorially reviewed, CC BY-SA 4.0, published to <https://wissen-ahrensburg.de>. [`README.md`](README.md) explains the OpenWiki approach.

## Zusammenarbeit Mensch & KI (Co-Wiki)

Mensch (Chef: Themen, Faktencheck, Freigabe) und KI (Assistent: Entwürfe, Formatierung,
Verlinkung, Korrektur) arbeiten am selben Markdown-Ordner; die KI veröffentlicht nie eigenständig.
Ablauf: Idee → RAG-Recherche → Entwurf → menschliche Prüfung → Veröffentlichung → Pflege.
Voll: [`co-wiki`-Skill](.claude/skills/co-wiki/SKILL.md). Redaktionspipeline (`redaktion-*`-Subagenten)
und Event-Driven-Delta-Updates: [`docs/agent-notes.md`](docs/agent-notes.md) §3–§4.

## Commands

- `mdbook build` — render `src/` to `book/` (gitignored). Run from the repo root.
- `mdbook serve` — live-reloading preview at <http://localhost:3000>.
- `npm run ver` — deploy: pushes `book/` to the `gh-pages` branch via `gh-pages`, with `--nojekyll` and `--cname wissen-ahrensburg.de`. Deploy is manual (no CI workflow in this repo).

Full deploy sequence: `npm install` (the `gh-pages` binary is a dev dependency and `node_modules/` is gitignored, so it's absent on a fresh checkout) → `mdbook build` → `npm run ver`.

`mdbook` is a Rust binary (`~/.cargo/bin/mdbook`), not an npm dependency. The build also needs
`mdbook-mermaid` (preprocessor for the diagram in `src/openwiki/architecture.md`). Pin it to a
version that supports mdBook 0.4.x — `cargo install mdbook-mermaid --version 0.14.0`; newer
releases target mdBook 0.5 and fail with "Unable to parse the input". Its vendored assets
`mermaid.min.js` / `mermaid-init.js` live at the repo root and are checked in.

## Structure & conventions

- **`src/SUMMARY.md` is the table of contents.** A page under `src/` is only included in the book if it is linked from `SUMMARY.md`. Adding a new page means creating `src/<slug>.md` *and* adding a link in `SUMMARY.md`.
- **`raw/` is the human draft area.** `raw/<thema>.md` (Vorlage `raw/_vorlage.md`) liegt außerhalb
  von `src/`, nicht in `SUMMARY.md`, wird nicht gebaut, kein Transparenzhinweis. `raw/<thema>.md`
  ist gitignoriert (nur `raw/README.md` + `raw/_vorlage.md` eingecheckt) — eine gelöschte Rohfassung
  ist endgültig weg. Weg: Entwurf → Faktencheck → menschliche Freigabe → neue `src/<slug>.md` +
  `SUMMARY.md`-Eintrag (dann Hinweis oben und unten). Siehe [`raw/README.md`](raw/README.md).
- **AI transparency notice.** Every content page opens and closes with the italic line:
  `*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*`
  Keep this on both ends when creating or substantially rewriting a page. (`datenschutz.md` is the one legitimate exception.)
- Internal links use relative `.md` paths (e.g. `[Geografie](geografie.md)`); mdBook rewrites them to `.html`.
- All prose is German.
- `book.toml`: `default-theme = light`, `preferred-dark-theme = navy`.
- `src/openwiki/*.md` are **manual copies** of the generated `openwiki/` pages, so they can be listed in `SUMMARY.md` (mdBook only builds files under `src/`). The OpenWiki workflow updates `openwiki/`, not these copies — re-sync them by hand when the originals change.

## Related pages

- [`AGENTS.md`](AGENTS.md) — `openwiki/` evidence index; validation rules.
- [`README.md`](README.md) — taxonomy of AI code-wiki approaches.
- [`openwiki/`](openwiki/) — generated index (`overview`, `architecture`, `source-map`).
- [`docs/deploy-verification.md`](docs/deploy-verification.md) — deploy runbook; CNAME-only diff check.
- [`docs/agent-notes.md`](docs/agent-notes.md) — operational notes: deploy, OpenWiki/Co-Wiki copies, `.agents/` mirror, `raw/`.
- [`raw/README.md`](raw/README.md) — human draft area → `src/` page.

<!-- OPENWIKI:START -->

## OpenWiki

See [AGENTS.md](AGENTS.md) for OpenWiki agent instructions.

<!-- OPENWIKI:END -->
