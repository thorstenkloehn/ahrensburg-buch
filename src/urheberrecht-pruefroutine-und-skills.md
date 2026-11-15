# Anleitung: Urheberrecht prüfen – Intervalle, Workflow und Skills

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

In einem kollaborativen Wissensprojekt wie dem Ahrensburg-Wiki, in dem Menschen und KI-Agenten gemeinsam recherchieren, entwerfen und aktualisieren (siehe [Co-Wiki](co-wiki.md)), ist die rechtliche Absicherung von Inhalten eine fortlaufende Aufgabe. Um Urheberrechtsverletzungen, unvollständige Lizenzangaben oder unbelegte Textübernahmen zuverlässig zu verhindern, folgt die Redaktion einer festen Prüfroutine mit zwei spezialisierten KI-Skills.

Diese Anleitung erklärt, **wie oft** geprüft werden soll, **welche Skill** in welcher Phase zum Einsatz kommt und wie der Prüfablauf Schritt für Schritt funktioniert.

---

## Die Prüf- und Redaktions-Skills im Überblick

Für die rechtliche, textliche und technische Qualitätssicherung stehen im Repository acht spezialisierte KI-Skills (sowie ein Co-Wiki-Grundlagen-Skill) zur Verfügung:

### 1. Rechtliche & Textliche Prüf-Skills

| Kriterium | Skill: `/urheberrecht-pruefung` | Skill: `/urheberrechtliche-fachpruefung` | Skill: `/duplicate-content-pruefung` | Skill: `/dsgvo-und-persoenlichkeitsrecht` |
|---|---|---|---|---|
| **Hauptzweck** | Schnelles Screening, Verdachtsliste, Erkennung von formalen Mängeln und direkte Textbereinigung. | Vertiefte redaktionelle Rechteprüfung, vollständiger Primärquellenabgleich, Nachweis der Rechtekette. | Interne Redundanzen und Textdopplungen aufspüren; Single-Source-of-Truth und Querverweise etablieren. | Prüfung auf personenbezogene Daten Lebender (DSGVO), Äußerungsrecht bei lokalen Betrieben und Pflichtseiten. |
| **Prüftiefe** | Screening nach Zitaten, Wikipedia-Bausteinen, ungenauen Pauschalformulierungen und Bildverweisen. | Vollständiges Seiteninventar mit Prüfsummen (SHA-256), Einzelfallmatrix und Schrankenprüfung (§§ 2, 5, 23, 51, 87a UrhG). | Absatzweiser Ähnlichkeitsabgleich (`scripts/find_duplicate_content.py`, Jaccard ≥ 50 %). | Scan nach privaten Kontaktdaten, Klarnamen Nicht-Öffentlicher und werblichen Superlativen. |
| **Ausgabe** | Arbeitsbericht mit Fundstellen, Schweregraden (Niedrig/Mittel/Hoch) und sofortigen Korrekturen. | Förmlicher Prüfbericht unter `docs/urheberrechtliche-fachpruefung-JJJJ-MM-TT.md` mit Veröffentlichungsempfehlung. | Analysebericht mit Dopplungs-Paaren, Bestimmung der Hauptseite und Entflechtungs-Diffs. | Risikobericht (DSGVO / APR / UWG) mit Empfehlungen zur Neutralisierung oder Anonymisierung. |
| **Typischer Einsatz** | Routine-Check vor dem Veröffentlichen und bei einzelnen Textüberarbeitungen. | Periodisches Gesamtaudit und Revisionsprüfung vor größeren Meilensteinen. | Redaktionelle Bereinigung vor Deploys zur Vermeidung von SEO-Kannibalisierung. | Bei Artikeln über Vereine, Gastronomie, Praxen, Unternehmen und Persönlichkeiten. |

### 2. Technische & Redaktionelle Workflow-Skills

| Skill | Automatisierte Aufgabe & Skript-Unterstützung | Wann einsetzen? |
|---|---|---|
| **`/wiki-konventions-check`** | Führt `scripts/check_wiki_conventions.py` aus: Prüft `SUMMARY.md`-Vollständigkeit, EU-AI-Act-Transparenzhinweise (oben/unten), interne Links/Anker, Stormarn-Lexikon-Zusatz (`© Kreisarchiv Stormarn`) und Wikipedia-Blöcke. | Vor jedem Commit oder Pull Request. |
| **`/deploy-und-sync`** | Synchronisiert den Mirror (`.claude/` → `.agents/`), prüft `src/openwiki/` auf Drift, führt `mdbook build` sowie den CNAME-only-Diff-Check gegen `origin/gh-pages` aus. | Vor und nach jedem Web-Deploy (`npm run ver`). |
| **`/raw-zu-artikel`** | Steuert die 6-stufige Multi-Agenten-Redaktionspipeline (`forscher` → `architekt` → `schreiber` → `faktenchecker` + `lektor` → `verlinker`) für menschliche Rohentwürfe unter `raw/<thema>.md`. | Wenn ein neuer Rohentwurf in `raw/` ausgearbeitet werden soll. |
| **`/aktualitaet-und-fakten-check`** | Scannt bestehende Artikel auf veraltende Angaben („aktuell/derzeit", Öffnungszeiten, Buslinien, Politik, vergangene Jahreszahlen) sowie tote externe Links und erstellt punktgenaue Delta-Updates. | Regelmäßige Bestandspflege oder bei lokalen Änderungen in Ahrensburg. |

---

## Das 3-Stufen-Modell: Wie oft soll geprüft werden?

Die Prüfhäufigkeit richtet sich nach dem Arbeitsstand im Redaktionszyklus:

```
[Stufe 1: Autor & KI] ---> [Stufe 2: Vor-Veröffentlichung] ---> [Stufe 3: Periodisches Audit]
 Bei jedem neuen Text        Vor jedem Web-Deploy (Push)           Alle 3 bis 6 Monate
 Selbstcheck & Herkunft      /urheberrecht-pruefung               /urheberrechtliche-fachpruefung
```

### Stufe 1: Laufend bei jeder Inhaltsänderung (Selbstcheck)

Jedes Mal, wenn ein neuer Artikel entworfen (z. B. aus einer Rohfassung unter `raw/`) oder eine bestehende Seite erweitert wird:

- **Herkunftsdeklaration:** Stammen Textteile oder Gliederungen aus der Wikipedia?  
  *(Sofort den standardisierten Attribution-Block gemäß [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de) mit Link auf den Artikel, Lizenz und Bearbeitungshinweis setzen).*
- **Hinreichender Abstand ([§ 23 UrhG](https://www.gesetze-im-internet.de/urhg/__23.html)):** Fremde Regionalquellen (Broschüren, städtische Webseiten, Vereinsberichte) nur als Faktenbasis nutzen – niemals Wortketten oder Satzbau übernehmen.
- **Echte Zitate ([§ 51 UrhG](https://www.gesetze-im-internet.de/urhg/__51.html)):** Wörtliche Zitate nur ausnahmsweise als Beleg für Werturteile oder historische Aussagen verwenden, immer in Anführungszeichen setzen und mit genauer Primärquelle nachweisen.

### Stufe 2: Vor jeder Veröffentlichung / jedem Deploy (Screening)

Bevor Änderungen per `npm run ver` auf die öffentliche Website (`gh-pages`) übertragen werden:

- **Befehl / Slash-Command:** `/urheberrecht-pruefung`
- **Aufgabe der Skill:**
  - Durchsucht alle geänderten oder neu hinzugefügten Dateien im `src/`-Ordner.
  - Prüft, ob alle Wikipedia-Abschnitte vollständig sind und keine unbegründeten Pauschalfreigaben (z. B. „Text ist frei kopierbar“) enthalten sind.
  - Sucht nach versehentlich eingebetteten Bildern (`![]()`), für die keine gesonderten Bildrechte nachgewiesen sind.
- **Korrektur:** Auffällige Passagen werden direkt redaktionell neutralisiert oder präzisiert.

### Stufe 3: Periodisch alle 3 bis 6 Monate (Vollständige Fachprüfung)

In regelmäßigen Abständen sowie vor großen Buch-Veröffentlichungen:

- **Befehl / Slash-Command:** `/urheberrechtliche-fachpruefung`
- **Aufgabe der Skill:**
  - Erstellt ein lückenloses Inventar aller Seiten inklusive SHA-256-Dateihashes.
  - Gleicht die Inhalte systematisch gegen bekannte Primärquellen und Schutzgesetze ab.
  - Prüft die Aktualität und Erreichbarkeit aller verlinkten Lizenz- und Quellennachweise.
  - Speichert das datierte Audit als Nachweis redaktioneller Sorgfalt außerhalb des Buchs unter `docs/urheberrechtliche-fachpruefung-JJJJ-MM-TT.md`.
  - Spricht eine begründete Veröffentlichungsempfehlung nach dem vorgegebenen Entscheidungsraster aus.

---

## Welches Sprachmodell (LLM) soll man am besten nutzen?

Die Wahl des richtigen Sprachmodells hat erheblichen Einfluss auf die Qualität, Zuverlässigkeit und Kosten der Prüfung. Nicht jede Prüfaufgabe erfordert das teuerste Modell – aber komplexe juristische Abwägungen scheitern oft an zu kleinen Modellen.

### 1. Das gestufte Modellkonzept (Tiered Selection)

In der Redaktionspraxis empfiehlt sich eine Aufteilung in zwei aktuelle Modellklassen (Stand Ende 2026):

* **Denkstarke Frontier- & Reasoning-Modelle (`Fable` / `Opus 5.5` / `Gemini 4 Argon & Carbon` / `GPT-6 Astra & Sol`):**  
  Für vertiefte Textanalysen, Schutzschrankenprüfung (§ 23 vs. § 2 UrhG) und das Verfassen des formellen Fachberichts. Sie verfügen über eingebautes adaptives Reasoning (Deep Thinking), erfassen feine semantische Nuancen, erkennen versteckte Paraphrasen und neigen nicht zu voreiligen Pauschalentwarnungen.
* **Schnelle, token-effiziente Ausführungs- & Subagenten-Modelle (`Sonnet 5.5` / `Haiku 5.5` / `Gemini 4 Hydrogen & 3.8 Flash` / `GPT-6 Luna`):**  
  Für das regelmäßige Vorab-Screening, das Auffinden formaler Mängel (fehlender Wikipedia-Block, verwaiste Anführungszeichen) und die schnelle Ausführung automatisierter Prüfskripte für Duplicate Content.

---

### 2. Aktuelle Modell-Matrix nach Prüfaufgabe (Generation Ende 2026)

| Prüfaufgabe & Skill | Empfohlene Modellklasse | Aktuelle Top-Modelle (Stand Ende 2026) | Warum dieses Modell? |
|---|---|---|---|
| **Vertiefte Fachprüfung**<br>`/urheberrechtliche-fachpruefung` | **Frontier / Deep Reasoning** | **Anthropic:** Claude Fable 5.2 / Claude Opus 5.5<br>**Google:** Gemini 4 Carbon / Gemini 4 Argon<br>**OpenAI:** GPT-6 Astra / GPT-6.1 Sol | Höchste Urteilskraft durch adaptives Denken; trennt präzise zwischen gemeinfreien Fakten und geschützter Sprachgestaltung ([§ 23 UrhG](https://www.gesetze-im-internet.de/urhg/__23.html)); erstellt fundierte, konsistente Prüfberichte. |
| **Ganzheitlicher Repository-Scan**<br>(alle 65+ Seiten gleichzeitig) | **1M+ Unified Context** | **Google:** Gemini 4 Argon / Carbon (1M Kontext)<br>**Anthropic:** Claude Opus 5.5 / Sonnet 5.5 (1M Kontext) | Hält das gesamte `src/`-Verzeichnis samt Primärquellen, Lizenztexten und Gesetzen in einem einzigen 1-Millionen-Token-Kontextfenster – ohne Informationsverlust. |
| **Routine-Screening vor Deploy**<br>`/urheberrecht-pruefung` | **Balanced Workhorse** | **Anthropic:** Claude Sonnet 5.5<br>**Google:** Gemini 4 Hydrogen / Gemini 3.8 Flash<br>**OpenAI:** GPT-6.1 Sol / GPT-6 Luna | Optimales Verhältnis aus Geschwindigkeit, Kosten und Textverständnis; findet unvollständige Lizenzblöcke oder unzulässige Pauschalbehauptungen in Sekunden. |
| **Interne Textdopplungen**<br>`/duplicate-content-pruefung` | **High-Speed / Subagent** | **Google:** Gemini 3.8 Flash / Gemini 4 Hydrogen<br>**Anthropic:** Claude Haiku 5.5<br>**OpenAI:** GPT-6 Luna | Extrem schnelle Skriptausführung und Datenextraktion; verarbeitet Zeilennummern präzise und verdichtet redundante Passagen zu schlanken Querverweisen. |

---

### 3. Überblick der aktuellen Hersteller-Generationen (2026)

* **Google DeepMind (Gemini 4 & 3.8):**
  * **Gemini 4 Carbon & Gemini 4 Argon:** Die Flaggschiff-Modelle für komplexe Mehr-Schritt-Analysen, tiefe Dokumentenprüfung und lange Begründungsketten.
  * **Gemini 4 Hydrogen & Gemini 3.8 Flash:** Hocheffiziente Ausführungsmodelle mit einstellbarer Denktiefe (Thinking-Level) – ideal für schnelle Agenten-Durchläufe und Subagenten.
* **Anthropic (Claude 5-Serie):**
  * **Claude Fable 5.2 & Claude Opus 5.5:** Die Spitzenmodelle für anspruchsvolle Wissensarbeit und komplexe juristisch-redaktionelle Abgleiche (durchgängig mit 1M-Token-Kontext und 128K Output).
  * **Claude Sonnet 5.5 & Claude Haiku 5.5:** Schnelle Alltags- und Subagenten-Modelle für Vorab-Screenings und Lektoratsläufe.
* **OpenAI (GPT-6-Serie):**
  * **GPT-6 Astra & GPT-6.1 Sol:** Haben die frühere GPT-5- und o3/o4-Generation abgelöst und vereinen tiefes eingebettetes Reasoning mit zuverlässiger Werkzeugnutzung.
  * **GPT-6 Luna:** Die schnelle, kostenschonende Variante für Routine-Prüfungen.

---

### 4. Wichtige Konfigurationen für die Prüfung

Unabhängig vom gewählten Modell sollten folgende Einstellungen beachtet werden:

1. **Temperatur niedrig ansetzen (0.0 bis 0.2):**  
   Rechtliche Prüfungen erfordern maximale Sachlichkeit und Wiederholbarkeit. Eine niedrige Temperatur minimiert kreative Ausschmückungen und Halluzinationen.
2. **Im Zweifel „Verdacht“ statt falscher Entwarnung:**  
   Das Modell sollte instruiert sein, unklare Passagen als *„nicht abschließend geklärt / Verdacht“* zu markieren, anstatt bei fehlenden Quellen vorschnell Freigaben zu erteilen.
3. **Menschliche Endabnahme (Human-in-the-Loop):**  
   Selbst das beste Sprachmodell liefert lediglich eine redaktionelle Entscheidungshilfe. Die Letztentscheidung über die Veröffentlichung verbleibt immer beim Menschen.

---

## Praktische Schritt-für-Schritt-Anleitung

Wenn Sie als Autorin oder Redakteur einen Beitrag bearbeiten oder prüfen lassen möchten, gehen Sie wie folgt vor:

### Schritt 1: Text erstellen oder Rohfassung ausarbeiten
Schreiben Sie Ihren Textentwurf (idealerweise zunächst in `raw/<thema>.md`). Achten Sie darauf, Zahlen, Daten und Fakten eigenständig in eigenen Worten zusammenzufassen.

### Schritt 2: Quellenabschnitt prüfen
Enthält der Artikel Inhalte aus freien Quellen, ergänzen Sie am Ende des Artikels (vor dem Transparenzhinweis) den entsprechenden Herkunftsblock:
```markdown
## Wikipedia als Quelle

Teile dieses Artikels wurden aus der deutschsprachigen Wikipedia übernommen und für dieses Wiki bearbeitet (gekürzt, neu gegliedert und sprachlich überarbeitet). Autoren der Vorlagen jeweils laut Versionsgeschichte des jeweiligen Artikels; die Ursprungstexte stehen unter [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de), diese Seite steht unter derselben Lizenz.

- [Originalartikel](https://de.wikipedia.org/wiki/...)
```

### Schritt 3: Screening ausführen
Rufen Sie im Agenten-Chat den Befehl auf:
```text
/urheberrecht-pruefung Prüfe die neu bearbeiteten Seiten
```
Der Agent analysiert die Änderungen und behebt eventuelle Zitat- oder Lizenzunschärfen direkt im Text.

### Schritt 4: Gesamtfreigabe vorbereiten
Vor dem nächsten Release starten Sie die Fachprüfung:
```text
/urheberrechtliche-fachpruefung Prüfe das gesamte Wiki
```
Prüfen Sie das Ergebnis im generierten Bericht unter `docs/urheberrechtliche-fachpruefung-JJJJ-MM-TT.md`. Lautet das Fazit *„Redaktionell zur Veröffentlichung empfohlen“*, liegt die redaktionelle Grundlage für die Veröffentlichung vor.

### Schritt 5: Menschliche Freigabe (Human-in-the-Loop)
Gemäß den Co-Wiki-Regeln trifft immer der **Mensch** die finale Veröffentlichungsentscheidung. Nach Ihrer Freigabe führen Sie den Build und das Deployment durch:
```bash
mdbook build
npm run ver
```

---

## Wichtige rechtliche Grundsätze auf einen Blick

- **Reine Fakten sind gemeinfrei ([§ 2 Abs. 2 UrhG](https://www.gesetze-im-internet.de/urhg/__2.html)):** Öffnungszeiten, historische Jahreszahlen, Einwohnerstatistiken oder Straßennamen genießen keinen Urheberrechtsschutz. Geschützt ist erst die individuelle sprachliche Gestaltung.
- **Amtliche Werke ([§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html)):** Amtliche Satzungstexte und Beschlüsse sind gemeinfrei. Webseiten, Fotos oder Broschüren von Behörden sind jedoch *nicht* automatisch gemeinfrei!
- **Share-Alike-Pflicht:** Wer Inhalte unter CC BY-SA 4.0 nutzt, muss das daraus entstandene Werk zwingend wieder unter derselben Lizenz weitergeben.
- **Transparenz:** Nach Art. 50 des EU AI Act werden alle mit KI-Unterstützung erstellten Seiten mit dem entsprechenden Hinweistext gekennzeichnet.
- **Keine Rechtsberatung:** Diese Prüfwerkzeuge dienen der redaktionellen Qualitätssicherung; sie ersetzen im Streitfall keine anwaltliche Begutachtung.

---

## Verwandte Themen

- [Urheberrecht und Duplicate Content](urheberrecht-und-duplicate-content.md)
- [Co-Wiki: Mensch & KI](co-wiki.md)
- [Neue Artikel erstellen](neue-artikel-erstellen.md)
- [LLM Wiki](llm-wiki.md)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
