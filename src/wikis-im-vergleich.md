# Wiki-Programme im Vergleich

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Ein **Wiki** ist ein Programm, mit dem viele Menschen gemeinsam ein großes
Nachschlagewerk schreiben. Jede Seite lässt sich von jedem ändern, und jede
Änderung wird gespeichert – man kann also jederzeit zurückspringen. Das
bekannteste Wiki ist die Wikipedia.

Diese Seite vergleicht die wichtigsten offenen Wiki-Programme an den Maßstäben
aus [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md).
Fast alle hier genannten Programme sind **Open Source** (Bauplan öffentlich,
gratis nutzbar). Die Ausnahme unter den ernsthaften Kandidaten ist Outline, das
nur „quelloffen einsehbar" ist. Confluence, das nur zum Vergleich genannt wird,
ist ebenfalls nicht quelloffen. Zu beiden mehr weiter unten.

> Fachwörter wie *Open Source*, *Schnittstelle*, *REST-API*, *GraphQL*,
> *Datenbank*, *Git* oder *Node.js* sind in
> [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md#fachwörter-kurz-erklärt)
> in einer kurzen Liste erklärt.

## Die Kandidaten kurz vorgestellt

### MediaWiki – das Programm hinter Wikipedia

- **Herkunft:** Seit 2002, geschrieben in der Sprache PHP. Betreibt Wikipedia mit
  vielen Millionen Seiten – der Beweis, dass es riesige Mengen verträgt.
- **Speicher:** Datenbank. Am besten getestet mit MySQL/MariaDB; PostgreSQL wird
  seit Version 1.7 unterstützt, gilt aber als „zweite Wahl" (weniger Leute testen
  es).
- **Sicherungsdatei:** Eingebauter **XML-Export**. Das ist das Standard-Format
  zum Weitergeben von Wiki-Inhalten. Es enthält die Seiten und ihre gesamte
  Änderungsgeschichte samt den **Benutzernamen der Autoren**, **aber keine
  Nutzerkonten, Passwörter, E-Mail-Adressen oder Bilder**. Für sehr große Wikis
  läuft ein vollständiger Export nicht über den Browser, sondern über ein
  Sicherungs-Skript (`dumpBackup.php`); das Ergebnis ist trotzdem eine offene
  XML-Datei.
- **KI-Zugang:** Umfangreiche Schnittstelle (die „Action-API" und eine neuere
  REST-API). KI-Werkzeuge können Seiten lesen und schreiben.
- **Gemeinschaft:** Sehr groß, von der Wikimedia-Stiftung getragen. Höchster
  Reifegrad.
- **Haken:** Aufwendig einzurichten und umzugestalten. Eigene Wiki-Schreibweise
  (nicht das verbreitete Notizformat Markdown). Wirkt technisch altbacken.

### XWiki – das „Baukasten-Wiki"

- **Herkunft:** Erste Versionen ab 2003/2004, Version 1.0 im Jahr 2007;
  geschrieben in Java. Wird von der Firma XWiki SAS und einer aktiven
  Gemeinschaft gepflegt, mit etwa monatlichem Erscheinungsrhythmus (Version 18.x
  im Jahr 2026).
- **Speicher:** Datenbank – **PostgreSQL**, MySQL/MariaDB und weitere werden
  gleichwertig unterstützt.
- **Sicherungsdatei:** **XAR-Export** – ein Archiv-Format speziell für XWiki
  (eine ZIP-Datei voller XML-Dateien), das sich auch über die Schnittstelle
  abrufen lässt. Inhalte sind von den Nutzerkonten getrennt.
- **KI-Zugang:** Vollständige **REST-API** zum Lesen **und** Schreiben von Seiten.
  Damit kommen Claude Code, Copilot und ähnliche Werkzeuge gut zurecht.
- **Gemeinschaft:** Kleiner als bei MediaWiki, aber stabil und seit rund zwei
  Jahrzehnten aktiv. Von Behörden und Unternehmen im Alltag eingesetzt.
- **Haken:** Sehr mächtig, dadurch komplex. Braucht mehr Arbeitsspeicher (Java).
- **Besonders:** Feine Rechteverwaltung je Seite und Bereich; man kann eigene
  strukturierte Datenblätter bauen.

### Wiki.js – das moderne, hübsche Wiki

- **Herkunft:** Geschrieben in JavaScript (Node.js, einer Umgebung für
  JavaScript-Programme auf dem Server). Zeitgemäßes Aussehen, angenehmer Editor.
- **Speicher:** Datenbank – **PostgreSQL empfohlen**, auch MySQL, MariaDB, MS SQL
  Server oder die kleine Datei-Datenbank SQLite.
- **Sicherungsdatei:** Besonders praktisch – Wiki.js kann alle Seiten
  **automatisch als Markdown-Dateien in ein Git-Lager schreiben** (Git = die
  Versionsverwaltung, die auch dieses Wiki nutzt). Damit hat man jederzeit alle
  Texte als einfache, gut lesbare Dateien außerhalb der Datenbank – ideal für
  Weitergabe und für KI-Werkzeuge.
- **KI-Zugang:** Schnittstelle über **GraphQL** (ein Abfrage-System für Daten,
  flexibler als eine REST-API, aber mit demselben Zweck). Über den Git-Ordner
  kommen KI-Werkzeuge auch direkt an die Texte.
- **Gemeinschaft:** Vorhanden, aber kleiner. **Wichtiger Haken:** Die
  Weiterentwicklung stockte länger – Version 2 wurde kaum noch verbessert,
  Version 3 blieb lange im Test. Vor einer Entscheidung den aktuellen Stand
  prüfen.

### BookStack – das aufgeräumte Team-Wiki

- **Herkunft:** PHP (mit dem Framework Laravel), sehr freie MIT-Lizenz. Wird von
  einem kleinen Kernteam sehr zuverlässig gepflegt.
- **Speicher:** Datenbank – **nur MySQL/MariaDB** (kein PostgreSQL).
- **Sicherungsdatei:** Export je Seite, Kapitel oder Buch als **Markdown**, HTML,
  PDF oder reiner Text. Ein Export des **kompletten** Wikis in **eine** Datei ist
  nicht eingebaut, lässt sich aber über die Schnittstelle nachrüsten.
- **KI-Zugang:** Saubere **REST-API**.
- **Gemeinschaft:** Klein, aber sehr aktiv und verlässlich; gute Anleitungen.
- **Struktur:** Inhalte liegen in Regalen, die Bücher enthalten; Bücher gliedern
  sich optional in Kapitel mit Seiten. Das ist einsteigerfreundlich, aber
  weniger frei als bei MediaWiki oder XWiki.
- **Haken:** Auf einige tausend Seiten ausgelegt, nicht auf Wikipedia-Größe.

### DokuWiki – das Wiki ganz ohne Datenbank

- **Herkunft:** Seit 2004, PHP, GPLv2. Sehr schlank.
- **Speicher:** **Keine Datenbank** – jede Seite ist eine einfache Textdatei im
  Ordner. Damit ist die „datenbank-neutrale Sicherung" automatisch erfüllt: Man
  kopiert einfach den Ordner.
- **Sicherungsdatei:** Der Seiten-Ordner selbst; zusätzlich Export je Seite.
- **KI-Zugang:** Fest eingebaut sind eine ältere Fernsteuer-Schnittstelle
  (XML-RPC) und seit 2024 zusätzlich eine überarbeitete, modernere (JSON-RPC).
  KI-Werkzeuge können die Textdateien auch direkt öffnen.
- **Gemeinschaft:** Groß und langlebig, viele Zusatzbausteine.
- **Haken:** Eigene Schreibweise (nicht Markdown ab Werk). Bei zehntausenden
  Dateien und vielen gleichzeitigen Autoren wird das Datei-Prinzip langsam und
  unübersichtlich.

### Neuere Alternativen: Outline und Docmost

Beide sehen zeitgemäß aus (ähnlich dem Notiz-Programm Notion) und brauchen
**PostgreSQL** sowie zusätzlich **Redis** (ein schneller Zwischenspeicher, der
häufig gebrauchte Daten bereithält). Unterschied bei der Lizenz:

- **Docmost** – echte Open-Source-Lizenz (AGPL-3.0).
- **Outline** – nur „quelloffen einsehbar" (Lizenz BSL 1.1): Man darf es
  selbst betreiben, aber nicht als eigenen Bezahldienst anbieten; erst nach einer
  Frist (für die jeweilige Version Mitte 2030) wird der Code zu Apache 2.0 und
  damit voll frei. Für dieses Projekt ist das ein Nachteil.

Beide sind noch jung und haben kleinere Gemeinschaften als MediaWiki oder XWiki.

### Nur zum Vergleich: Confluence

**Confluence** von der Firma Atlassian ist das bekannteste Firmen-Wiki, aber
**kein Open Source** und kostenpflichtig. Für dieses Projekt fällt es damit
raus – es dient hier nur als Messlatte für den Funktionsumfang.

## Vergleichstabelle

| Programm | Lizenz (offen?) | Speicher | PostgreSQL? | Export in lesbarer Form | Schnittstelle für KI | Für 10.000+ Seiten | Gemeinschaft |
|---|---|---|---|---|---|---|---|
| **MediaWiki** | Ja (GPLv2 o. später) | Datenbank | Ja (zweite Wahl) | Ja – XML-Export (mit Autor-Namen, ohne Konten/Passwörter/Bilder) | REST- und Action-API | Ja (Wikipedia-Größe) | Sehr groß |
| **XWiki** | Ja (LGPL 2.1 o. später) | Datenbank | Ja (gleichwertig) | Ja – XAR (ZIP mit XML) | Volle REST-API (lesen + schreiben) | Ja | Mittel, stabil |
| **Wiki.js** | Ja (AGPL-3.0) | Datenbank | Ja (empfohlen) | Ja – alle Seiten als Markdown per Git | GraphQL + Git-Ordner | Wahrscheinlich, kaum erprobt | Klein, Entwicklung stockte |
| **BookStack** | Ja (MIT) | Datenbank | Nein (nur MySQL) | Teilweise – je Seite/Buch, nicht das Ganze | REST-API | Bis einige tausend | Klein, sehr aktiv |
| **DokuWiki** | Ja (GPLv2) | Dateien, keine Datenbank | – | Ja – der Seiten-Ordner selbst | XML-RPC, seit 2024 JSON-RPC im Kern | Nur begrenzt | Groß, langlebig |
| **Docmost** | Ja (AGPL-3.0, EE-Zusätze) | Datenbank | Ja (Pflicht) | Export je Seite/Bereich | REST-API | Noch wenig erprobt | Klein, jung |
| **Outline** | Eingeschränkt (BSL 1.1) | Datenbank | Ja (Pflicht) | Export je Sammlung | REST-API | Wenig belegt | Mittel |

## Empfehlung für dieses Projekt

1. **XWiki** – bester Gesamtpasser: PostgreSQL gleichwertig, vollständige
   Schreib-Schnittstelle, XAR-Export, seit rund zwei Jahrzehnten stabil. Preis
   dafür: höherer Betriebsaufwand.
2. **MediaWiki** – wenn maximale Größe und die größte Gemeinschaft zählen. Der
   XML-Export (mit Autor-Namen, aber ohne Konten, Passwörter oder E-Mail-Adressen)
   passt gut zum Ziel „jeder kann alles herunterladen". Preis dafür: sperrige
   Einrichtung, keine Markdown-Texte.
3. **Wiki.js** – am angenehmsten zu bedienen und der Git-Export ist genau richtig
   für die KI-Zusammenarbeit. Nur wegen der stockenden Entwicklung mit Vorsicht;
   vorher aktuellen Stand prüfen.
4. **DokuWiki / BookStack** – gut für einen überschaubaren Anfang, aber nicht für
   das Endziel von zehntausenden Artikeln.

Wer den heutigen datei-basierten Aufbau behalten will, sollte statt eines Wikis
die [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md) ansehen.
Auch die datei-basierten Vertreter unter den [CMS](cms-im-vergleich.md) kommen
als Alternative in Frage.

## Quellen

- [WikiMatrix – Vergleich von Wiki-Programmen](https://www.wikimatrix.org/compare/bookstack+wiki-js+dokuwiki+mediawiki+xwiki+wackowiki)
- [MediaWiki – Handbuch: PostgreSQL](https://www.mediawiki.org/wiki/Manual:PostgreSQL)
- [MediaWiki – Hilfe: Export](https://www.mediawiki.org/wiki/Help:Export)
- [MediaWiki – Handbuch: XML-Dumps importieren](https://www.mediawiki.org/wiki/Manual:Importing_XML_dumps)
- [XWiki wird unter LGPL verfügbar (XWiki-Blog)](https://xwiki.com/en/Blog/XWikiAvailableUnderLGPL)
- [XWiki bei Wikipedia](https://en.wikipedia.org/wiki/XWiki)
- [DokuWiki bei Wikipedia](https://en.wikipedia.org/wiki/DokuWiki)
- [Wiki.js – Git-Speicher (Dokumentation)](https://docs.requarks.io/storage/git)
- [Wiki.js bei Wikipedia](https://en.wikipedia.org/wiki/Wiki.js)
- [BookStack – Inhalte exportieren und importieren](https://www.bookstackapp.com/docs/user/export-import/)
- [BookStack – Systemvoraussetzungen](https://www.bookstackapp.com/docs/admin/requirements/)
- [BookStack bei Wikipedia](https://en.wikipedia.org/wiki/BookStack)
- [Docmost vs. Outline (elest.io-Blog)](https://blog.elest.io/docmost-vs-outline-which-self-hosted-notion-alternative-in-2026/)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
