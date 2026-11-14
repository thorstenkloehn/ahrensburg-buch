---
name: duplicate-content-pruefung
description: Überprüfe alle Inhalte dieses Wikis auf interne Textdopplungen (Internal Duplicate Content) und externe Redundanzen. Identifiziere wiederholte Absätze, bestimme die kanonische Hauptseite (Single Source of Truth) und schlage Querverweise vor, um Keyword-Kannibalisierung und Redundanz zu beheben. Kompatibel mit Codex, Antigravity (agy) und Claude Code.
---

# Duplicate Content & Redundanz-Prüfung (Wiki-Audit)

Diese Skill leitet Coding- und Redaktions-Agenten (Codex, Antigravity/agy, Claude Code) an, alle Inhaltsseiten dieses Wikis (`src/**/*.md`) systematisch auf interne Textdopplungen (Internal Duplicate Content) und übermäßige Redundanzen zu überprüfen.

---

## 1. Auftrag & Zielsetzung

Duplicate Content führt in Wissensprojekten zu drei wesentlichen Problemen:
1. **Suchmaschinen-Probleme (SEO & Keyword-Kannibalisierung):** Findet Google weitgehend identische Absätze auf mehreren Unterseiten, kann das Ranking-Signal zersplittern. Die Suchmaschine bestimmt oft willkürlich eine Version als kanonisch und stuft andere Seiten herab.
2. **Wartungs-Albtraum (Sync-Overhead):** Wenn Fakten (z. B. historische Daten, Öffnungszeiten, Adressen) auf fünf Seiten wiederholt werden, führt jede spätere Korrektur zu veralteten Angaben auf den anderen vier Seiten.
3. **Minderwertiges Leseerlebnis:** Besuchende, die sich durch das Buch navigieren, empfinden wiederholte Floskeln und doppelte Zusammenfassungen als redundanten Fülltext.

**Ziel des Skills:**
- Aufspüren aller identischen oder eng verwandten Textabsätze (Jaccard-Ähnlichkeit ≥ 50 % oder identische Satzketten) über Seitengrenzen hinweg.
- Festlegung der **Single Source of Truth (Kanonische Hauptseite)** für das jeweilige Thema.
- Bereinigung der Nebenseiten: Ersetzen des doppelten Fließtextes durch eine prägnante 1-Satz-Zusammenfassung mit gezieltem **Querverweis** (`[Thema](zielseite.md)`).

---

## 2. Analyseverfahren: Automatisiert & Token-schonend

Um Kontextfenster nicht mit manuellem Lesen aller Dateien zu belasten, nutzt der Agent das im Repository bereitgestellte Analyse-Skript [`scripts/find_duplicate_content.py`](../../../scripts/find_duplicate_content.py):

```bash
python3 scripts/find_duplicate_content.py src 0.50
```

### Was das Skript leistet:
- Extrahiert alle Absätze aus `src/**/*.md` (unter Ausschluss von `SUMMARY.md` und `openwiki/`).
- Filtert bekannte Standardblöcke heraus (z. B. Transparenzhinweise gemäß Art. 50 EU AI Act, Wikipedia-Lizenzbausteine).
- Berechnet 4-Gramm-Shingles und die Jaccard-Ähnlichkeit zwischen allen Absatzpaaren.
- Gibt eine sortierte Liste aller signifikanten Dopplungen mit Zeilennummern und Ähnlichkeitsprozenten aus.

---

## 3. Lösungsstrategie: Das „Single Source of Truth“-Prinzip

Für jede identifizierte Dopplung wendet der Agent folgende Redaktionsregeln an:

| Schritt | Regel & Vorgehen |
|---|---|
| **1. Hauptseite bestimmen** | Wo gehört die Information logisch zuhause hin? *(Beispiel: Ausführliche Baudaten zum Schloss gehören auf `schloss-ahrensburg.md`, nicht als langer Volltext auf `persoenlichkeiten.md` oder `sehenswuerdigkeiten.md`).* |
| **2. Nebenseiten verdichten** | Auf den Neben- oder Verteilerseiten wird der redundante Absatz auf **1 bis maximal 2 Sätze** verdichtet. |
| **3. Querverweis setzen** | Ein präziser Markdown-Link verweist direkt auf das Hauptkapitel: `Mehr zur Entstehungsgeschichte beschreibt das Kapitel [Schloss Ahrensburg](schloss-ahrensburg.md).` |
| **4. Standard-Callouts prüfen** | Wiederkehrende Begriffserklärungen (z. B. Glossar-Hinweise) sollten nicht auf 5 Seiten als Zitatkasten kopiert werden, sondern auf die übergeordnete Wegweiser- oder Architekturseite verweisen. |
| **5. Transparenzhinweis erhalten** | Auch nach der Entflechtung muss der Hinweis gemäß Art. 50 EU AI Act oben und unten erhalten bleiben. |

---

## 4. Berichtsformat

Der Agent dokumentiert die Prüfung in folgendem Tabellenformat:

### Übersicht der Fundstellen

| Nr. | Ähnlichkeit | Seite A (Hauptquelle) | Seite B (Nebenseite) | Betroffener Inhalt / Thema | Empfohlene Maßnahme |
|---|---|---|---|---|---|
| 1 | 100 % | `src/hauptthema.md:25` | `src/nebenthema.md:40` | Gleicher Absatz zu ... | Absatz auf Nebenseite durch Querverweis auf Hauptseite ersetzen |

### Konkreter Korrekturvorschlag (Diff-Muster)

```markdown
### Vorher (auf Nebenseite):
Peter Rantzau ließ zwischen 1585 und 1595 das Schloss errichten. Es ist ein dreiflügeliger Bau mit vier Ecktürmen im Stil der Renaissance... [5 Zeilen Detailtext]

### Nachher (auf Nebenseite):
Peter Rantzau ließ das Schloss ab 1585 errichten; Einzelheiten zur Architektur und Geschichte des Baus beschreibt das Kapitel [Schloss Ahrensburg](schloss-ahrensburg.md).
```

---

## 5. Abgrenzung zu anderen Skills

- **`/urheberrecht-pruefung`**: Prüft gegen **externe** Quellen (Fremdplagiate, Wikipedia-Lizenzbedingungen, UrhG).
- **`/urheberrechtliche-fachpruefung`**: Prüft die lückenlose **Rechtekette** und den Nachweis für Veröffentlichungen.
- **`/duplicate-content-pruefung`**: Prüft **interne Redundanzen** innerhalb des eigenen Wiki-Bestands und optimiert Linkstruktur und Textökonomie.
