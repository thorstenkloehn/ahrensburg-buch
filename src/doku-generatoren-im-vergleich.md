# Doku-Generatoren im Vergleich

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Ein **Doku-Generator** ist eine Art Druckmaschine: Vorne steckt man einfache
Textdateien hinein – meist im Notizformat **Markdown** – und hinten kommt eine
fertige Website oder ein Online-Buch heraus. „Fertig" heißt hier **statisch**:
Die Seiten werden einmal gebaut und dann nur noch angezeigt, ganz ohne Datenbank
(englischer Sammelbegriff: *static site generator*). Innerhalb der Gruppe gibt es
zwei Zweige: **spezialisierte Dokumentations-Generatoren** (mdBook, Sphinx,
MkDocs, Antora) und **allgemeine Website-Generatoren** (Hugo, Jekyll, Zola), die
alles vom Blog bis zum Handbuch bauen.

Dieses Wiki nutzt heute den Doku-Generator **mdBook**. Diese Seite vergleicht
mdBook mit den Alternativen – an den Maßstäben aus
[Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md).

> Fachwörter wie *Markdown*, *Git*, *Open Source*, *Schnittstelle*, *MCP* oder
> *RAG* sind in
> [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md#fachwörter-kurz-erklärt)
> in einer kurzen Liste erklärt.

## Warum diese Gruppe gut zu den Projektzielen passt

Fast alle Punkte aus der Zielliste sind bei Doku-Generatoren **automatisch**
erfüllt:

- **Keine persönlichen Daten:** Es gibt keine Nutzerkonten – nur Texte.
- **Datenbank-neutrale Sicherung:** Die „Sicherungsdatei" ist der Ordner mit den
  Markdown-Dateien selbst. Jeder kann ihn kopieren, lesen und woanders
  weiterverwenden.
- **Offen und kostenlos:** Alle hier verglichenen Kandidaten sind Open Source –
  Ausnahme ist der weiter unten genannte Bezahldienst Obsidian Publish.
- **KI-Zugang:** KI-Werkzeuge wie Claude Code öffnen die Textdateien direkt – man
  braucht nicht einmal eine Schnittstelle.
- **Versionsverwaltung:** Die Dateien passen perfekt zu Git (Zeitmaschine für
  jede Änderung).

Der **Schwachpunkt** ist immer derselbe: Ab vielen tausend Seiten dauert das
Bauen länger, es gibt keine feine Rechteverwaltung, und wenn zwei Menschen
dieselbe Datei ändern, gibt es einen Konflikt, den jemand von Hand auflösen muss.

## Die Kandidaten

### mdBook – schlank und robust (heute im Einsatz)

- **Sprache:** Rust. Offene Lizenz (MPL-2.0). Damit ist das offizielle
  „Rust-Buch" gebaut.
- **Aufbau:** Eine Datei `SUMMARY.md` ist das Inhaltsverzeichnis, alles Weitere
  sind Markdown-Dateien. Eine einzige Einstellungsdatei `book.toml`.
- **Kann:** Seitenleiste, **eingebaute Volltextsuche**, mehrere Farbschemata,
  Code-Hervorhebung.
- **Kann nicht:** Mehrsprachigkeit von Haus aus, Versionsstände eines Artikels,
  freieres Website-Layout. Es ist bewusst „nur" ein Buch.
- **Für 10.000+ Seiten:** Unklar – mdBook ist für überschaubare Handbücher
  gedacht, nicht erprobt für ein Nachschlagewerk dieser Größe.

### MkDocs mit dem Design „Material"

- **Sprache:** Python. Offene Lizenzen (MkDocs BSD, Material MIT). Einige
  Zusatzfunktionen erscheinen zuerst im kostenpflichtigen „Insiders"-Programm und
  wandern nach und nach in die freie Version.
- **Kann:** Sehr gute Suche, klares Aussehen, viele Erweiterungen;
  Mehrsprachigkeit über eine Erweiterung.
- **Gemeinschaft:** Groß und aktiv. Sehr beliebt für Software-Handbücher.
- **Für 10.000+ Seiten:** Machbar; große Projekte setzen es ein.
- **Einordnung:** Der wahrscheinlich einfachste Umstieg von mdBook mit deutlich
  mehr Funktionen.

### Docusaurus

- **Sprache:** JavaScript/React, gebaut und gepflegt von der Firma Meta. Offene
  Lizenz (MIT). Weit verbreiteter Doku-Generator.
- **Kann:** **Versionsstände und Mehrsprachigkeit ab Werk**, interaktive Bausteine
  direkt im Text, große Websites mit vielen Bereichen.
- **Haken:** Schwergewichtiger Aufbau (Node.js, eine JavaScript-Umgebung),
  längere Bauzeiten, mehr zu lernen.
- **Für 10.000+ Seiten:** Ausdrücklich dafür gedacht.

### Sphinx

- **Sprache:** Python. Offene Lizenz (BSD). Der Veteran – damit ist die
  Python-Dokumentation gebaut. Die Hosting-Plattform „Read the Docs" entstand
  ursprünglich rund um Sphinx, baut heute aber auch andere Generatoren.
- **Kann:** Echte Querverweise, Stichwortverzeichnisse, **PDF-Ausgabe**.
  Versteht neben seinem eigenen Format „reStructuredText" (ein älteres
  Notizformat wie Markdown) auch Markdown selbst (über die Erweiterung MyST).
  Versionsstände (ein Umschalter zwischen Doku-Ständen) gibt es über Read the
  Docs oder eine Erweiterung, nicht im Kern.
- **Haken:** Wirkt technisch und etwas altbacken; die eigene Schreibweise ist
  gewöhnungsbedürftig.

### Antora

- **Sprache:** JavaScript. Offene Lizenz (MPL-2.0). Schreibweise: **AsciiDoc**
  (mächtiger als Markdown, aber weniger verbreitet).
- **Besonderheit:** Gebaut, um Dokumentation aus **vielen getrennten Lagern**
  zusammenzuführen und zu versionieren. Stark, wenn das Wissen später auf mehrere
  Projekte aufgeteilt wird.

### Hugo

- **Sprache:** Go. Offene Lizenz (Apache-2.0). **Höchstes Bautempo** – baut auch
  sehr große Websites in Sekunden.
- **Kann:** Alles von Blog über allgemeine Website bis Handbuch. Sehr große
  Gemeinschaft, viele Designs.
- **Haken:** Kein reiner Doku-Generator; für ein Doku-Design braucht man ein
  passendes Thema (z. B. „Docsy"). Die Vorlagensprache ist gewöhnungsbedürftig.
- **Für 10.000+ Seiten:** Von allen hier die beste Wahl bei reiner Menge und
  Bautempo.

### Weitere, kurz

| Programm | Kurzbeschreibung |
|---|---|
| **Jekyll** | Der Ruby-Klassiker für GitHub Pages (ein kostenloser Hosting-Dienst von GitHub). Wird ab vielen Seiten langsam. |
| **Zola** | Wie Hugo, aber in Rust geschrieben und mit bewusst kleinerem Funktionsumfang. Sehr schnell. |
| **VitePress** | Doku-Generator auf Basis von Vue und Vite (ein Web-Framework und sein Bau-Werkzeug). Gut für Handbücher. |
| **Starlight** | Doku-Design für das Website-System „Astro". Suche und Mehrsprachigkeit mitgeliefert. Gut für kleine bis mittlere Dokumentationen. |
| **Quartz** | Baut aus einem Obsidian-Notizbuch eine Website – mit **Rückwärts-Verweisen** (wer verlinkt auf diese Seite?). Für vernetzte Wissensgärten. |
| **Quarto** | Für wissenschaftliches Schreiben: Bücher, Websites und PDF aus einer Quelle, mit **direkt ausführbaren Code-Blöcken** (Python, R). |
| **Jupyter Book** | Verwandelt Rechen-Notizbücher in ein Online-Buch. Version 2 nutzt statt Sphinx die MyST-Engine. |

**Nicht empfehlenswert für dieses Projekt:** *Obsidian Publish* – der
Veröffentlichungs-Dienst der Notiz-App Obsidian ist kostenpflichtig und nicht
Open Source. Das Schreiben in Obsidian selbst ist kostenlos; nur zum
Veröffentlichen dann besser Quartz nehmen.

## Sonderfall: KI-kompatible Wissenssysteme (LLM-Wiki / Co-Wiki)

Die neueste Gruppe sind Wissenssysteme, die von Grund auf für die Zusammenarbeit
mit KI gebaut sind – **LLM-Wiki** (nach dem großen Sprachmodell hinter Chat-KI)
oder **Co-Wiki** genannt. Sie sind meist kein eigenes Programm, sondern ein
**Organisationsmuster**: kleine, klar benannte Markdown-Dateien, dazu eine
einheitliche KI-Andockstelle (*MCP*) und die Technik *RAG* („erst nachschlagen,
dann antworten"). Ein Doku-Generator wie mdBook baut daraus die sichtbare
Website.

Dieses Wiki folgt dem Co-Wiki-Prinzip: einfache, KI-lesbare Markdown-Dateien mit
menschlicher Redaktion. Die ausführliche Erklärung steht in
[Co-Wiki: Mensch & KI](co-wiki.md); der technische Hintergrund im
[Überblick](openwiki/overview.md) und in der [Architektur](openwiki/architecture.md).

## Vergleichstabelle

| Programm | Sprache | Schreibweise | Suche ab Werk | Mehrsprachig ab Werk | Versionsstände | Sehr viele Seiten | Gemeinschaft |
|---|---|---|---|---|---|---|---|
| **mdBook** (heute) | Rust | Markdown | Ja | Nein | Nein | Unerprobt | Mittel |
| **MkDocs + Material** | Python | Markdown | Ja (sehr gut) | Über Zusatz | Über Zusatz | Ja | Groß |
| **Docusaurus** | JavaScript | Markdown/MDX | Über Zusatz | Ja | Ja | Ja | Sehr groß |
| **Sphinx** | Python | reStructuredText / Markdown | Ja | Ja | Über Zusatz | Ja | Groß |
| **Antora** | JavaScript | AsciiDoc | Über Erweiterung | Teilweise | Ja | Ja | Mittel |
| **Hugo** | Go | Markdown | Über Thema | Ja | Über Aufbau | Ja (am schnellsten) | Sehr groß |
| **Quartz** | TypeScript | Markdown | Ja | Nein | Über Git | Mittel | Mittel |

## Empfehlung für dieses Projekt

- **Beim datei-basierten Aufbau bleiben, aber mehr Funktionen:** von mdBook zu
  **MkDocs mit Material** wechseln – ähnliche Einfachheit, deutlich bessere Suche,
  Mehrsprachigkeit und Erweiterungen.
- **Wenn Versionsstände und Mehrsprachigkeit wichtig werden:** **Docusaurus**.
- **Wenn es vor allem um schiere Menge und Bautempo geht:** **Hugo** mit einem
  Doku-Thema.
- **Wenn die starke Vernetzung der Artikel im Vordergrund steht:** in Obsidian
  schreiben und mit **Quartz** veröffentlichen.
- Sobald **viele Menschen gleichzeitig** schreiben sollen oder eine feine
  Rechteverwaltung nötig wird, ist die Grenze der Doku-Generatoren erreicht –
  dann zu den [Wiki-Programmen](wikis-im-vergleich.md) wechseln.

## Quellen

- [mdBook – offizielle Dokumentation](https://rust-lang.github.io/mdBook/)
- [Material for MkDocs – Alternativen (Vergleich)](https://squidfunk.github.io/mkdocs-material/alternatives/)
- [Docusaurus – offizielle Website](https://docusaurus.io/)
- [Sphinx – offizielle Website](https://www.sphinx-doc.org/)
- [Antora – offizielle Website](https://antora.org/)
- [Hugo – offizielle Website](https://gohugo.io/)
- [Read the Docs – Beliebte Dokumentationswerkzeuge](https://docs.readthedocs.com/platform/stable/intro/doctools.html)
- [Read the Docs bei Wikipedia (Entstehung rund um Sphinx)](https://en.wikipedia.org/wiki/Read_the_Docs)
- [Jupyter Book – offizielle Website](https://jupyterbook.org/)
- [Obsidian Publish – Preise](https://obsidian.md/publish)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
