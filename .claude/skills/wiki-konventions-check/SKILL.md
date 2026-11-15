---
name: wiki-konventions-check
description: Prüfe alle Inhaltsseiten unter src/ automatisch auf Einhaltung der mdBook- und Co-Wiki-Konventionen – SUMMARY.md-Vollständigkeit, EU-AI-Act-Transparenzhinweis oben/unten, gültige interne Links und Anker, Wikipedia-Lizenzbaustein sowie Stormarn-Lexikon-Kennzeichnung. Kompatibel mit Codex, Antigravity (agy) und Claude Code.
---

# Wiki-Konventions-Check (Technischer Linter)

Diese Skill leitet Coding- und Redaktions-Agenten (Codex, Antigravity/agy, Claude Code) an, alle Inhaltsseiten dieses Wikis (`src/**/*.md`) schnell und deterministisch auf die formalen und technischen Konventionen aus [`CLAUDE.md`](../../../CLAUDE.md) und [`docs/agent-notes.md`](../../../docs/agent-notes.md) zu prüfen.

---

## 1. Auftrag & Prüfkriterien

Vor einem Commit oder Deploy stellt diese Skill sicher, dass keine strukturellen oder formalen Mängel in `src/` vorliegen:

1. **Inhaltsverzeichnis (`src/SUMMARY.md`):**
   - Jede Inhaltsdatei unter `src/**/*.md` muss in `src/SUMMARY.md` verlinkt sein (keine verwaisten Seiten).
   - Jeder Eintrag in `src/SUMMARY.md` muss auf eine tatsächlich existierende Datei zeigen.
   - Neue Vergleichs- und Architektur-Seiten stehen im oberen Prefix-Block vor `# Ahrensburg – Allgemeines`.
2. **Transparenzhinweis gemäß Art. 50 EU AI Act:**
   - Jede Inhaltsseite (einzige Ausnahme: `src/datenschutz.md`) muss am Seitenanfang (unter der H1 bzw. ganz oben) **und** am Seitenende exakt folgende kursive Zeile tragen:
     `*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*`
3. **Interne Markdown-Links & Anker:**
   - Alle relativen Links (`[Text](ziel.md)` oder `[Text](ziel.md#anker)`) müssen auf existierende `.md`-Dateien innerhalb von `src/` und vorhandene Überschriften-Anker zeigen.
4. **Quellen- & Lizenzkonventionen:**
   - **Stormarn-Lexikon:** Jeder Verweis auf `stormarnlexikon.de` muss den Zusatz `© Kreisarchiv Stormarn, alle Rechte vorbehalten` tragen.
   - **Wikipedia-Block:** Enthält eine Seite den Abschnitt `## Wikipedia als Quelle`, müssen der Lizenzhinweis `CC BY-SA 4.0`, der Bearbeitungshinweis und mindestens ein direkter Link auf `https://de.wikipedia.org/wiki/...` vorhanden sein.
   - **Bild-Einbettungen (`![]()`):** Werden gesondert gemeldet, damit für jedes eingebettete Bild die Lizenzkette geprüft wird.

---

## 2. Automatisierter Prüflauf (Token-schonend)

Statt alle Dateien einzeln in das Kontextfenster zu laden, führt der Agent zuerst das Linter-Skript [`scripts/check_wiki_conventions.py`](../../../scripts/check_wiki_conventions.py) aus:

```bash
python3 scripts/check_wiki_conventions.py src
```

Zusätzlich prüft der Agent kurz den mdBook-Build:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
mdbook build
```

---

## 3. Klassifizierung der Befunde

| Schweregrad | Bedeutung | Beispiele |
|---|---|---|
| 🔴 **HOCH** | Bricht Navigation oder Build | Toter interner Link, fehlende Zieldatei in `SUMMARY.md`, verwaiste `src/*.md`-Datei, Link bricht aus `src/` aus. |
| 🟡 **MITTEL** | Verletzt verbindliche Repo-Regeln | Fehlender oder abweichender EU-AI-Act-Transparenzhinweis (oben/unten), fehlender `© Kreisarchiv Stormarn`-Zusatz, unvollständiger Wikipedia-Quellenblock, ungeprüfte Bild-Einbettung. |
| 🟢 **NIEDRIG** | Redaktioneller Feinschliff | Abweichender Überschriften-Anker (`#...`), stilistische Kleinigkeiten in Linktexten. |

---

## 4. Berichtsformat & Korrektur-Workflow

1. **Skript ausführen** und Ausgabe analysieren.
2. **Gezieltes Lesen (Scoped Reading):** Nur die im Skript gemeldeten Dateien und Zeilenbereiche mit `read_file` / `view_file` öffnen.
3. **Bericht ausgeben:**

```markdown
# Prüfbericht: Wiki-Konventions-Check

**Geprüfte Dateien:** [Anzahl]
**Status `mdbook build`:** PASS / FAIL
**Befunde:** 🔴 HOCH: [X] | 🟡 MITTEL: [Y] | 🟢 NIEDRIG: [Z]

| Schweregrad | Fundstelle | Kategorie | Befund & Korrekturvorschlag |
|---|---|---|---|
| 🔴 / 🟡 / 🟢 | `src/datei.md:Zeile` | [Kategorie] | [Kurze Beschreibung + konkrete Korrektur] |
```

4. **Delta-Fix (falls vom Menschen gewünscht):** Mängel punktgenau per Edit-Tool beheben (niemals ganze Dateien neu schreiben) und `python3 scripts/check_wiki_conventions.py src` erneut bis `PASS` ausführen.
