---
type: Reference
title: Multi-Agenten-Redaktionspipeline
description: Das Roboter-Team — spezialisierte Agenten (Forscher, Architekt, Schreiber, Lektor, Faktenchecker, Verlinker) unter einem Supervisor, die einen Artikel gemeinsam produzieren.
tags:
  - co-wiki
  - multi-agent
  - pipeline
  - subagents
---

# Multi-Agenten-Redaktionspipeline: Das Roboter-Team

Hier arbeitet nicht eine einzelne KI, sondern ein Team spezialisierter Helfer zusammen — wie in
einer echten Redaktion. In diesem Repo sind die Rollen als Subagenten unter
[`.claude/agents/`](../../../agents/) angelegt (`redaktion-*`).

## Wer macht was?

| Rolle | Agent | Aufgabe |
|-------|-------|---------|
| **Der Forscher** | `redaktion-forscher` | Durchsucht Web und vorhandene `src/`-Seiten nach echten Fakten, legt eine Info-Mappe an (Quellen + Zitate). |
| **Der Architekt** | `redaktion-architekt` | Erstellt den Bauplan: Überschriften und ein Satz pro Absatz, worum es dort geht. |
| **Der Schreiberling** | `redaktion-schreiber` | Verfasst anhand des Bauplans den Fließtext auf Deutsch, mit Transparenzhinweis und relativen `.md`-Links. |
| **Der Lektor** | `redaktion-lektor` | Prüft Verständlichkeit, Spannung, Dopplungen, Ton. Kein Faktencheck. |
| **Der Detektiv & Faktenchecker** | `redaktion-faktenchecker` | Vergleicht jede Aussage mit der Info-Mappe. Unbelegtes wird markiert, nicht stillschweigend übernommen. |
| **Der Verlinker** | `redaktion-verlinker` | Setzt Querverweise zu anderen `src/`-Seiten und schlägt Tags/Stichwörter vor. |
| **Der Chef vom Dienst** | Supervisor / Orchestrator | Verteilt Aufgaben, prüft Zwischenstände, entscheidet „weiter" oder „nochmal". In Claude Code ist das der **Haupt-Thread** (bzw. der Mensch), nicht ein eigener Subagent — nur der Haupt-Thread kann Subagenten starten. |

## Schritt für Schritt

1. **Briefing** — Der Supervisor bekommt den Auftrag: „Schreibe einen leicht verständlichen
   Artikel über Thema X."
2. **Recherche** — Der Forscher sammelt die wichtigen Bausteine, sortiert Unwichtiges aus,
   füllt die Info-Mappe.
3. **Gliederung** — Der Architekt baut das Überschriften-Gerüst.
4. **Drafting** — Der Schreiberling füllt das Gerüst mit Text.
5. **Kritikschleife** — Faktenchecker und Lektor prüfen genau. Bei Fehlern überarbeitet der
   Schreiberling erneut — **maximal 2–3 Runden**, dann eskaliert der Supervisor an den Menschen.
6. **Finale** — Ein Mensch wirft den letzten Blick darauf und gibt frei (Human-in-the-Loop,
   dann `mdbook build` / `npm run ver` nur auf ausdrückliche Freigabe).

## Hinter den Kulissen

- **Roboter-Regelpläne (LangGraph, CrewAI):** Werkzeuge, die festlegen, welcher Agent wann mit
  welcher Aufgabe dran ist. In Claude Code übernimmt das der Haupt-Thread mit dem Agent-Tool.
- **Gemeinsamer Schmierzettel (Shared State):** Ein Notizblock, auf den alle zugreifen. Hier:
  eine Arbeitsdatei im Scratchpad (Info-Mappe, Bauplan, Review-Notizen) statt Kontext-Weitergabe.
- **Schlaue Arbeitsteilung (Kosten sparen):**
  - *Schnelle, sparsame Modelle* (z. B. Haiku, Gemini Flash) — Gliederung, Tippfehlersuche, Tags.
  - *Starke Denk-Modelle* (z. B. Opus/Sonnet, Gemini Pro) — schwierige Recherche, tiefgründiger
    Fließtext, Faktencheck.
  - Die Subagent-Dateien setzen dafür je ein passendes `model` in der Frontmatter.

## Bezug zu den Arbeitsmodellen

Die Pipeline ist eine ausgebaute Variante von Arbeitsmodell 4 („Selbstständiger Roboter") aus
[`arbeitsmodelle.md`](arbeitsmodelle.md): mehr Spezialisierung, feste Kritikschleife, aber
weiterhin menschliche Freigabe am Ende.
