---
type: Reference
title: Redaktions-Subagenten
description: Die redaktion-* Subagenten der Multi-Agenten-Redaktionspipeline — Rollen, Modelle, Reihenfolge.
tags:
  - subagents
  - multi-agent
  - co-wiki
  - redaktion
---

# Redaktions-Subagenten

Jede `redaktion-*.md` hier ist eine Claude-Code-Subagent-Definition (`name` / `description` /
`tools` / `model` + Systemprompt) für die **Multi-Agenten-Redaktionspipeline**. Volle
Beschreibung des Ablaufs:
[`../skills/co-wiki/references/multi-agent-pipeline.md`](../skills/co-wiki/references/multi-agent-pipeline.md).
Rollen-Tabelle mit Modellen und Merksätzen: [`../../docs/agent-notes.md`](../../docs/agent-notes.md) §4.

| Datei | Rolle | Modell | Wann |
|-------|-------|--------|------|
| `redaktion-forscher.md` | Fakten sammeln, Info-Mappe | sonnet | Schritt 1, vor allem anderen |
| `redaktion-architekt.md` | Bauplan / Überschriften | haiku | nach der Recherche |
| `redaktion-schreiber.md` | Fließtext, Überarbeitungen | sonnet | nach der Gliederung, jede Runde |
| `redaktion-lektor.md` | Stil, Aufbau, Dopplungen | haiku | Kritikschleife |
| `redaktion-faktenchecker.md` | jede Aussage gegen die Info-Mappe | sonnet | Kritikschleife |
| `redaktion-verlinker.md` | Querverweise, Tags | haiku | letzter Schritt vor der Freigabe |
| `redaktion-aktualisierer.md` | Delta-Updates (Event-Driven) | sonnet | wenn sich eine belegte Tatsache ändert |

**Supervisor** = der Haupt-Thread (bzw. der Mensch); nur er startet Subagenten, ein Subagent
startet keine weiteren. Er brieft, ruft in Reihenfolge auf, führt den Shared State (eine
Scratchpad-Datei) zusammen, entscheidet nach der Kritikschleife „weiter" / „nochmal" (max.
2–3 Runden, dann an den Menschen) und legt dem Menschen zur Freigabe vor. Kein Subagent deployt.
