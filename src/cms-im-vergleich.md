# CMS im Vergleich

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

**CMS** steht für *Content-Management-System*, auf Deutsch etwa
„Inhalts-Verwaltungs-System" oder Redaktionssystem. Es ist ein Programm, mit dem
eine Redaktion eine Website pflegt: Artikel schreiben, Bilder einbinden, Menüs
ordnen, das Aussehen festlegen. Anders als bei einem [Wiki](wikis-im-vergleich.md)
schreiben meist **wenige** Leute und **viele** lesen nur.

Diese Seite prüft, welche offenen CMS zu den Zielen aus
[Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)
passen. Ein CMS ist für dieses Wiki nicht die naheliegendste Wahl – aber einige
CMS arbeiten wie das heutige Wiki ohne Datenbank, nur mit einzelnen Textdateien
(Fachwort: *Flat-File*).

> Fachwörter wie *Open Source*, *Schnittstelle*, *REST-API*, *GraphQL*, *JSON*,
> *Datenbank*, *Git* oder *Node.js* sind in
> [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md#fachwörter-kurz-erklärt)
> in einer kurzen Liste erklärt.

## Drei Bauarten von CMS

| Bauart | Idee | Beispiele |
|---|---|---|
| **Klassisch (monolithisch)** | Ein großes Programm macht alles: Texte speichern, Seite gestalten, ausliefern. Inhalte stecken in einer Datenbank. | WordPress, Drupal, TYPO3, Joomla |
| **Headless** („kopflos") | Das CMS speichert und verwaltet nur die Inhalte und gibt sie über eine Schnittstelle heraus. Das Aussehen baut man getrennt. | Strapi, Directus, Payload, Ghost |
| **Flat-File / Git-basiert** | Keine Datenbank. Jede Seite ist eine Textdatei im Ordner, oft in Markdown, verfolgt mit der Versionsverwaltung Git. | Grav, Kirby, Decap, Statamic |

## Klassische CMS

### WordPress

- **Verbreitung:** Mit Abstand am größten – ein großer Teil aller Websites läuft
  damit. Riesige Gemeinschaft, unzählige Erweiterungen. PHP, Lizenz GPL
  (Version 2 oder später – gilt ebenso für Drupal und TYPO3).
- **Speicher:** Datenbank, **nur MySQL/MariaDB** (kein PostgreSQL).
- **Sicherungsdatei:** Eingebauter **WXR-Export** (kurz für „WordPress Extended
  RSS", eine XML-Datei mit Beiträgen und Seiten). Praktisch, aber Bilder und
  einige Einstellungen sind darin nicht enthalten.
- **KI-Zugang:** **REST-API** ist ab Werk dabei.
- **Haken:** Für ein Nachschlagewerk mit zehntausenden verknüpften Artikeln ist
  WordPress nicht gebaut; es glänzt bei Blogs und Firmen-Websites. Große
  Installationen brauchen sorgfältige Pflege gegen Sicherheitslücken.

### Drupal

- **Stärke:** Gebaut für **große, stark strukturierte** Websites mit viel Inhalt.
  Bei Behörden und Hochschulen für trafficstarke Installationen bewährt. PHP.
- **Speicher:** Datenbank – **MySQL/MariaDB, PostgreSQL oder SQLite**.
- **Sicherungsdatei:** Kein einzelner Standard-Export wie bei WordPress; Inhalte
  exportiert man über Zusatzbausteine (z. B. „Default Content") nach JSON (ein
  lesbares Textformat für Daten).
- **KI-Zugang:** **JSON-Schnittstelle und REST** sind im Kern enthalten.
- **Haken:** Anspruchsvoll zu lernen. Kleinere, aber sehr fachkundige
  Gemeinschaft.

### TYPO3

- **Herkunft:** Im deutschsprachigen Raum stark verbreitet, viele Behörden und
  größere Unternehmen. PHP. Sehr gute Mehrsprachigkeit.
- **Speicher:** Datenbank – MySQL/MariaDB, daneben PostgreSQL und SQLite; einige
  Erweiterungen setzen jedoch MySQL voraus.
- **Sicherungsdatei:** Eigene Export-/Import-Funktion (Format T3D bzw. XML).
- **KI-Zugang:** REST über Erweiterungen.
- **Haken:** Gilt als schwergewichtig. Für sehr große, trafficstarke
  Installationen gibt es weniger dokumentierte Referenzen als bei Drupal.

## Headless CMS

Diese Programme trennen Inhalt und Aussehen. Strapi, Directus und Payload bieten
**REST- und GraphQL-Schnittstellen** (zwei Arten von Abfrage-Schnittstellen für
Programme), Ghost nur REST – in allen Fällen gut für KI-Werkzeuge.

### Strapi

- **Grundlage:** Node.js (Laufzeitumgebung für JavaScript auf dem Server). Strapi
  hat die mit Abstand größte Gemeinschaft unter den Headless-CMS und einen
  sichtbaren Baukasten für Inhaltstypen.
- **Speicher:** PostgreSQL, MySQL/MariaDB oder SQLite.
- **Lizenz-Einschränkung:** Der Kern (Community Edition) bleibt MIT-lizenziert;
  seit Version 5 sind aber mehr Funktionen – etwa die dauerhafte
  Inhalts-Versionierung, Freigabe-Abläufe und die zentrale Anmeldung (ein Login
  für alles, englisch *Single Sign-On* / SSO) – bezahlten Plänen vorbehalten.
  Entwicklung genau beobachten.

### Directus

- Node.js, „datenbank-zuerst": Directus legt sich **über eine ganz normale
  SQL-Datenbank** – am besten PostgreSQL – und macht daraus sofort eine
  Schnittstelle. Die Daten bleiben in einfachen, selbst lesbaren Datenbank-
  Tabellen – **keine Abhängigkeit vom Programm**.
- **Lizenz-Einschränkung:** Nicht mehr voll Open Source. 2023 Wechsel von GPLv3 auf die
  „Business Source License", inzwischen die „Monospace Sustainable Core License".
  Kostenlos für kleine Organisationen (unter 5 Mio. US-Dollar Umsatz **und**
  unter 50 Beschäftigte); jede Version wird nach vier Jahren GPLv3. Für ein
  gemeinnütziges Projekt meist unkritisch, aber vorher prüfen.

### Payload

- Node.js/TypeScript, echte offene Lizenz (MIT). Aufbau über Code. 2025 von der
  Design-Firma Figma übernommen.
- **Speicher:** PostgreSQL, SQLite oder MongoDB (eine Datenbank, die Daten als
  einzelne Dokumente statt als Tabellen ablegt).
- Jünger und mit kleinerer Gemeinschaft als Strapi oder Directus.

### Ghost (Sonderfall)

- Node.js, offene Lizenz (MIT). Eigentlich für Blogs und Newsletter gemacht.
- **Bester Export der Gruppe:** eingebauter **JSON-Export** des gesamten Inhalts.
- **Speicher:** ausschließlich MySQL 8 (SQLite nur zum Entwickeln; MariaDB wird
  nicht mehr unterstützt).
- Für ein großes verknüpftes Nachschlagewerk aber zu einfach gestrickt.

## Flat-File- / Git-basierte CMS

Diese Gruppe liegt am nächsten am heutigen Aufbau dieses Wikis (Markdown-Dateien
+ Git).

### Grav

- PHP, offene Lizenz (MIT). **Keine Datenbank** – nur Markdown-Dateien im Ordner,
  damit von Natur aus datenbank-neutral und gut für Git.
- **Version 2** (stabil seit Mitte 2026) bringt eine **REST-API**, eine neue
  Verwaltungsoberfläche, ein Werkzeug für den Umstieg bestehender
  Grav-1.7/1.8-Seiten und sogar einen eigenen **MCP-Server** (*Model Context
  Protocol* – eine einheitliche Andockstelle speziell für KI-Helfer). REST-API,
  neue Oberfläche, Migrationswerkzeug und MCP-Server gehören nach Angaben des
  Grav-Blogs alle zum kostenlosen Kern.
- Mittelgroße, aktive Gemeinschaft.
- **Haken:** Bei sehr vielen Seiten und mehreren gleichzeitigen Autoren gilt das
  Gleiche wie bei allen Datei-Systemen: Es kann langsam und konfliktreich werden.

### Decap CMS (früher „Netlify CMS")

- Offene Lizenz (MIT). Kein eigenständiges CMS, sondern eine
  **Bearbeitungs-Oberfläche**, die man **über** einen Doku-Generator legt. Die
  Texte bleiben als Markdown im Git-Lager, keine Datenbank.
- Damit können auch Menschen, die keine Textdateien bearbeiten möchten, die
  Inhalte über eine grafische Oberfläche ändern.
- **Haken:** Nachdem die Firma Netlify sich zurückgezogen hat, wird das Projekt
  von der Gemeinschaft weitergeführt – mit kleinerem, wechselndem Team.

### Kirby und Statamic

Beide sind sehr solide Flat-File-CMS mit Git-Unterstützung, aber **beide Kerne
stehen unter proprietären Lizenzen** – der Code liegt nur einsehbar auf GitHub.

- **Kirby** kostet 99 € (Tarif „Basic", nur bei unter 1 Mio. € Umsatz) bzw.
  349 € (Tarif „Enterprise") pro Website. Kostenlose Lizenzen für Studierende
  und Lehrende; für gemeinnützige Organisationen je nach Fall kostenlos oder
  vergünstigt.
- **Statamic** hat einen dauerhaft **kostenlos nutzbaren** Kern (unter einer
  eigenen, nicht quelloffenen Lizenz); erweiterte Funktionen kosten extra
  („Pro", 349 US-Dollar pro Website).

Für das Ziel „jeder darf alles frei nutzen und weitergeben" sind damit **Kirby
und Statamic** heikel.

## Vergleichstabelle

Diese Seite bewertet CMS an den Zielen dieses Projekts. Wie dieselben Systeme
technisch mit sehr großen Beständen umgehen – und welche davon überhaupt „echtes"
PostgreSQL sprechen –, behandelt die Seite
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md).

| Programm | Bauart | Lizenz voll offen? | Speicher | PostgreSQL? | Ganzer-Inhalt-Export | Schnittstelle | Nah am heutigen Aufbau? |
|---|---|---|---|---|---|---|---|
| **WordPress** | klassisch | Ja (GPL v2+) | Datenbank | Nein | Ja – WXR (XML), ohne Medien | REST ab Werk | Nein |
| **Drupal** | klassisch | Ja (GPL v2+) | Datenbank | Ja | Über Zusatzbausteine (JSON) | JSON-API + REST ab Werk | Nein |
| **TYPO3** | klassisch | Ja (GPL v2+) | Datenbank | Ja (auch SQLite) | Ja – T3D/XML | REST per Erweiterung | Nein |
| **Strapi** | headless | Kern MIT, Teile kostenpflichtig | Datenbank | Ja | Über Zusatzbausteine | REST + GraphQL | Nein |
| **Directus** | headless | Eingeschränkt (Source-available, MSCL) | Datenbank | Ja | Daten liegen offen in SQL-Tabellen | REST + GraphQL | Nein |
| **Payload** | headless | Ja (MIT) | Datenbank | Ja (auch SQLite) | Über Code/Schnittstelle | REST + GraphQL | Nein |
| **Ghost** | headless | Ja (MIT) | Datenbank | Nein (nur MySQL 8) | Ja – JSON ab Werk | REST (Content + Admin) | Nein |
| **Grav** | flat-file | Ja (MIT) | Dateien | – | Ja – der Ordner selbst | REST (ab Version 2) + MCP | **Ja** |
| **Decap CMS** | flat-file | Ja (MIT) | Dateien (über Git) | – | Ja – der Git-Ordner | arbeitet über Git | **Ja** |

## Empfehlung für dieses Projekt

Ein **CMS ist selten die beste Wahl** für ein Nachschlagewerk – dafür sind
[Wiki-Programme](wikis-im-vergleich.md) gebaut. Muss es doch ein CMS sein, hängt
die Antwort von der Bauart ab:

- **Flat-File (beste Passung):** **Grav** (echte offene Lizenz, keine Datenbank,
  REST-API und KI-Andockstelle in Version 2) oder **Decap CMS** als reine
  Bearbeitungs-Oberfläche über einem Doku-Generator. Beide erhalten den heutigen
  datei-basierten Aufbau. Für einen reinen Datei-Ansatz ohne Oberfläche siehe auch
  [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md).
- **Klassisch:** **Drupal**, wenn eine Datenbank und sehr viel strukturierter
  Inhalt gewünscht sind (PostgreSQL, für große Installationen bewährt,
  Schnittstelle ab Werk).
- **Headless:** **Directus** ist technisch reizvoll (Daten bleiben in offenen
  PostgreSQL-Tabellen), aber die Lizenz (Monospace Sustainable Core License)
  vorher genau prüfen.

## Quellen

- [Headless-CMS-Vergleich 2026: Strapi vs. Directus vs. Payload (dsrpt.com.au)](https://dsrpt.com.au/think-tank/headless-cms-showdown-strapi-vs-payload-vs-directus-in-2026)
- [Open-Source-CMS-Vergleich 2026: WordPress vs. Strapi vs. Directus (rajeshrnair.com)](https://rajeshrnair.com/blog/web-development/open-source-cms-comparison-wordpress-strapi-directus-india.html)
- [Flat-File-CMS vs. Datenbank-CMS (unfoldcms.com)](https://unfoldcms.com/blog/flat-file-cms-vs-database-cms)
- [Grav vs. Kirby CMS (selecthub.com)](https://www.selecthub.com/cms-software/grav-cms-vs-kirby/)
- [WXR-Datei in WordPress importieren und exportieren (DreamHost)](https://help.dreamhost.com/hc/en-us/articles/360050852091-Importing-and-exporting-a-WXR-file-in-WordPress)
- [TYPO3 bei Wikipedia](https://en.wikipedia.org/wiki/TYPO3)
- [Grav 2.0 Released! (getgrav.org-Blog)](https://getgrav.org/blog/grav-2-stable-released)
- [Warum wir Directus neu lizenzieren (directus.com)](https://directus.com/resources/why-we-are-relicensing-directus/)
- [Directus – Lizenz](https://directus.com/license/)
- [Ghost – Unterstützte Datenbanken (Dokumentation)](https://ghost.org/docs/faq/supported-databases/)
- [Statamic – Preise](https://statamic.com/pricing)
- [Kirby – Lizenzen kaufen](https://getkirby.com/buy)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
