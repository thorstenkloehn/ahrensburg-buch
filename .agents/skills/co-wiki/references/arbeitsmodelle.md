---
type: Reference
title: Co-Wiki — die vier Arbeitsmodelle
description: Die vier Muster, nach denen Mensch und KI im Co-Wiki zusammenarbeiten, mit Einsatzhinweisen.
tags:
  - co-wiki
  - arbeitsmodelle
  - workflow
---

# Wie arbeiten Mensch und KI zusammen?

Vier Muster. Der Mensch wählt pro Aufgabe eines aus (oder wechselt mittendrin).

## 1. Mensch schreibt, KI korrigiert

Der Mensch schreibt den Aufsatz, die KI prüft Rechtschreibung, Grammatik und Satzbau und schlägt
passende Links vor.

- **Gut für:** Texte, bei denen Stimme und Urteil des Menschen im Vordergrund stehen; heikle oder
  wertende Themen.
- **KI-Rolle:** rein unterstützend — korrigieren, verlinken, formatieren. Keine inhaltlichen
  Umschreibungen ohne Rückfrage.

## 2. KI schreibt vor, Mensch verbessert

Die KI liefert den ersten Entwurf, der Mensch macht ihn richtig gut und besser verständlich.

- **Gut für:** neue Seiten von null, Zusammenfassungen großer Quellen, Standardstruktur.
- **KI-Rolle:** vollständigen Rohtext liefern, klar als Entwurf gekennzeichnet, mit benannten
  Unsicherheiten und Quellen für den Faktencheck.

## 3. Gleichzeitig nebeneinander

Der Mensch schreibt an Kapitel 1, während die KI parallel schon an Kapitel 2 arbeitet.

- **Gut für:** große Seiten oder mehrere Seiten auf einmal, unter Zeitdruck.
- **KI-Rolle:** am zugewiesenen Abschnitt bleiben, keine fremden Abschnitte anfassen, damit sich
  die beiden nicht in die Quere kommen (getrennte Dateien/Abschnitte, saubere Diffs).

## 4. Selbstständiger Roboter

Die KI arbeitet Aufgaben allein ab (z. B. „alle Seiten auf tote Links prüfen und reparieren"),
aber am Ende muss **immer ein Mensch** auf „Freigeben" drücken.

- **Gut für:** mechanische, gut abgegrenzte Wartungsaufgaben über viele Seiten.
- **KI-Rolle:** Aufgabe abarbeiten, Ergebnis zur Prüfung vorlegen. **Nicht** deployen
  (`npm run ver`) ohne ausdrückliche menschliche Freigabe — siehe
  [`docs/deploy-verification.md`](../../../../docs/deploy-verification.md).

## Gemeinsame Regel für alle vier Modelle

Egal welches Modell: Themenwahl, inhaltliche Letztentscheidung und die Freigabe zur
Veröffentlichung liegen beim Menschen.
