---
type: Reference
title: raw/ — Rohfassungen
description: Ablage für unfertige Artikelentwürfe und lose Notizen von Menschen, bevor daraus eine fertige src/-Seite wird.
tags:
  - raw
  - drafts
  - workflow
  - co-wiki
---

# raw/ — Rohfassungen

Hier schreiben **Menschen** ihre Artikel und Notizen in roher Form auf, bevor daraus eine
polierte Wiki-Seite unter [`../src/`](../src/) wird. Der Roh-Ordner ist die „unordentliche
Notizen"-Stufe aus dem [Co-Wiki-Ablauf](../.claude/skills/co-wiki/references/ablauf-und-technik.md).

## Was hier hin gehört

- Erste Textentwürfe, Stichpunkte, kopierte Absätze, Interview-Mitschriften.
- Alles, was noch nicht fertig ist: unfertige Sätze, offene Fragen, Quellen-Links ohne Fließtext.
- Eine Datei pro geplantem Artikel: `raw/<thema>.md`. Vorlage: [`_vorlage.md`](_vorlage.md).

## Was hier **nicht** hin gehört

- Fertige, freigegebene Artikel — die gehören nach `src/` und in `src/SUMMARY.md`.

## Regeln

- **`raw/` ist nicht Teil des Buchs.** Es liegt außerhalb von `src/`, steht nicht in
  `SUMMARY.md` und wird von `mdbook build` ignoriert. Nichts hier erscheint auf
  <https://wissen-ahrensburg.de>.
- **Kein Transparenzhinweis nötig**, solange es eine Rohfassung ist. Der Hinweis (oben und
  unten) kommt erst dazu, wenn die Seite nach `src/` wandert.
- **Rohfassungen werden nicht versioniert.** `raw/<thema>.md` steht in `.gitignore` (nur diese
  `README.md` und `_vorlage.md` sind im Repo). Das heißt: Eine gelöschte Rohfassung ist
  **endgültig weg** — `git` holt sie nicht aus der Historie zurück. Rohfassungen leben nur
  lokal auf dem Rechner, an dem geschrieben wird. Was erhalten bleiben soll, muss in eine
  fertige `src/`-Seite überführt werden.

## Vom Roh-Ordner zur Wiki-Seite

1. Mensch legt `raw/<thema>.md` an und schreibt los (oder sammelt nur Material).
2. Die KI / die [Redaktions-Subagenten](../.claude/agents/README.md) machen daraus einen
   strukturierten Entwurf: Gliederung, Fließtext, Faktencheck gegen die Quellen im Roh-Text.
3. Mensch prüft und gibt frei.
4. Die fertige Seite wird als `src/<slug>.md` angelegt **und** in `src/SUMMARY.md` verlinkt;
   Transparenzhinweis oben und unten.
5. Die Rohfassung darf in `raw/` bleiben oder gelöscht werden. Da sie nicht versioniert ist,
   ist ein Löschen endgültig — vorher sicherstellen, dass alles Wichtige in der `src/`-Seite steht.

## Abgeschlossene Rohfassungen

- **`Ueberricht.md`** → über die volle Redaktionspipeline zu
  [`src/urheberrecht-und-duplicate-content.md`](../src/urheberrecht-und-duplicate-content.md)
  ausgearbeitet, freigegeben, deployt (`gh-pages` `52107f5`), Rohfassung anschließend gelöscht
  (2026-09-03). Der verwertbare Inhalt steht vollständig in der `src/`-Seite; Details im
  Deploy-Log [`docs/agent-notes.md`](../docs/agent-notes.md) §1.
