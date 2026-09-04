---
type: Agent Guide
title: Wiki-KI-Agenten — Das schlaue Lexikon der Zukunft
description: Leitfaden für Coding Agents — wie Mensch und KI-Roboter im Co-Wiki, in der Multi-Agenten-Pipeline und bei Event-Driven Documentation zusammenarbeiten.
tags:
  - agents
  - co-wiki
  - multi-agent
  - event-driven
  - openwiki
  - evidence-index
  - validation
audience: coding agents
schema: LLM-Wiki pattern (Karpathy) — frontmatter + named sections + Related pages; frontmatter fields align with Google's Open Knowledge Format (OKF); interlinked like the openwiki/ pages
---

# Wiki-KI-Agenten: Das schlaue Lexikon der Zukunft

> **Schema.** Same shape as [`CLAUDE.md`](CLAUDE.md) and the [`openwiki/`](openwiki/) pages:
> frontmatter, named sections, and a **Related pages** section. The block between the
> `OPENWIKI` markers below is managed by the OpenWiki workflow — edit around it, not inside it.
>
> The frontmatter matches Google's **Open Knowledge Format** (OKF), a vendor-neutral spec for
> knowledge as a directory of Markdown files: `type` required; `title` / `description` /
> `resource` / `tags` / `timestamp` optional; free-form body. Keep new meta-docs OKF-compatible.
> See the OKF section in [`README.md`](README.md).

Ein digitales Lexikon über Ahrensburg, an dem Menschen **und** KI-Agenten schreiben — sie
recherchieren, entwerfen, korrigieren, verlinken und halten das Wissen aktuell.

**Kurzfassung — volle Beschreibung in der [`co-wiki`-Skill](.claude/skills/co-wiki/SKILL.md)
und deren `references/`; bei Bedarf laden.**

## Die drei Betriebsmuster

### 1. Co-Wiki: Mensch und KI schreiben gemeinsam

Mensch und KI arbeiten am selben Markdown-Ordner (`src/`). Der **Mensch** (Chef) entscheidet:
Themen, Prompts, Faktencheck, Feinschliff, Freigabe. Die **KI** (Assistent) führt aus: Entwürfe,
Zusammenfassungen, Formatierung, Verlinkung, Korrektur. Das **Wiki** (Bibliothek) bewahrt auf,
vernetzt (Tags/Links) und versioniert (git). Die KI veröffentlicht nie eigenständig und trifft
keine inhaltliche Letztentscheidung.

Ablauf: Idee → Recherche (RAG) → Entwurf → menschliche Prüfung (Human-in-the-Loop) →
Veröffentlichung → Pflege. Vier Arbeitsmodelle (Mensch schreibt/KI korrigiert · KI entwirft/Mensch
verbessert · parallel · autonom mit menschlicher Freigabe). Technische Bausteine: Docs-as-Code
(mdBook), MCP, Vektordatenbank/RAG. Details: `references/rollen.md`, `arbeitsmodelle.md`,
`ablauf-und-technik.md`.

### 2. Multi-Agenten-Redaktionspipeline (Das Roboter-Team)

Ein Team spezialisierter Subagenten unter [`.claude/agents/`](.claude/agents/) (`redaktion-*`,
gespiegelt in `.agents/agents/`):

- **`redaktion-forscher`** — belegte Fakten in eine Info-Mappe
- **`redaktion-architekt`** — Überschriften-Bauplan
- **`redaktion-schreiber`** — Fließtext, arbeitet Korrekturen ein
- **`redaktion-lektor`** — Verständlichkeit, Ton, Dopplungen (kein Faktencheck)
- **`redaktion-faktenchecker`** — jede Aussage gegen die Info-Mappe
- **`redaktion-verlinker`** — Querverweise und Schlagwörter
- **Supervisor** — der Haupt-Thread bzw. der Mensch (ein Subagent startet keine Subagenten)

Ablauf: Briefing → Recherche → Gliederung → Drafting → Kritikschleife (Faktenchecker + Lektor,
max. 2–3 Runden) → menschliche Freigabe. Kostenaufteilung: einfache Jobs auf `haiku`,
Recherche/Schreiben/Faktencheck auf `sonnet`. Details: `references/multi-agent-pipeline.md`.

### 3. Event-Driven Documentation (selbst-aktualisierendes Buch)

Ein Ereignis (Push auf `main`, geschlossenes Issue/PR, manuelle Inhaltsmeldung) löst aus:
Wichtigkeits-Check → betroffene `src/`-Seite finden → **Delta-Update** (nur den veralteten Satz /
die Tabelle ersetzen, nie neu schreiben) → Vorher/Nachher-Diff dem Menschen vorlegen → Freigabe →
Deploy. Mehrere kleine Änderungen werden gesammelt (Batching). Agent: `redaktion-aktualisierer`.
Struktur, Ton und der Transparenzhinweis bleiben unangetastet. Details:
`references/event-driven-docs.md`.

---

## Roh-Ordner `raw/`

`raw/<thema>.md` ist die Ablage, in der **Menschen** Artikel und Notizen roh vorschreiben
(Vorlage: `raw/_vorlage.md`). Für Agenten:

- `raw/` liegt außerhalb von `src/`, steht nicht in `SUMMARY.md`, wird nicht gebaut — nichts
  davon erscheint auf der Website.
- Eine Rohfassung in `raw/` ist ein **Auftrag zum Ausarbeiten**, keine fertige Seite: daraus
  Gliederung + Fließtext machen, Fakten gegen die im Roh-Text genannten Quellen prüfen, dann dem
  Menschen zur Freigabe vorlegen.
- Erst nach der Freigabe: neue `src/<slug>.md` anlegen **und** `SUMMARY.md`-Eintrag ergänzen,
  Transparenzhinweis oben und unten. Die Rohfassung in `raw/` nicht ungefragt löschen.
- **`raw/<thema>.md` wird nicht versioniert** (`.gitignore`; nur `raw/README.md` und
  `raw/_vorlage.md` sind eingecheckt). Eine gelöschte Rohfassung ist endgültig weg — es gibt
  keine Wiederherstellung aus der Git-Historie. Alles Erhaltenswerte muss in die `src/`-Seite.

Details: [`raw/README.md`](raw/README.md).

---

## Token-Effizienz & Ressourcenschonung

Um Kontextfenster und Tokenverbrauch bei voller Qualität minimal zu halten:

- **Delta-Updates statt Full-Rewrites:** Bestehende `src/`-Seiten oder Quellcodedateien immer punktgenau bearbeiten (nur geänderte Zeilen/Absätze ersetzen), niemals ganze Dateien komplett neu ausgeben.
- **Gezielter Dateizugriff (Scoping):** Vor dem Lesen mit `grep_search` filtern und bei `view_file` strikt Zeilengrenzen (`StartLine` / `EndLine`) nutzen, statt hunderte Zeilen auf Verdacht in den Kontext zu laden.
- **Recherche-Isolation (Subagenten):** Aufwändige Web-Suchen, Mehrfachabfragen oder grobe Quellensichtungen in Subagenten (z. B. `redaktion-forscher` oder `research`) auslagern. Der Hauptkontext erhält nur die kompakte Faktenmappe/Zusammenfassung.
- **Präzise, No-Fluff Kommunikation:** Antworten direkt, faktenorientiert und strukturiert formulieren – ohne einleitende Höflichkeitsfloskeln oder redundante Inhaltswiederholungen.

<!-- OPENWIKI:START -->

## OpenWiki

This repository has a generated `openwiki/` evidence index. It is optional just-in-time context, not required startup reading.

- Treat source code and tests as authoritative. A brief's unknowns and review items are verification gaps, not automatic requirements.
- Prefer the narrowest quiet validation that proves the changed behavior. Preserve complete failure output.

The scheduled OpenWiki GitHub Actions workflow refreshes the repository wiki. Do not hand-edit generated OpenWiki pages unless explicitly asked; prefer updating source code/docs and letting OpenWiki regenerate.

<!-- OPENWIKI:END -->

## Related pages

- [`CLAUDE.md`](CLAUDE.md) — build/deploy commands and content conventions.
- [`README.md`](README.md) — taxonomy of AI code-wiki approaches and where OpenWiki fits.
- [`openwiki/overview.md`](openwiki/overview.md) — project overview (generated).
- [`openwiki/architecture.md`](openwiki/architecture.md) — build & content architecture (generated).
- [`openwiki/source-map.md`](openwiki/source-map.md) — per-file map of the repository (generated).
- [`docs/deploy-verification.md`](docs/deploy-verification.md) — deploy runbook and the CNAME-only diff check.
- [`docs/agent-notes.md`](docs/agent-notes.md) — collected operational notes (deploy, OpenWiki copies, Co-Wiki copies).
- [`raw/README.md`](raw/README.md) — human draft area; how a Rohfassung becomes a `src/` page.
- [`src/co-wiki.md`](src/co-wiki.md) — öffentliche Besucher-Seite über das Co-Wiki-Modell.

