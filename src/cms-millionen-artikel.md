# Wie CMS mit Millionen Artikeln umgehen

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Ein **Content-Management-System** (CMS) ist ein Programm, mit dem Redaktionen
Texte, Bilder und Seiten pflegen, ohne selbst zu programmieren. Fast jede größere
Website läuft auf so einem System. Diese Seite fragt: Was passiert mit einem CMS,
wenn aus ein paar Dutzend Artikeln Hunderttausende oder Millionen werden – und mit
welchen belegbaren Techniken halten selbst betriebene, quelloffene CMS das aus?

Sie ist damit der **technische Tiefgang** zu
[CMS im Vergleich](cms-im-vergleich.md): Dort werden einzelne CMS an den Zielen
dieses Projekts bewertet, hier geht es um die Technik dahinter. Die
übergeordnete Vogelperspektive auf vier Familien von Wissenssystemen bietet
[Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md). Der rote Faden
hier ist die Datenbank:
Die Geschichte der CMS ist auch eine Geschichte von Datenbank-Architektur, und die
freie Datenbank **PostgreSQL** dient dabei als durchgehendes Anschauungsbeispiel.

> Fachwörter wie *Open Source*, *Schnittstelle* (*API*), *REST*, *GraphQL*,
> *Datenbank*, *Markdown*, *Git*, *Node.js*, *MCP* oder *RAG* sind in
> [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md#fachwörter-kurz-erklärt)
> in einer kurzen Liste erklärt.

## Das Skalierungsproblem

Der erste Gedanke ist meist der Speicherplatz. Der ist aber selten das Problem:
Eine Million reine Textartikel sind nur wenige Gigabyte, das passt auf jede
Festplatte. Eng wird es an anderen Stellen:

- **Datenbank-Zugriffe.** Jede aufgerufene Seite löst mehrere Abfragen aus. Bei
  großen Tabellen und vielen gleichzeitigen Besuchern summiert sich das, bis die
  Datenbank zum Nadelöhr wird.
- **Verbindungen.** Jede gleichzeitige Verbindung zur Datenbank kostet
  Arbeitsspeicher. Ab einer gewissen Zahl gleichzeitiger Besucher reicht die
  Standardeinstellung nicht mehr.
- **Suche.** Eine Volltextsuche über Millionen Artikel direkt in der Datenbank
  wird langsam und belastet zugleich den normalen Betrieb.
- **Caching.** Ohne Zwischenspeicher berechnet der Server jede Seite bei jedem
  Aufruf neu. Bei viel Verkehr muss ein großer Teil der Anfragen beantwortet
  werden, bevor er das eigentliche CMS überhaupt erreicht.

Für jeden dieser Punkte gibt es erprobte Werkzeuge; der Abschnitt
[PostgreSQL als roter Faden](#postgresql-als-roter-faden) erklärt sie einzeln. Die
drei Stufen im nächsten Abschnitt ordnen nur ein, ab wann welches nötig wird.

## Drei Skalierungsstufen

Die folgenden Grenzen sind **grobe Orientierung**, keine belegten Schwellen. Wann
ein Aufbau an seine Grenze kommt, hängt stark von Inhalten, Verkehr und
Serverausstattung ab. Als Faustbild helfen drei Stufen trotzdem.

### Bis etwa 100.000 Artikel

Ein Standard-CMS auf einem einzelnen PostgreSQL-Server reicht hier meist aus,
ergänzt um das eingebaute Caching des CMS und einen vorgeschalteten
Zwischenspeicher für Besucher, die nicht angemeldet sind. Sinnvoll ist, die
**Suche früh auszulagern** – also einen eigenen Suchdienst neben die Datenbank zu
stellen, statt die Datenbank selbst suchen zu lassen. Das erspart später einen
Umbau unter Last. Typische Fälle in dieser Größe sind Behörden- oder
Hochschulportale.

### Etwa 100.000 bis 1 Million Artikel

Hier beginnt das Standard-Setup zu wackeln, und mehrere Techniken greifen
ineinander: große Tabellen **aufteilen** (Partitioning), **Lese-Kopien** (englisch
*Read-Replicas*) einsetzen, Verbindungen über einen **Pooler** bündeln, einen
**externen Suchdienst** betreiben und einen **Vorschalt-Cache** vor den anonymen
Verkehr setzen. Außerdem lohnt ein Blick auf das Datenmodell: Manche Systeme
verteilen die Felder eines Artikels auf viele Einzeltabellen, sodass schon das
Anzeigen einer Seite viele Verknüpfungen zwischen Tabellen (englisch *Joins*)
braucht. Auch Redaktionsübersichten wie „5.234 Artikel insgesamt" werden spürbar
langsam (siehe [Das Zähl-Problem](#das-zähl-problem)).

### Etwa 1 bis 10 Millionen Artikel und mehr

In dieser Größe hilft kein „mehr desselben" mehr, sondern ein qualitativ anderer
Aufbau. Große Organisationen bauen sich dann einen mehrschichtigen Stack aus
einzelnen Bausteinen zusammen, teilen Datenbank oder Suchindex bei Bedarf auf
mehrere Server auf (**Sharding**) und erzeugen aufwändige Nebenprodukte wie
Suchindizes oder KI-Vektoren in geplanten Stapelläufen (**Batch**) statt bei
jedem Speichern. Als öffentlich nachvollziehbares Vorbild dient die Architektur
von MediaWiki, dem Programm hinter der Wikipedia, das seit Jahren viele Millionen
Seiten trägt.

## PostgreSQL als roter Faden

PostgreSQL ist eine freie, weit verbreitete Datenbank. Die folgenden Werkzeuge
sind ihr Standard-Baukasten für große Bestände – die meisten haben eine
Entsprechung in anderen Datenbanken.

### Große Tabellen aufteilen (Partitioning)

**Partitioning** heißt: Eine sehr große Tabelle wird intern in mehrere kleinere
Stücke zerlegt – zum Beispiel nach Jahr oder nach Anfangsbuchstabe. Für das CMS
bleibt es eine einzige Tabelle, die Datenbank arbeitet aber nur mit dem jeweils
passenden Stück. Das macht Abfragen schneller und die Pflege (etwa das Löschen
alter Daten) einfacher. PostgreSQL kann das seit Version 10 aus dem Jahr 2017 mit
einer eigenen, einfachen Schreibweise.

### Verbindungen bündeln (PgBouncer)

Ab einer gewissen Zahl gleichzeitiger Besucher braucht ein CMS viele parallele
Datenbankverbindungen. Das wird für PostgreSQL zum Problem, weil es jede
Verbindung als eigenen Betriebssystem-Prozess mit eigenem Speicherbedarf führt –
Tausende davon überlasten den Server allein durch ihre Zahl. Ein **Connection
Pooler** löst das: ein Vermittler, der einen kleinen Vorrat an Verbindungen offen
hält und ihn unter vielen Anfragen weiterreicht. Der verbreitetste für PostgreSQL
ist das schlanke **PgBouncer**, das Tausende Client-Verbindungen auf wenige
Dutzend echte Datenbankverbindungen zusammenfassen kann.

### Lesen und Schreiben trennen (Lese-Kopien)

Die meisten Zugriffe auf ein Wiki oder CMS sind **Lesezugriffe**. PostgreSQL kann
seit Version 9.0 (2010) laufende Kopien einer Datenbank mitführen
(**Streaming-Replikation**). Lese-Anfragen gehen dann an diese Lese-Kopien, nur
Schreib-Anfragen an den Haupt-Server; so verteilt sich die Last auf mehrere
Maschinen. MediaWiki macht das seit 2004 vor. Verbreitete CMS und Web-Frameworks
wie Drupal und das hinter Wagtail stehende Framework Django bringen dafür
Konfigurationsmöglichkeiten mit.

### Suche auslagern

Große Wikis suchen **nicht** über die Datenbank. MediaWiki nutzt dafür die
Erweiterung CirrusSearch, die einen getrennten Suchverbund anspricht. Für ein
selbst betriebenes CMS kommen eigene Suchdienste wie **OpenSearch** (Lizenz
Apache 2.0), **Meilisearch** (MIT), **Typesense** oder **Elasticsearch** (Lizenz
seit 2021 eingeschränkt, seit 2024 auch als AGPL) in Frage. Drupal bindet solche
Dienste über sein Modul „Search API" an, Wagtail über austauschbare
Such-Anbindungen. Der Vorteil: Die Suche belastet den normalen Seitenbetrieb
nicht mehr und lässt sich unabhängig vergrößern.

### Vorschalt-Caches (CDN / Reverse Proxy)

Ein **Reverse Proxy** ist ein Server, der vor dem eigentlichen CMS steht und
fertige Seiten zwischenspeichert; ein **CDN** (Content Delivery Network) ist ein
weltweites Netz solcher Zwischenspeicher. Verbreitete Vertreter sind Varnish,
Fastly und Cloudflare. Für Besucher, die nicht angemeldet sind, kann so ein Cache
den Großteil der Anfragen beantworten, ohne dass CMS oder Datenbank etwas tun
müssen. Drupal ist auf dieses Zusammenspiel ausgelegt und bringt zusätzlich
mehrere eigene Cache-Ebenen mit.

### Das Zähl-Problem

Eine genaue Antwort auf „Wie viele Artikel gibt es?" ist in PostgreSQL
überraschend teuer: Die Datenbank muss dafür die ganze Tabelle beziehungsweise
einen ganzen Index durchgehen. Das beschreibt das PostgreSQL-Wiki unter „Slow
Counting". Bei kleinen Beständen fällt das nicht auf, bei Millionen Zeilen schon.
Übliche Auswege sind, in Redaktionsübersichten mit **Näherungswerten** zu
arbeiten (die PostgreSQL aus seiner internen Statistik schnell liefern kann) oder
solche Zahlen nur gelegentlich neu zu berechnen und zwischenzuspeichern.

### Bedeutung statt Stichwort (pgvector)

**pgvector** ist eine Erweiterung, die PostgreSQL beibringt, mit **Embeddings**
umzugehen – langen Zahlenreihen, die den Inhalt eines Textes als Koordinaten
abbilden. Ähnliche Inhalte liegen dann nah beieinander, auch wenn kein Wort
übereinstimmt. Damit lässt sich nach **Bedeutung** suchen und ein
Nachschlage-Ablauf für KI-Antworten (**RAG**, „erst nachschlagen, dann
antworten") aufbauen, ohne einen separaten Vektor-Dienst zu betreiben – die
Vektoren stehen einfach neben dem Inhalt in derselben Datenbank. Für schnelles
Suchen legt pgvector besondere Indizes an. Bei sehr großen Beständen erzeugt man
die Embeddings sinnvollerweise in Stapelläufen. pgvector steht unter der freien
**PostgreSQL-Lizenz**.

## Wie CMS entstanden – und wohin sie gehen

Man kann die Entwicklung der CMS in Generationen lesen. Das ist eine mögliche
Einteilung, kein Fachstandard – und die Generationen lösen sich nicht ab, sondern
bestehen nebeneinander.

### Klassische, monolithische CMS

Ein **Monolith** ist ein einziges Programm, das alles erledigt: Inhalte
verwalten, Seiten bauen, anzeigen. Diese Familie entstand mit dem klassischen
Web-Baukasten aus Linux, Webserver, Datenbank und der Sprache PHP. Bekannte
quelloffene Vertreter sind **TYPO3** (seit 1998, Lizenz GPL), **Drupal** (seit
2001, GPL) und **WordPress** (seit 2003, GPL). Solche Systeme tragen weit, stoßen
bei sechsstelligen Beständen aber eher an Grenzen, wenn nicht die oben genannten
Techniken dazukommen.

### Enterprise-Systeme aus der Java-Welt

Parallel entstand eine Linie großer Systeme in der Programmiersprache Java, die
auf Konzerne und Portale mit vielen Redakteuren zielt. **OpenCms** wird nach
Projektangaben seit dem Jahr 2000 durchgehend entwickelt, steht unter der Lizenz
LGPL und führt PostgreSQL unter den unterstützten Datenbanken. **Liferay**
entstand Anfang der 2000er Jahre; seine frei verfügbare Community-Ausgabe (Lizenz
LGPL 2.1) unterstützt quelloffene Datenbanken einschließlich PostgreSQL ab Werk.
Diese Systeme waren früh PostgreSQL-fähig, verlangen aber einen hohen
Betriebsaufwand.

### Headless und Decoupled

Neuere Systeme trennen Inhalt und Darstellung. **Headless** heißt wörtlich „ohne
Kopf": Das CMS verwaltet nur die Inhalte und liefert sie über Schnittstellen
(REST, GraphQL), zeigt sie aber nicht selbst an. **Decoupled** meint eine
Zwischenform, bei der das CMS wahlweise noch selbst Seiten bauen kann. Vertreter
mit echtem PostgreSQL-Bezug sind **Strapi** (seit 2015, Node.js, Kern unter
MIT-Lizenz), **Directus** (in seiner heutigen Form ein Neubau, veröffentlicht
2021) und **Payload** (seit 2021, Node.js; PostgreSQL kam in einer späteren
Hauptversion dazu). Zu Lizenzänderungen bei Strapi und Directus in neueren
Versionen siehe [CMS im Vergleich](cms-im-vergleich.md).

### Composable und MACH

Die jüngste Stufe zerlegt das CMS in viele kleine, über Schnittstellen verbundene
Dienste. Das Schlagwort **MACH** steht für *Microservices, API-first,
Cloud-native, Headless*. Die dahinterstehende MACH Alliance wurde 2020 als
Non-Profit gegründet. In der Praxis ist dieser Markt überwiegend
**Mietsoftware** (SaaS) von Anbietern wie Contentful oder Sanity – „Cloud-native"
meint hier ausdrücklich vom Anbieter betriebene Dienste. Für ein selbst
betriebenes Projekt lässt sich ein ähnlicher Aufbau nachbauen, er ist dann aber
kein „MACH" im Sinne der Allianz.

### KI-gestützt und agentisch

Zuletzt wird das CMS zur **Datenquelle für KI**: Sein Inhalt speist einen
RAG-Ablauf, oder spezialisierte KI-Agenten arbeiten an einem gemeinsamen
Content-Bestand, während ein Mensch die Freigabe behält. Der Inhalt liegt dann
als Markdown in einem Git-Lager oder in einer Datenbank, und ein MCP-Server
dient als Andockstelle für die Agenten. Wie das konkret aussieht, zeigen die
Seiten [LLM Wiki](llm-wiki.md) und [Co-Wiki: Mensch & KI](co-wiki.md).

## Welche Open-Source-CMS sprechen echtes PostgreSQL?

„Echt" heißt hier: PostgreSQL wird vom Projekt selbst unterstützt und getestet –
nicht über ein loses Zusatz-Plugin.

**First-Class im Kern.** Bei **Drupal** ist PostgreSQL ein vom Kern unterstützter
Datenbanktreiber (benötigt die Erweiterung `pg_trgm`); ein früherer Zusatztreiber
empfiehlt heute selbst den Wechsel auf den Kern-Treiber. **TYPO3** spricht
PostgreSQL über eine universelle Datenbank-Schicht an und testet diese Anbindung
aktiv. Bei **Wagtail** und dem darunterliegenden Framework **Django** ist
PostgreSQL voll unterstützt; darüber hinaus bietet PostgreSQL in Django
Zusatzfunktionen, unter anderem für die Volltextsuche.
**Directus** arbeitet „database-first": Es spiegelt ein bestehendes
SQL-Schema, statt ein eigenes Datenmodell aufzuzwingen – das Schema bleibt also
lesbar; eine dünne Abstraktionsschicht liegt trotzdem dazwischen. **Payload**
bietet einen offiziell unterstützten PostgreSQL-Adapter. **Strapi** unterstützt
ausschließlich SQL-Datenbanken, darunter PostgreSQL. **OpenCms** und die
**Liferay Community Edition** führen PostgreSQL seit Langem in ihrer Liste
unterstützter Datenbanken.

**Nicht oder nur über Umwege.** **WordPress** unterstützt offiziell nur
MySQL/MariaDB; PostgreSQL geht allein über das Drittanbieter-Plugin PG4WP, das
nach eigener Angabe zuletzt nicht mehr aktiv gepflegt und mit aktuellen
WordPress-Versionen getestet wurde. **Ghost** hatte früher PostgreSQL-Support,
hat ihn aber mit dem Sprung auf Version 1.0 eingestellt – als Begründung nennt
das Projekt hohen Pflegeaufwand und fehlende Entwickler, die PostgreSQL im
Betrieb nutzen. Aktuell unterstützt Ghost nur MySQL 8.

Ob eines dieser CMS **jenseits einer Million Artikel** im Praxisbetrieb erprobt
ist, lässt sich öffentlich kaum belegen. Nachweisbaren Groß-Referenzbetrieb in
dieser Größenordnung hat vor allem MediaWiki bei der Wikimedia-Stiftung; für die
CMS gibt es einzelne große Installationen, aber keine belastbare öffentliche
Datenlage.

## CMS und PostgreSQL auf einen Blick

| Programm | Bauart | PostgreSQL | Für > 1 Mio. Artikel öffentlich belegt? | Lizenz frei? | Stichwort zur Skalierung |
|---|---|---|---|---|---|
| Drupal | Monolith (PHP) | Kern-Treiber | Nein (einzelne große Sites) | Ja (GPL) | Feldtabellen im Blick behalten, externe Suche |
| TYPO3 | Monolith (PHP) | über Datenbank-Schicht, aktiv getestet | Nein | Ja (GPL) | Caching, externe Suche |
| Wagtail / Django | Headless/Decoupled | voll unterstützt (in Django mit Zusatzfunktionen) | Nein | Ja (BSD) | Lese-Kopien, Seitenbaum flach halten |
| Directus | Headless (database-first) | voll unterstützt | Nein | Neuere Versionen eingeschränkt | Schema bleibt lesbar, Suche auslagern |
| Payload | Headless (Node.js) | offizieller Adapter | Nein | Ja (MIT) | Batch-Aufgaben, externe Suche |
| Strapi | Headless (Node.js) | unterstützt (nur SQL) | Nein | Kern frei (MIT), Zusätze teils kostenpflichtig | Connection Pooling |
| OpenCms | Enterprise (Java) | unterstützt | Nein | Ja (LGPL) | Java-Portalbetrieb, Clustering |
| Liferay CE | Enterprise (Java) | ab Werk in der Community Edition | Nein | Ja (LGPL 2.1) | Clustering, Caching |
| WordPress | Monolith (PHP) | nur über Plugin PG4WP (ungepflegt) | – | Ja (GPL) | – |
| Ghost | Headless/Blog (Node.js) | eingestellt (heute nur MySQL 8) | – | Ja (MIT) | – |

Diese Tabelle ordnet nur die PostgreSQL-Frage und die Skalierung ein. Die
Bewertung an den Zielen dieses Projekts – Export, Lizenzfeinheiten, Nähe zum
heutigen Dateiaufbau – steht auf [CMS im Vergleich](cms-im-vergleich.md).

## Was heißt das für dieses Wiki?

Dieses Wiki nutzt heute **mdBook** mit **Git** und **Markdown** – „Docs as Code",
also gar kein CMS und keine Datenbank. Das passt zum überschaubaren Bestand von
rund sechzig Artikeln und zur Zusammenarbeit mit KI, weil alle Inhalte einfache
Textdateien sind. Sollte das Projekt einmal stark wachsen, käme eher ein echtes
Wiki-System oder ein zusätzlicher Suchverbund in Frage als ein klassisches CMS;
die Werkzeuge dieser Seite – Partitioning, Pooler, Lese-Kopien, ausgelagerte
Suche, Vorschalt-Caches – wären dann die Stellschrauben. Würde eine solche
Erweiterung einen eigenen Anwendungs-Server erfordern, sind zusätzlich
Programmiersprache und Webframework zu bedenken – erläutert auf
[Webframeworks im Vergleich](webframeworks-im-vergleich.md). Der eigentliche eigene
Weg dieses Projekts ist aber kein bestimmtes Programm, sondern die geregelte
Zusammenarbeit von Mensch und KI, beschrieben unter
[Co-Wiki: Mensch & KI](co-wiki.md) und [LLM Wiki](llm-wiki.md).

## Verwandte Seiten

- [CMS im Vergleich](cms-im-vergleich.md) – Bewertung einzelner CMS an den Zielen
  dieses Projekts (Ebene über dieser Seite)
- [Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md) – die vier
  Familien von Wissenssystemen von oben betrachtet
- [Ein Wissenssystem selbst bauen](wissenssystem-selbst-bauen.md) – konkrete
  Programmiersprachen-Ökosysteme und Werkzeug-Stacks für Eigenbau
- [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)
  – Übersicht und Fachwörter-Liste
- [Wiki-Programme im Vergleich](wikis-im-vergleich.md) ·
  [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md) –
  Schwesterseiten
- [Co-Wiki: Mensch & KI](co-wiki.md) · [LLM Wiki](llm-wiki.md) – die agentische
  Stufe

## Quellen

- [Drupal – Database server requirements](https://www.drupal.org/docs/getting-started/system-requirements/database-server-requirements)
- [Drupal – Core provided database drivers moved to their own modules](https://www.drupal.org/node/3129492)
- [Drupal – PostgreSQL fallback driver](https://www.drupal.org/project/pgsql_fallback)
- [TYPO3 – Database (Doctrine DBAL)](https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ApiOverview/Database/DoctrineDbal/Index.html)
- [Wikipedia – TYPO3](https://en.wikipedia.org/wiki/TYPO3)
- [django-treebeard – Materialized Path trees](https://django-treebeard.readthedocs.io/en/latest/mp_tree.html)
- [Wagtail – A tale of digging into Wagtail's page tree internals](https://wagtail.org/blog/a-tale-of-digging-into-wagtails-page-tree-internals/)
- [Directus – Bring your existing database](https://directus.com/features/existing-database)
- [Directus – Data model](https://directus.io/docs/getting-started/data-model)
- [Directus – Open Data Platform Concept](https://directus.io/blog/Directus-and-the-Open-Data-Platform-Concept)
- [Payload – Postgres](https://payloadcms.com/docs/database/postgres)
- [Payload – Announcing Payload 2.0](https://payloadcms.com/posts/blog/payload-2-0)
- [Strapi – Database configuration](https://docs.strapi.io/cms/configurations/database)
- [Strapi – Supported databases](https://docs.strapi.io/snippets/supported-databases)
- [OpenCms – FAQ](https://www.opencms.org/en/overview/faq/index.html)
- [Wikipedia – OpenCms](https://en.wikipedia.org/wiki/OpenCms)
- [Liferay – Portal 7 CE: App Server, Database & Clustering Support](https://liferay.dev/en/b/liferay-portal-7-ce-app-server-database-clustering-support)
- [Liferay – PostgreSQL Database Support Policy](https://help.liferay.com/hc/en-us/articles/360018064092-PostgreSQL-Database-Support-Policy)
- [WordPress – Plugin „PostgreSQL for WordPress (PG4WP)"](https://wordpress.org/support/plugin/postgresql-for-wordpress/)
- [GitHub – postgresql-for-wordpress](https://github.com/PostgreSQL-For-Wordpress/postgresql-for-wordpress)
- [Ghost – Dropping Support for PostgreSQL](https://ghost.org/changelog/dropping-support-for-postgresql/)
- [Ghost – Supported databases](https://ghost.org/docs/faq/supported-databases/)
- [PostgreSQL 10 – Release-Ankündigung](https://www.postgresql.org/about/news/1786/)
- [PostgreSQL – Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)
- [PostgreSQL – Log-Shipping Standby Servers (warm standby)](https://www.postgresql.org/docs/current/warm-standby.html)
- [PostgreSQL-Wiki – Slow Counting](https://wiki.postgresql.org/wiki/Slow_Counting)
- [PostgreSQL-Wiki – Count estimate](https://wiki.postgresql.org/wiki/Count_estimate)
- [PgBouncer – offizielle Website](https://www.pgbouncer.org/)
- [GitHub – pgbouncer](https://github.com/pgbouncer/pgbouncer)
- [GitHub – pgvector](https://github.com/pgvector/pgvector)
- [Crunchy Data – HNSW-Indizes mit Postgres und pgvector](https://www.crunchydata.com/blog/hnsw-indexes-with-postgres-and-pgvector)
- [MACH Alliance](https://machalliance.org/)
- [Wikipedia – MACH Alliance](https://en.wikipedia.org/wiki/MACH_Alliance)
- [MediaWiki – Extension: CirrusSearch](https://www.mediawiki.org/wiki/Extension:CirrusSearch)
- [MediaWiki – Manual: MediaWiki architecture](https://www.mediawiki.org/wiki/Manual:MediaWiki_architecture)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
