---
type: Reference
title: Co-Wiki — Ablauf und Technik
description: Der typische Weg von der Idee zum veröffentlichten Artikel und die technischen Bausteine (Docs-as-Code, MCP, Vektordatenbank/RAG) — einfach erklärt.
tags:
  - co-wiki
  - workflow
  - rag
  - mcp
  - docs-as-code
---

# Ablauf und Technik

## Der typische Ablauf (Vom Gedanken zum fertigen Artikel)

1. **Idee & Thema** — Der Mensch wählt ein Thema (oder die KI bemerkt, dass ein wichtiges Thema
   noch fehlt).
2. **Recherche & Spickzettel (RAG)** — Die KI durchsucht alte Notizen und Unterlagen, um echte
   Fakten zu sammeln.
3. **Erster Entwurf** — Die KI schreibt die Rohfassung mit ersten Überschriften.
4. **Menschliche Prüfung (Human-in-the-Loop)** — Ein Mensch liest alles durch, korrigiert Fehler
   und passt den Schreibstil an.
5. **Veröffentlichung** — Der fertige Text wird für alle im Wiki sichtbar gemacht.
6. **Jungbrunnen-Pflege** — KI-Helfer prüfen regelmäßig, ob Links noch funktionieren oder Infos
   veraltet sind.

### So sieht das in diesem Repo aus

| Schritt | Konkret hier |
|---------|--------------|
| 1 Idee & Thema | neuer `src/<slug>.md` + Eintrag in `src/SUMMARY.md` |
| 2 Recherche | vorhandene `src/`-Seiten und `openwiki/`-Index lesen; Unsicherheiten benennen |
| 3 Entwurf | Rohtext mit Transparenzhinweis oben/unten, Prosa auf Deutsch, relative `.md`-Links |
| 4 Prüfung | der Mensch macht den Faktencheck und den Feinschliff |
| 5 Veröffentlichung | `mdbook build` → `npm run ver` — **nur auf ausdrückliche menschliche Freigabe**, siehe [`../../../../docs/deploy-verification.md`](../../../../docs/deploy-verification.md) |
| 6 Pflege | z. B. „alle Seiten auf tote Links prüfen" als selbstständige Aufgabe (Arbeitsmodell 4) |

## Wie funktioniert das technisch? (Einfach erklärt)

- **Dateien wie am Computer (Docs-as-Code)** — Das Wiki besteht aus einfachen Textdateien, die
  mit Programmen wie Obsidian, Quartz oder MkDocs in schicke Webseiten verwandelt werden. Dieses
  Repo nutzt **mdBook** (`src/*.md` → `book/` → GitHub Pages).
- **Universal-Stecker für KI (Model Context Protocol / MCP)** — Wie ein universelles USB-Kabel,
  über das die KI sicher auf Dateien, Notizen und das Internet zugreifen kann.
- **Schlaue Bedeutungssuche (Vektordatenbank & RAG)** — Die KI sucht nicht nur nach genauen
  Wörtern, sondern versteht die Bedeutung (z. B. findet sie „Hund", wenn du nach „Haustier mit
  vier Pfoten" suchst).
