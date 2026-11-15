---
name: raw-zu-artikel
description: Verwandle einen menschlichen Rohentwurf aus raw/<thema>.md mithilfe der 7-stufigen Multi-Agenten-Redaktionspipeline (Forscher, Architekt, Schreiber, Faktenchecker, Lektor, Verlinker) in einen veröffentlichungsreifen Wiki-Artikel. Kompatibel mit Codex, Antigravity (agy) und Claude Code.
---

# Raw-zu-Artikel (Multi-Agenten-Redaktionspipeline)

Diese Skill orchestriert den gesamten Weg von einer menschlichen Rohfassung unter [`raw/<thema>.md`](../../../raw/README.md) bis zum freigabefertigen Artikelentwurf gemäß dem Co-Wiki-Modell ([`.claude/skills/co-wiki/SKILL.md`](../co-wiki/SKILL.md)) und den Spezial-Subagenten unter [`.claude/agents/`](../../agents/README.md).

---

## 1. Grundregeln für `raw/` (Zwingend zu beachten!)

1. **`raw/<thema>.md` ist nicht versioniert (`.gitignore`):**
   - Nur `raw/README.md` und `raw/_vorlage.md` stehen in Git.
   - **NIEMALS** eine Datei in `raw/<thema>.md` ungefragt löschen oder überschreiben! Eine gelöschte Rohfassung ist unwiederbringlich verloren.
2. **Ein Rohentwurf ist ein Arbeitsauftrag, keine fertige Seite:**
   - Der Mensch liefert Stichpunkte, Ideen, Absätze und erste Quellenhinweise.
   - Die KI strukturiert, recherchiert fehlende Belege, formuliert den Fließtext eigenständig aus und prüft Fakten sowie Urheberrecht.
3. **Human-in-the-Loop (Freigabevorbehalt):**
   - Erst wenn der Mensch den ausgearbeiteten Entwurf **explizit freigibt**, wird die Datei unter `src/<slug>.md` angelegt und in `src/SUMMARY.md` eingetragen.

---

## 2. Die 6 Pipeline-Phasen (Subagenten-Orchestrierung)

Der Haupt-Agent fungiert als **Supervisor**. Er steuert die Phasen nacheinander (oder über Subagenten) und hält den Zwischenstand in einer temporären Arbeitsdatei (Scratchpad) fest:

### Phase 1: Rohfassung analysieren & Faktenmappe erstellen (`redaktion-forscher`)
- Lies `raw/<thema>.md` vollständig ein.
- Extrahiere alle genannten Behauptungen, Zahlen, Daten, Namen und Quellenlinks.
- Prüfe die genannten Quellen und ergänze fehlende Basisdaten zu Ahrensburg aus verlässlichen, belegten Quellen.
- **Ergebnis:** Strukturierte **Info-Mappe** (nur belegte Fakten + Lizenzstatus jeder Quelle, z. B. amtlich, Wikipedia CC BY-SA 4.0, Stormarn-Lexikon © geschützt). Unbelegte Aussagen aus `raw/` werden als `[UNBELEGT – Rückfrage an Mensch]` markiert.

### Phase 2: Gliederung entwerfen (`redaktion-architekt`)
- Erstelle auf Basis der Info-Mappe und bestehender Nachbarseiten in `src/` einen klaren Überschriften-Bauplan (`# H1`, `## H2`, `### H3`).
- Prüfe mit `/duplicate-content-pruefung` bzw. `scripts/find_duplicate_content.py`, welche Teilaspekte bereits auf anderen `src/`-Seiten eine kanonische Heimat haben, und plane dort kurze Querverweise statt Doppelerklärungen ein.

### Phase 3: Fließtext verfassen (`redaktion-schreiber`)
- Schreibe den vollständigen Artikel auf Deutsch in neutralem, enzyklopädischem Ton.
- **Urheberrecht beachten:** Keine wörtlichen Übernahmen oder engen Paraphrasen aus geschützten Quellen (insb. Stormarn-Lexikon, Zeitungsartikel). Fakten immer in eigener Satzstruktur und Gedankenführung darstellen.
- Füge oben und unten den Pflicht-Transparenzhinweis gemäß Art. 50 EU AI Act ein:
  `*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*`
- Falls Wikipedia substanziell genutzt wurde: Abschnitt `## Wikipedia als Quelle` vor dem unteren Transparenzhinweis einfügen.
- Falls `stormarnlexikon.de` verlinkt wird: Zusatz `(© Kreisarchiv Stormarn, alle Rechte vorbehalten)` ergänzen.

### Phase 4: Parallele Kritikschleife (`redaktion-faktenchecker` + `redaktion-lektor`)
- **Faktencheck (`redaktion-faktenchecker`):** Jede Zahl, jedes Datum und jeder Eigenname im Entwurf wird gegen die Info-Mappe aus Phase 1 abgeglichen. Keine hinzuerfundenen Details!
- **Lektorat (`redaktion-lektor`):** Prüft Verständlichkeit, Lesefluss, Absatzlängen und baut Wortwiederholungen ab.
- Bei Mängeln bessert `redaktion-schreiber` nach (maximal 2–3 Schleifen).

### Phase 5: Vernetzung im Wiki (`redaktion-verlinker`)
- Suche passende bestehende Seiten in `src/SUMMARY.md`:
  1. Welche Seiten soll der neue Artikel im Fließtext und unter `## Verwandte Themen` / `## Siehe auch` verlinken?
  2. Welche **bestehenden** `src/`-Seiten sollten einen Rückverweis (Link) auf den neuen Artikel erhalten?
  3. An welcher exakten Zeile in `src/SUMMARY.md` soll der neue Artikel einsortiert werden?

### Phase 6: Vorlage zur menschlichen Freigabe
Präsentiere dem Menschen das Ergebnis übersichtlich zur Entscheidung:

```markdown
# Entwurf bereit zur Freigabe: [Titel des Artikels]

- **Ausgangsdatei:** `raw/<thema>.md` (bleibt unverändert erhalten)
- **Geplanter Zielpfad:** `src/<slug>.md`
- **Geplante Position in `src/SUMMARY.md`:** Unterhalb von `[Kapitel](datei.md)`
- **Geplante Rückverweise in bestehenden Seiten:** `src/seite-a.md`, `src/seite-b.md`
- **Offene Fakten-Rückfragen:** [Keine / Liste unklarer Punkte aus dem Rohentwurf]

---

## Artikel-Entwurf

[Vollständiger Markdown-Text inklusive Transparenzhinweis oben und unten]

---
**Soll ich diesen Artikel jetzt unter `src/<slug>.md` anlegen und in `src/SUMMARY.md` eintragen?**
```

---

## 3. Abschluss nach Freigabe

Sobald der Mensch zustimmt:
1. `src/<slug>.md` schreiben.
2. `src/SUMMARY.md` per Delta-Edit ergänzen.
3. Geplante Rückverweise in bestehenden `src/`-Seiten per Delta-Edit einfügen.
4. `python3 scripts/check_wiki_conventions.py src` und `mdbook build` zur Verifikation ausführen.
5. `raw/<thema>.md` **nicht** löschen (es sei denn, der Mensch weist dies ausdrücklich an).
