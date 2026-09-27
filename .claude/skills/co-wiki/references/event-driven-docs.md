---
type: Reference
title: Event-Driven Documentation
description: Das Buch, das sich selbst aktualisiert — Auslöser, automatischer Kreislauf mit Delta-Update und menschlicher Freigabe, und warum das Wissen dadurch nie veraltet.
tags:
  - co-wiki
  - event-driven
  - automation
  - stale-docs
---

# Event-Driven Documentation: Das Buch, das sich selbst aktualisiert

Menschen vergessen oft, Anleitungen nachzuziehen, wenn sich etwas geändert hat. Bei der
ereignisgesteuerten Dokumentation merkt der Computer die Veränderung selbst und schlägt sofort
die passende Seitenänderung vor.

## Wann wacht die KI auf? (Auslöser / Events)

- **Neuer Programmcode ist fertig** — eine neue Funktion wurde fertiggestellt.
- **Aufgabe erledigt** — in einer Aufgabenliste (z. B. Jira) wird ein Haken bei „Erledigt" gesetzt.
- **Besprechung beendet** — die KI hört im Meeting zu und hält die wichtigsten Entscheidungen fest.

Für dieses Repo realistisch: ein Git-Push auf `main`, ein geschlossenes Issue/PR, oder ein
manueller Anstoß („die Öffnungszeiten von X haben sich geändert").

## Der automatische Kreislauf

1. **Klingelzeichen (Webhook)** — das System meldet: „Es gibt eine wichtige Neuerung."
2. **Wichtigkeits-Check** — die KI prüft: „Ist das für eine Wiki-Seite relevant?" Reine
   Tippfehler oder interne Umbauten werden ignoriert.
3. **Alte Seite finden** — die KI sucht im Wiki, wo die betroffene Erklärung steht
   (`src/`-Seite + Abschnitt).
4. **Gezieltes Ausbessern (Delta Update)** — nur der veraltete Satz / die veraltete Tabelle
   wird ersetzt, nicht der ganze Artikel neu geschrieben.
5. **Vorschlag an den Menschen** — die KI zeigt genau die Änderung als Diff (rot = alt,
   grün = neu).
6. **Freigabe per Klick** — der Mensch bestätigt, die Seite ist wieder aktuell (danach der
   übliche Deploy).

## Warum praktisch?

- **Nie wieder veraltetes Wissen (Stale Docs):** Das Wiki ist immer auf dem Stand von heute.
- **Sammeln statt Drängeln (Batching):** Bei 10 kleinen Änderungen kurz hintereinander wartet
  die KI kurz und macht alles in einem sauberen Durchgang.
- **Zeitersparnis:** Niemand muss veraltete Seiten von Hand suchen und umschreiben.

## Wichtig für Agenten in diesem Repo

- **Delta, nicht Neufassung.** Beim Aktualisieren einer bestehenden Seite nur das Veraltete
  ändern; Struktur, Ton und der Transparenzhinweis oben/unten bleiben stehen.
- **Immer als Vorschlag.** Änderung zeigen, nicht selbst veröffentlichen. Deploy
  (`mdbook build` / `npm run ver`) nur auf ausdrückliche menschliche Freigabe.
- **Batching auch hier:** mehrere anstehende Aktualisierungen sammeln und in einem Commit
  vorschlagen.
- Verwandt: die **Jungbrunnen-Pflege** aus [`ablauf-und-technik.md`](ablauf-und-technik.md)
  (Schritt 6 des typischen Ablaufs) ist die geplante, event-getriebene die spontane Variante
  derselben Idee.
