---
type: Source Map
title: Source File Map
description: Map of source files, generated outputs, configuration, documentation, and agent tooling in the Ahrensburg mdBook repository.
tags:
  - source-map
  - files
  - mdbook
---

# Source File Map

## Configuration and build files

| File | Purpose |
|------|---------|
| `book.toml` | mdBook configuration: title, authors, language, output theme settings, Mermaid preprocessor, additional JS. |
| `package.json` | Declares `gh-pages` dependency and the `ver` deploy script. |
| `package-lock.json` | Locked npm dependency versions (gitignored but present in working tree). |
| `.gitignore` | Excludes `book/`, `node_modules/`, `package-lock.json`, and `raw/*.md` drafts. |
| `mermaid.min.js` | Vendored Mermaid runtime used by `mdbook-mermaid`. |
| `mermaid-init.js` | Theme-aware Mermaid initializer; reloads diagrams on mdBook theme changes. |

## Content source (`src/`)

| File | Summary | Listed in `SUMMARY.md` |
|------|---------|------------------------|
| `SUMMARY.md` | Table of contents and page hierarchy. | Yes (root navigation) |
| `hauptseite.md` | Main landing page, license note, sister projects. | Yes |
| `geschichte-allgemeines.md` | History & general section intro. | Yes |
| `geschichte-der-stadt-ahrensburg.md` | Detailed city history from prehistory to modern era. | Yes |
| `ahrensburger-tunneltal.md` | Ahrensburg Tunnel Valley and the Ahrensburg Culture. | Yes |
| `stadtwappen.md` | Coat of arms and flag of Ahrensburg. | Yes |
| `geografie.md` | Geography, districts, climate, forests, nature reserves. | Yes |
| `sehenswuerdigkeiten-kultur.md` | Sights & culture section intro. | Yes |
| `sehenswuerdigkeiten.md` | Overview of sights. | Yes |
| `schloss-ahrensburg.md` | History and use of Ahrensburg Castle. | Yes |
| `schlosskirche-ahrensburg.md` | Ahrensburg Castle Church. | Yes |
| `musik-und-theater.md` | Music and theater venues/groups. | Yes |
| `regelmaessige-feste-veranstaltungen.md` | Regular festivals and events. | Yes |
| `alltag-leben-in-ahrensburg.md` | Everyday life section intro. | Yes |
| `die-stadtteile-im-portraet.md` | Portrait of city districts. | Yes |
| `vereinsleben.md` | Club and association life. | Yes |
| `wochenmarkt.md` | Weekly market. | Yes |
| `gastronomie-fuehrer.md` | Gastronomy guide overview. | Yes |
| `restaurant.md` | Restaurant listings/details. | Yes |
| `uebernachtungsmoeglichkeiten-in-ahrensburg-2.md` | Accommodation options (linked from section). | Yes |
| `einkaufen-in-ahrensburg-2.md` | Shopping options (linked from section). | Yes |
| `kirchen-und-religioese-gemeinschaften.md` | Churches and religious communities. | Yes |
| `seniorentreff.md` | Senior meeting places. | Yes |
| `gesundheit.md` | Health services. | Yes |
| `familie-bildung.md` | Family and education. | Yes |
| `natur-freizeit.md` | Nature & leisure section intro. | Yes |
| `naherholungsgebiete.md` | Local recreation areas. | Yes |
| `wander-und-radwege.md` | Hiking and cycling routes. | Yes |
| `spielplaetze.md` | Playgrounds. | Yes |
| `infrastruktur-wirtschaft.md` | Infrastructure & economy section intro. | Yes |
| `verkehrsanbindung.md` | Transport links. | Yes |
| `wichtige-unternehmen-arbeitgeber.md` | Important companies and employers. | Yes |
| `gewerbegebiete.md` | Commercial areas. | Yes |
| `stadtverwaltung.md` | City administration. | Yes |
| `ahrensburg-nachrichten-website.md` | Ahrensburg news website topic. | Yes |
| `co-wiki.md` | Public Co-Wiki page describing human/AI collaboration. | Yes |
| `software-fuer-ein-grosses-wissensprojekt.md` | Comparison framing page for wiki/CMS/doc-generator choices. | Yes |
| `wikis-im-vergleich.md` | Comparison of open wiki programs. | Yes |
| `cms-im-vergleich.md` | Comparison of open content management systems. | Yes |
| `doku-generatoren-im-vergleich.md` | Comparison of documentation/site generators. | Yes |
| `datenschutz.md` | Privacy policy / Datenschutzerklärung. | Yes |
| `impressum.md` | Legal imprint. | Yes |
| `einkaufen-in-ahrensburg.md` | Duplicate shopping page (orphaned from main sections). | No |
| `uebernachtungsmoeglichkeiten-in-ahrensburg.md` | Duplicate accommodation page (orphaned). | No |

## Generated output (`book/`)

The `book/` directory contains the static HTML, CSS, JavaScript, fonts, Mermaid assets, and search index produced by `mdbook build`. It is gitignored but deployed to the `gh-pages` branch. Key files:

| File | Purpose |
|------|---------|
| `book/index.html` | Built homepage (mirrors `hauptseite.html`). |
| `book/*.html` | One rendered HTML page per source Markdown file. |
| `book/searchindex.js` | Full-text search index used by mdBook's built-in search. |
| `book/print.html` | Single-page print version of the entire book. |
| `book/.nojekyll` | Disables Jekyll processing on GitHub Pages. |
| `book/mermaid.min.js` / `book/mermaid-init.js` | Copied from repo root by mdBook for runtime diagram rendering. |

## OpenWiki copies (`src/openwiki/`)

| File | Purpose |
|------|---------|
| `src/openwiki/overview.md` | Manual copy of `openwiki/overview.md` for inclusion in the book. |
| `src/openwiki/architecture.md` | Manual copy of `openwiki/architecture.md`. |
| `src/openwiki/source-map.md` | Manual copy of `openwiki/source-map.md`. |

## Documentation and agent files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Agent instructions referencing the generated OpenWiki evidence index. |
| `CLAUDE.md` | Claude Code guidance: build commands, conventions, project purpose. |
| `README.md` | Taxonomy of AI code-wiki approaches and where this repo's OpenWiki setup fits. |
| `docs/deploy-verification.md` | Deploy runbook and CNAME-only diff check. |
| `docs/agent-notes.md` | Operational notes for agents (deploy, OpenWiki copies, Co-Wiki copies). |
| `docs/verification/` | Render-verification screenshots. |
| `openwiki/` | Generated code wiki (this directory). |
| `openwiki/INSTRUCTIONS.md` | OpenWiki brief: "A code wiki for this repository." |

## Draft and agent-tooling directories

| Path | Purpose |
|------|---------|
| `raw/` | Human draft area. `raw/*.md` is gitignored; only `raw/README.md` and `raw/_vorlage.md` are tracked. |
| `.claude/skills/co-wiki/` | Co-Wiki skill: operative guidance for agents working on `src/` pages. |
| `.claude/agents/` | Subagent definitions for the multi-agent editorial pipeline. |
| `.agents/` | Mirror of `.claude/agents` + `.claude/skills` for other agent runners; checked in (byte-identical copy, re-synced after changes to `.claude/`). |
