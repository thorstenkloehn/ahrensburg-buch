---
name: co-wiki
description: Das Co-Wiki-Modell dieses Repos — Rollen von Mensch, KI und Wiki, die vier Arbeitsmodelle, der Ablauf von der Idee zum Artikel, die technischen Bausteine (Docs-as-Code, MCP, RAG) und die zwei fortgeschrittenen Muster (Multi-Agenten-Redaktionspipeline, Event-Driven Documentation). Aufrufen bei Arbeit an src/-Seiten, bei Fragen zu Zuständigkeit (Themenwahl, Faktencheck, Freigabe) oder „was ist ein Co-Wiki".
---

# Co-Wiki: Mensch & KI Hand in Hand

Ein **Co-Wiki** ist ein digitales Wissensbuch, bei dem Menschen und künstliche Intelligenz (KI)
Hand in Hand zusammenarbeiten. Beide sitzen virtuell am selben Schreibtisch: Sie greifen auf
denselben Ordner zu und lesen dieselben Textdateien (hier: Markdown unter `src/`).

Dieses Repo (`wissen-ahrensburg.de`, eine mdBook-Wissensdatenbank über Ahrensburg) ist so ein
Co-Wiki. Diese Skill fasst zusammen, wer welche Rolle hat und wie zusammengearbeitet wird.

## Die drei Rollen — Kurzfassung

| Rolle | Bild | Kernaufgabe |
|-------|------|-------------|
| **Mensch** | Der Chef | Entscheidet: Themen, Prompts, Faktencheck, Feinschliff, Freigabe |
| **KI** | Der fleißige Assistent | Führt aus: Entwürfe, Zusammenfassungen, Formatierung, Verlinkung, Korrektur |
| **Wiki** | Die Bibliothek | Bewahrt auf: zentraler Speicher, gemeinsame Schnittstelle, Vernetzung, Versionsgeschichte |

Details: [`references/rollen.md`](references/rollen.md).

## Die vier Arbeitsmodelle — Kurzfassung

1. **Mensch schreibt, KI korrigiert** — Mensch verfasst, KI prüft Rechtschreibung und schlägt Links vor.
2. **KI schreibt vor, Mensch verbessert** — KI liefert den Rohentwurf, Mensch macht ihn gut und verständlich.
3. **Gleichzeitig nebeneinander** — Mensch an Kapitel 1, KI parallel an Kapitel 2.
4. **Selbstständiger Roboter** — KI arbeitet Aufgaben allein ab; am Ende drückt **immer ein Mensch** auf „Freigeben".

Details: [`references/arbeitsmodelle.md`](references/arbeitsmodelle.md).

## Der typische Ablauf — Kurzfassung

Idee & Thema → Recherche (RAG) → Erster Entwurf → Menschliche Prüfung (Human-in-the-Loop) →
Veröffentlichung → Jungbrunnen-Pflege (Links/Aktualität).

Technische Bausteine: **Docs-as-Code** (Textdateien → Website, hier mdBook), **MCP** (sicherer
Zugriff der KI auf Dateien/Web), **Vektordatenbank & RAG** (Bedeutungssuche statt Wortsuche).

Details: [`references/ablauf-und-technik.md`](references/ablauf-und-technik.md).

## Fortgeschrittene Muster

- **Multi-Agenten-Redaktionspipeline (Das Roboter-Team)** — ein Team spezialisierter Subagenten
  (Forscher, Architekt, Schreiberling, Lektor, Faktenchecker, Verlinker) unter einem Supervisor
  produziert einen Artikel mit fester Kritikschleife. Die Subagenten liegen unter
  [`.claude/agents/`](../../agents/) (`redaktion-*`).
  Details: [`references/multi-agent-pipeline.md`](references/multi-agent-pipeline.md).
- **Event-Driven Documentation (selbst-aktualisierendes Buch)** — ein Ereignis (Push, erledigtes
  Issue, Meeting-Notiz) löst einen Wichtigkeits-Check aus; die betroffene Seite bekommt ein
  gezieltes **Delta-Update** als Vorschlag, das ein Mensch freigibt. Agent:
  `redaktion-aktualisierer`.
  Details: [`references/event-driven-docs.md`](references/event-driven-docs.md).

## So wendet ein Agent das hier an

- **Nie eigenständig veröffentlichen.** `mdbook build` / `npm run ver` (Deploy) nur auf
  ausdrückliche Anweisung. Die Freigabe-Entscheidung liegt beim Menschen (Modell 4).
- **Fakten nicht erfinden.** Bei fehlenden oder unsicheren Angaben nachfragen statt raten;
  Halluzinationen sind das, was der menschliche Faktencheck abfangen muss — mach ihm die Arbeit
  leicht, indem du Quellen/Unsicherheiten benennst.
- **Formales sauber liefern.** Transparenzhinweis oben und unten auf jeder Inhaltsseite
  (Ausnahme `datenschutz.md`), relative `.md`-Links, `SUMMARY.md`-Eintrag bei neuen Seiten,
  Prosa auf Deutsch. Siehe [`../../../CLAUDE.md`](../../../CLAUDE.md).
- **Rolle klären, wenn unklar.** Themenwahl, inhaltliche Letztentscheidung und Freigabe sind
  Chefsache. Entwerfen, ordnen, zusammenfassen, verlinken und korrigieren ist Assistentenarbeit.

## Verwandte Dokumente im Repo

- [`CLAUDE.md`](../../../CLAUDE.md) — Abschnitt „Zusammenarbeit Mensch & KI (Co-Wiki)": Kurzfassung derselben Rollen, verweist hierher.
- [`AGENTS.md`](../../../AGENTS.md) — Abschnitt „Die drei Betriebsmuster": Kurzfassung, verweist hierher; plus OpenWiki-Regeln.
- [`docs/deploy-verification.md`](../../../docs/deploy-verification.md) — Deploy-Runbook (die „Freigabe" technisch).
- [`.claude/agents/README.md`](../../agents/README.md) — die Redaktions-Subagenten (`redaktion-*`).
- [`README.md`](../../../README.md) — Taxonomie der KI-Code-Wiki-Ansätze.
