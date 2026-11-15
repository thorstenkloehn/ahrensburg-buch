---
name: aktualitaet-und-fakten-check
description: Überprüfe bestehende Wiki-Artikel unter src/ auf veraltete Angaben (Jahreszahlen, Öffnungszeiten, Preise, politische Ämter, Linienpläne, „heute/aktuell"-Formulierungen) sowie defekte externe Weblinks und schlage punktgenaue Delta-Updates vor. Kompatibel mit Codex, Antigravity (agy) und Claude Code.
---

# Aktualitäts- & Fakten-Check (Event-Driven & Bestands-Audit)

Diese Skill leitet Coding- und Redaktions-Agenten (Codex, Antigravity/agy, Claude Code) an, bestehende Artikel im Ahrensburg-Wiki (`src/**/*.md`) systematisch auf **zeitkritische / veraltende Aussagen** und **tote externe Weblinks** zu prüfen und punktgenaue **Delta-Updates** gemäß dem Muster *Event-Driven Documentation* ([`redaktion-aktualisierer`](../../agents/redaktion-aktualisierer.md)) vorzubereiten.

---

## 1. Auftrag & Prüfkategorien

Ein lokales Stadt-Wiki enthält viele Fakten, die im Lauf der Zeit veralten. Diese Skill untersucht `src/` gezielt auf vier Risikogruppen:

1. **Relativ-zeitliche Formulierungen („Zeitfallen"):**
   - Wörter wie *„derzeit"*, *„aktuell"*, *„heute"*, *„seit kurzem"*, *„in diesem Jahr"*, *„demnächst"*, *„geplant bis 202X"*.
   - **Regel:** Solche Angaben müssen immer mit einem konkreten Zeitstempel versehen werden (z. B. *„Stand: 2026"* oder *„seit Frühjahr 2025"*).
2. **Schnelllebige lokale Daten (Ahrensburg-Spezifika):**
   - **Politik & Verwaltung:** Bürgermeister/in, Sitzverteilung der Stadtverordnetenversammlung, Bürgervorsteher/in, Amtsleitungen, Gebühren (`src/buergermeister-und-stadtvertretung.md`, `src/stadtverwaltung.md`).
   - **Verkehr & Infrastruktur:** HVV-Buslinien, Regionalbahn-/U-Bahn-Takte, Baustellen, Parkgebühren (`src/verkehrsanbindung.md`).
   - **Alltag, Kultur & Freizeit:** Wochenmarkt-Zeiten, Öffnungszeiten/Eintrittspreise (Schloss Ahrensburg, Badlantic, Stadtbücherei), regelmäßige Stadtfeste, Vereinsdaten, Gastronomie/Handel.
   - **Demografie & Wirtschaft:** Einwohnerzahlen, Statistik-Stichtage, ansässige Großunternehmen (`src/demografie.md`, `src/wichtige-unternehmen-arbeitgeber.md`).
3. **Externe Weblinks (`https://...`):**
   - Prüfung auf HTTP-Statuscodes (`404 Not Found`, `410 Gone`, abgelaufene Domains oder permanente Weiterleitungen auf unpassende Startseiten).
4. **Vergangene Zukunftsprognosen:**
   - Formulierungen im Futur oder mit vergangenen Zieljahren (z. B. *„soll 2025 fertiggestellt werden"*).

---

## 2. Token-schonender Such-Workflow

Statt alle 66+ Dateien komplett zu lesen, filtert der Agent zuerst mit gezielten Suchbefehlen:

```bash
# 1. Zeitfallen („aktuell", „derzeit", „voraussichtlich", „geplant") finden
git grep -inE "(derzeit|aktuell|gegenwärtig|voraussichtlich|geplant|künftig|demnächst)" src/

# 2. Jahreszahlen der jüngeren Vergangenheit/Gegenwart prüfen
git grep -inE "202[0-6]" src/

# 3. Alle externen URLs in src/ extrahieren
git grep -Eo "https?://[^ )\">']+" src/ | sort -u
```

Für die Prüfung externer URLs kann ein schneller `curl`-Check (HEAD/GET mit kurzem Timeout) ausgeführt werden. Aufwändige Web-Recherchen zu geänderten Fakten werden an den Subagenten `research` bzw. `redaktion-forscher` delegiert.

---

## 3. Das Delta-Update-Prinzip (Keine Full-Rewrites!)

Wenn ein veralteter Fakt gefunden und durch eine verlässliche Quelle neu belegt wurde, gilt strikt das Prinzip des [`redaktion-aktualisierer`](../../agents/redaktion-aktualisierer.md):

- **Nur den betroffenen Satz / Tabellenwert aktualisieren** (Delta-Edit).
- **Struktur, Ton, Nachbarabsätze und den EU-AI-Act-Transparenzhinweis unangetastet lassen.**
- **Stand-Angabe ergänzen:** Bei veränderlichen Größen immer `(Stand: Monat JJJJ)` oder `(Stand: JJJJ)` dazuschreiben.

---

## 4. Berichtsformat (Vorher/Nachher-Diff zur Freigabe)

Vor jeder inhaltlichen Änderung an Fakten legt der Agent dem Menschen eine kompakte Übersicht vor:

```markdown
# Prüfbericht: Aktualitäts- & Fakten-Check

**Geprüfter Bereich:** [Gesamtes `src/` / Spezifische Kategorie]
**Geprüfte externe URLs:** [Anzahl] (davon defekt/weitergeleitet: [X])

## 1. Gefundene Aktualisierungsbedarfe

| Nr. | Dringlichkeit | Fundstelle (`Datei:Zeile`) | Aktueller Text im Wiki | Neuer belegter Stand & Quelle |
|---|---|---|---|---|
| 1 | 🔴 HOCH | `src/datei.md:42` | „soll Ende 2025 eröffnen" | Wurde im März 2026 eröffnet ([Quelle](https://...)) |
| 2 | 🟡 MITTEL | `src/datei.md:88` | Defekter Link (`404`) | Neue Ziel-URL: `https://...` |

## 2. Vorgeschlagene Delta-Updates

### `src/datei.md` (Zeile 42)
- **Vorher:** `...`
- **Nachher:** `...`
- **Beleg:** [Offizielle Quelle / Website]
```
