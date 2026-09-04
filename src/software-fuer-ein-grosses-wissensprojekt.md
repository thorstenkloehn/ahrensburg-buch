# Software für ein großes Wissensprojekt

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Dieses Wiki über Ahrensburg soll langfristig sehr groß werden – viele tausend
Artikel, geschrieben von Menschen und künstlicher Intelligenz (KI) gemeinsam
(siehe [Co-Wiki: Mensch & KI](co-wiki.md)). Für so ein Projekt muss man am Anfang
eine wichtige Frage beantworten: **Mit welchem Programm sammelt und verwaltet man
das ganze Wissen?** Welche Grundkonzepte hinter dem Speichern und Suchen stecken,
erklärt [Wissen speichern](wissen-speichern.md).

Diese Seite erklärt, worauf es dabei ankommt. Die drei folgenden Seiten
vergleichen dann die konkreten Programme:

- [Wiki-Programme im Vergleich](wikis-im-vergleich.md) – z. B. MediaWiki (das
  Programm hinter Wikipedia), XWiki, Wiki.js, BookStack, DokuWiki.
- [CMS im Vergleich](cms-im-vergleich.md) – Programme zum Betreiben von Websites,
  z. B. WordPress, Drupal, TYPO3, dazu **Headless**-CMS wie Strapi und Directus
  („headless" heißt „kopflos": das Programm verwaltet nur die Inhalte, nicht das
  fertige Aussehen) sowie das datei-basierte Grav.
- [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md) – Programme,
  die aus einfachen Textdateien ein Buch oder eine Website bauen, z. B. mdBook
  (das nutzt dieses Wiki), MkDocs, Docusaurus, Hugo.

Für einen selbstgebauten Anwendungs-Server – wenn also ein Projekt seinen eigenen
Internet-Dienst programmieren würde – sind die verfügbaren Programmiersprachen und
Webframeworks zentral; ein Überblick dazu steht auf der Seite
[Webframeworks im Vergleich](webframeworks-im-vergleich.md).

## Kurz erklärt: Wiki, CMS, Doku-Generator

Alle drei Arten von Programmen helfen dabei, Texte im Internet zu
veröffentlichen. Sie sind aber für unterschiedliche Zwecke gebaut.

| Art | Wofür gemacht | Bild dazu |
|---|---|---|
| **Wiki** | Viele Menschen schreiben gemeinsam an einem großen Nachschlagewerk. Jeder darf Seiten anlegen und ändern, jede Änderung wird gespeichert. | Ein öffentliches Notizbuch, in das alle hineinschreiben dürfen. |
| **CMS** (Redaktionssystem, englisch *Content-Management-System*) | Eine Redaktion pflegt eine Website mit Artikeln, Bildern, Menüs und festem Aussehen. Wenige Leute schreiben, viele lesen. | Eine Zeitungsredaktion mit fester Ausgabe. |
| **Doku-Generator** | Aus einfachen Textdateien (im Notizformat *Markdown*) wird automatisch ein sauberes Online-Buch. Die Texte liegen als Dateien, nicht in einer Datenbank. | Eine Druckmaschine: vorne Zettel rein, hinten fertiges Buch raus. |

Dieses Wiki nutzt heute einen Doku-Generator namens **mdBook**. Ob das auf Dauer
für zehntausende Artikel reicht, ist genau die Frage, um die es hier geht.

## Was dieses Projekt vom Programm verlangt

Die folgende Liste ist der Maßstab. Jedes Programm auf den Vergleichsseiten wird
an diesen Punkten gemessen.

### 1. Sehr viele Artikel verwalten

Das Ziel sind **mehr als 10.000 Artikel**, später gern noch viel mehr. Das
Programm muss so viele Seiten schnell anzeigen, durchsuchbar halten und im
Bearbeiten flüssig bleiben. Manche Programme sind für ein paar hundert Seiten
gedacht und werden dann langsam.

### 2. Offen und kostenlos (Open Source)

*Open Source* heißt: Der Bauplan des Programms (der Quelltext) ist öffentlich.
Jeder darf das Programm gratis benutzen, verändern und weitergeben. Wichtig, weil
das Projekt niemandem gehören soll und nicht von einer Firma abhängig sein darf,
die es später abschaltet oder teuer macht.

### 3. Keine persönlichen Daten (PII-frei)

*PII* steht für „persönlich identifizierbare Informationen" – also Namen,
E-Mail-Adressen, Zugangsdaten von Nutzern. Die **Inhalte** des Wikis sollen
komplett frei von solchen Nutzerdaten sein. So kann jeder den gesamten Text
herunterladen, ohne dass Datenschutz-Probleme entstehen. Konten und Passwörter
der Autorinnen und Autoren bleiben getrennt davon und werden nicht mitgegeben.

### 4. Datenbank-neutrale Sicherungsdatei

Das komplette Wissen soll sich in **eine einzige Datei** exportieren lassen, die
jeder öffnen und weiterverwenden kann – zum Beispiel `ahrensburg.xml`,
`ahrensburg.json` oder `ahrensburg.yaml`. „Datenbank-neutral" bedeutet: Die Datei
funktioniert auch ohne genau das Programm, das sie erzeugt hat. Sie ist kein
verschlüsselter Klumpen, sondern lesbarer Text in einem verbreiteten Format.

- **XML, JSON und YAML** sind drei solche Textformate. Sie schreiben Daten so
  auf, dass sowohl Menschen als auch Programme sie verstehen. XML nutzt
  spitze Klammern, sogenannte Tags (`<titel>…</titel>`); JSON und YAML sind
  kompakter.
- Mit so einer Datei kann jemand das Wissen auf einer anderen Website, in einem
  anderen Programm oder in einem gedruckten Buch weiterverwenden.

### 5. Speicherort: Datenbank oder Dateien

Es gibt zwei Wege, wie ein Programm die Texte ablegt:

| Weg | Wie es funktioniert | Vorteil | Nachteil |
|---|---|---|---|
| **Datenbank** (oft *PostgreSQL* – eine bekannte, kostenlose Datenbank) | Alle Texte stecken in einer Datenbank, einer Art riesiger sortierter Tabelle. | Schnell auch bei sehr vielen Seiten; viele Leute können gleichzeitig schreiben. | Man braucht einen laufenden Datenbank-Server; Sicherung ist aufwendiger. |
| **Dateisystem** (jede Seite eine Datei) | Jede Seite liegt als einzelne Textdatei in einem Ordner. | Einfach zu sichern, zu kopieren, per Versionsverwaltung *Git* zu verfolgen. | Wird bei zehntausenden Dateien und mehreren gleichzeitigen Autoren unübersichtlich und langsam. |

Für dieses Projekt wäre **PostgreSQL oder ein sauberes Dateisystem** in Ordnung –
solange Punkt 4 (die Export-Datei) erfüllt ist.

### 6. Reifegrad und aktive Entwicklung

„Reif" heißt: Das Programm gibt es seit vielen Jahren, es läuft stabil, es wird
von großen Organisationen im Alltag eingesetzt, und Sicherheitslücken werden
schnell geschlossen. Eine **große, aktive Entwicklergemeinschaft** ist wichtig,
damit das Programm auch in zehn Jahren noch gepflegt wird.

### 7. Zugang für KI-Werkzeuge (Schnittstelle / REST-API)

Damit KI-Programme wie **Claude Code**, **Codex CLI**, **Gemini CLI** oder
**GitHub Copilot** beim Schreiben helfen können, müssen sie an die Texte
herankommen. Am besten geht das über

- eine **Schnittstelle** (englisch *API*, meist *REST-API* oder *GraphQL*) – ein
  standardisierter Weg, über den andere Programme Seiten lesen und ändern dürfen,
  oder
- **einfache Textdateien im Ordner**, die ein KI-Werkzeug direkt öffnen kann (so
  arbeitet dieses Wiki heute).

## Sonderfall: LLM-Wiki / Co-Wiki

Es gibt eine neue Gruppe von Wissenssystemen, die von Anfang an für die
Zusammenarbeit mit KI gedacht sind. Man nennt sie **LLM-Wiki** oder **Co-Wiki**
(*LLM* = großes Sprachmodell, die Technik hinter Chat-KI). Kennzeichen:

- Die Inhalte sind kleine, klar benannte Markdown-Dateien – gut für Menschen
  **und** für die KI lesbar. Oft tragen sie ein paar **Kopfzeilen** (auch
  *Frontmatter* genannt: einige Zeilen am Dateianfang mit Titel,
  Kurzbeschreibung und Schlagwörtern).
- Eine Technik namens **RAG** (etwa: „Nachschlagen vor dem Antworten") lässt die
  KI erst die echten Notizen durchsuchen und dann daraus schreiben, statt sich
  etwas auszudenken.
- Dieses Wiki folgt diesem Modell: Markdown-Dateien, KI-lesbar, mit menschlicher
  Redaktion. Nur die technischen Dokumentationsseiten im Ordner `openwiki/`
  tragen ausführliche Kopfzeilen, die Ahrensburg-Artikel selbst nicht. Details in
  [Co-Wiki: Mensch & KI](co-wiki.md). Ausführlich werden die LLM-Grundlagen und
  Andrej Karpathys Muster zur Wissensverwaltung auf der Seite [LLM Wiki](llm-wiki.md)
  erklärt.

## Was ist mit „Vibe Coding"?

*Vibe Coding* ist ein Begriff aus der Softwareentwicklung: Man beschreibt einer
KI in normaler Sprache, was man haben will, und lässt sie den Code schreiben,
ohne jede Zeile selbst zu prüfen. Übertragen auf das Schreiben von Texten heißt
das: die KI formuliert, der Mensch nickt nur ab. Für schnelle Versuche ist das
praktisch. Für ein Wissensprojekt, das
richtig sein muss, ist es **allein nicht genug**: Jeder von der KI geschriebene
Text muss von einem Menschen auf Fakten geprüft und freigegeben werden
(*Human-in-the-Loop*, „der Mensch bleibt in der Schleife"). Die KI darf also
kräftig zuarbeiten – die letzte Entscheidung trifft immer ein Mensch.

## Kurzfazit

- **Reine Doku-Generatoren** (wie heute mdBook) sind einfach und robust, stoßen
  aber bei zehntausenden Seiten und vielen gleichzeitigen Autoren an Grenzen.
- **Wiki-Programme** sind für genau diesen Zweck gebaut. Für dieses Projekt sind
  vor allem **XWiki**, **MediaWiki** und **Wiki.js** interessant, weil sie viele
  Seiten, eine Schnittstelle und einen Export in ein offenes, datenbank-neutrales
  Format bieten (XML bei MediaWiki und XWiki, Markdown-Dateien per Git bei
  Wiki.js).
- **CMS** sind eher für klassische Websites gedacht; datei-basierte Flat-File-CMS
  wie **Grav** liegen nah am heutigen Aufbau.
- Egal welches Programm: Ausschlaggebend bleiben zwei Dinge. Erstens ein
  **Export in ein offenes, datenbank-neutrales Format**, dessen Inhalte keine
  E-Mail-Adressen oder Passwörter enthalten. Zweitens eine **große, aktive
  Entwicklergemeinschaft**.

Die Einzelheiten stehen auf den drei Vergleichsseiten. Wie diese Programme in
die größere Landschaft von Wissenssystemen passen – bis hinauf zu Beständen von
Millionen Artikeln und zur Suche nach Bedeutung –, zeigt die Seite
[Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md).

## Fachwörter kurz erklärt

Diese Begriffe tauchen auf den Vergleichsseiten immer wieder auf.

| Wort | Was es bedeutet |
|---|---|
| **Open Source** | Der Bauplan (Quelltext) des Programms ist öffentlich; jeder darf es gratis nutzen, ändern und weitergeben. |
| **Schnittstelle** (englisch *API*) | Ein fester Weg, über den ein Programm einem anderen Programm Daten gibt oder abnimmt. |
| **REST-API** | Die heute verbreitetste Art solcher Schnittstellen: Andere Programme rufen über Web-Adressen einzelne Seiten ab oder ändern sie. |
| **GraphQL** | Eine neuere Schnittstellen-Art; das fragende Programm sagt genau, welche Angaben es haben will, und bekommt nur die. |
| **Datenbank** | Ein Programm, das große Mengen Daten sortiert speichert und schnell durchsuchbar hält. **PostgreSQL** ist eine bekannte, kostenlose Datenbank. |
| **XML / JSON / YAML** | Drei verbreitete Textformate für Daten. XML nutzt spitze Klammern (Tags), JSON und YAML sind kompakter; alle sind für Menschen und Programme lesbar. |
| **Markdown** | Ein einfaches Notizformat: normaler Text mit ein paar Zeichen für Überschriften, Fettschrift und Listen. |
| **Git** | Eine „Zeitmaschine" für Dateien: Sie merkt sich jede gespeicherte Änderung, man kann jederzeit zurück. |
| **Node.js** | Eine Umgebung, um JavaScript-Programme außerhalb des Webbrowsers zu nutzen – auf Servern oder als Werkzeuge. |
| **MCP** (Model Context Protocol) | Ein einheitlicher, geregelter Weg, über den KI-Programme auf Dateien und Werkzeuge zugreifen. |
| **RAG** | „Erst nachschlagen, dann antworten": Die KI durchsucht echte Notizen, bevor sie einen Text schreibt. |

## Quellen

- [WikiMatrix – Vergleich von Wiki-Programmen](https://www.wikimatrix.org/compare/bookstack+wiki-js+dokuwiki+mediawiki+xwiki+wackowiki)
- [Wiki.js – Git-Speicher (Dokumentation)](https://docs.requarks.io/storage/git)
- [MediaWiki – Handbuch: PostgreSQL](https://www.mediawiki.org/wiki/Manual:PostgreSQL)
- [MediaWiki – Hilfe: Export](https://www.mediawiki.org/wiki/Help:Export)
- [XWiki.org – Lizenz](https://www.xwiki.org/xwiki/bin/view/Main/License)
- [BookStack – Inhalte exportieren und importieren](https://www.bookstackapp.com/docs/user/export-import/)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
