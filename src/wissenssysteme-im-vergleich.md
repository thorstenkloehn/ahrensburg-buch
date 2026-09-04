# Wissenssysteme im Vergleich

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Dieses Wiki ist heute klein – rund sechzig Artikel. Aber was, wenn ein
Nachschlagewerk aus **Hunderttausenden oder Millionen** Artikeln bestünde? Große
Organisationen wie die Wikimedia-Stiftung, Software-Firmen oder Behörden stehen
vor genau dieser Frage: Wie speichert, sichert und durchsucht man so viel Wissen,
ohne dass alles unübersichtlich oder langsam wird?

Diese Seite ist ein **Blick nach oben** – eine Landkarte, kein Ratgeber für die
nächste Entscheidung dieses Projekts. Sie sortiert die verfügbaren Ansätze in
**vier Familien** und beschreibt, wie weit jede Familie trägt.

Die genaue Bewertung einzelner Programme an den Projektzielen steht weiterhin auf
den vier Schwesterseiten, die von
[Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)
ausgehen. Die grundlegenden Konzepte zum Speichern und Suchen von Wissen
erklärt [Wissen speichern](wissen-speichern.md). Hier geht es um die Ebene
darüber: die Größenordnung von einer Million Artikeln aufwärts und der
Ausblick auf Systeme, die nach Bedeutung suchen statt nur nach Stichwörtern.

> Fachwörter wie *Open Source*, *Schnittstelle* (*API*), *REST*, *GraphQL*,
> *Datenbank*, *Markdown*, *Git*, *Node.js*, *MCP* oder *RAG* sind in
> [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md#fachwörter-kurz-erklärt)
> in einer kurzen Liste erklärt.

## Vier Familien von Wissenssystemen

Die vier Familien lösen unterschiedliche Probleme. Manche Projekte kombinieren
sie sogar. Hier der Reihe nach.

### 1. Wiki-Engines – viele Menschen schreiben gemeinsam

Ein **Wiki** ist darauf ausgelegt, dass viele Menschen dieselben Seiten
bearbeiten. Jede Änderung landet in einer Versionsgeschichte, man kann also
jederzeit zurückspringen und sehen, wer was geändert hat. Das ist der große
Unterschied zu einem Ordner voller Dateien: Das Wiki verwaltet den gemeinsamen
Zugriff selbst.

**MediaWiki**, das Programm hinter der Wikipedia, ist der Beweis, dass diese
Familie riesige Mengen verträgt. Es speichert die Inhalte in einer Datenbank
(am besten unterstützt: MySQL/MariaDB) und hält den Betrieb mit mehreren
Zwischenspeichern (Caches) schnell: Im Wikimedia-Betrieb beantworten die meisten
Anfragen vorgelagerte Caches, sie erreichen die eigentlichen Anwendungs-Server
nie. Außerdem bringt MediaWiki seit 2004 eine eingebaute Lastverteilung mit –
Lese-Anfragen gehen an Kopien der Datenbank, Schreib-Anfragen an den
Haupt-Server.

Die Volltextsuche großer Wikis läuft dabei **nicht** über die Datenbank. Dafür
gibt es die Erweiterung **CirrusSearch**, die einen eigenen Suchdienst
(Elasticsearch beziehungsweise das quelloffene OpenSearch) als getrennten
Verbund von Servern anspricht. Diese Kombination wird bei der Wikimedia-Stiftung
für Wikis mit vielen Millionen Seiten eingesetzt. Wer die Wiki-Seiten zusätzlich
als strukturierte Daten nutzen will – mit festen Feldern und Abfragen –, greift
zu Fachversionen wie **Wikibase** (der Software hinter Wikidata, mit verknüpften
offenen Daten) oder **Semantic MediaWiki**; das Programm **XWiki** bietet noch
mehr freie Gestaltung. Mehr zu den einzelnen Programmen auf der Seite
[Wiki-Programme im Vergleich](wikis-im-vergleich.md).

### 2. Docs-as-Code und Static Site Generators – Texte als Dateien versioniert

„**Docs as Code**" heißt: Dokumentation wird mit denselben Werkzeugen und
Abläufen geschrieben wie Programmcode – Klartext-Dateien (meist Markdown),
Versionsverwaltung mit Git, gegenseitige Durchsicht („Reviews") und automatische
Prüfungen. Aus den Dateien baut dann ein **Static Site Generator** eine fertige
Website. Genau so entsteht auch dieses Wiki – mit dem Generator mdBook.

In dieser Familie gibt es reife Vertreter für große Bestände: **MkDocs** mit dem
Design „Material" (die Suche läuft komplett im Browser des Lesers, breit
eingesetzt), **Hugo** (in der Sprache Go geschrieben, das höchste Bautempo),
**Antora** (führt Dokumentation aus mehreren getrennten Git-Lagern zusammen,
Schreibweise AsciiDoc) und **Backstage/TechDocs**, die selbstgebaute Lösung von
Spotify: Dort werden nach eigenen Angaben über 5.000 Dokumentations-Websites auf
diese Weise betrieben.

Die Grenze dieser Familie ist immer dieselbe: Wenn sehr viele Menschen
**gleichzeitig** schreiben sollen, gibt es Datei-Konflikte, die jemand von Hand
auflösen muss. Und bei sehr großen Beständen dauert das Bauen der Website
länger – wie lange, hängt stark vom gewählten Generator ab. Einzelheiten auf der
Seite [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md).

### 3. Suche und semantische Systeme – nach Bedeutung suchen

Bei Millionen Artikeln reicht die reine Stichwortsuche oft nicht: Wer „Auto"
eingibt, findet keine Seite, auf der nur „Kraftfahrzeug" oder „Pkw" steht.
Semantische Systeme suchen deshalb nach der **Bedeutung** eines Textes, nicht
nur nach den genauen Wörtern.

Dafür wird jeder Text in eine lange Zahlenreihe übersetzt, ein **Embedding** oder
**Vektor**. Man kann sich das wie Koordinaten vorstellen: „Auto", „Kraftfahrzeug"
und „Pkw" bekommen ähnliche Koordinaten und liegen nah beieinander, obwohl kein
Buchstabe übereinstimmt. Die Suche liefert dann die **k nächsten Nachbarn**
(englisch *k-NN*) – die inhaltlich ähnlichsten Texte. Eine **Hybrid-Suche**
kombiniert beides: klassische Stichwörter plus Bedeutungsähnlichkeit.

Bekannte quelloffene Bausteine sind **OpenSearch** und **Elasticsearch** –
Such-Verbünde, die man durch Hinzufügen weiterer Server wachsen lässt und die
seit einigen Jahren auch mit Vektoren umgehen; **Meilisearch** – bewusst einfach
einzurichten und tolerant gegenüber Tippfehlern; und **pgvector** – eine
Erweiterung, die Vektoren in der Datenbank PostgreSQL ablegt, sodass kein
zusätzliches System nötig ist. Eng verwandt ist **RAG** – „erst nachschlagen,
dann antworten": Eine KI durchsucht echte Dokumente, bevor sie einen Text
formuliert. Damit das gelingt, werden lange Dokumente vorher in handliche Teile
zerlegt (**Chunking**). Das quelloffene **RAGFlow** ist darauf spezialisiert,
auch schwierige Dateien wie PDFs mit Tabellen sauber in solche Häppchen zu
zerlegen und daraus einen Frage-Antwort-Ablauf zu bauen. Für pgvector kursieren
Angaben zum Arbeitsspeicher-Bedarf – von wenigen Gigabyte bis zu mehreren zehn
Gigabyte je Million Vektoren; das sind **grobe Schätzungen** aus zweiter Hand und
hängen stark von den Einstellungen ab.

### 4. Selbstgebaute Systeme aus mehreren Schichten

Sehr große Organisationen kaufen selten ein einzelnes Fertigprodukt. Sie bauen
sich einen **Schichten-Aufbau** (englisch *Stack*): eine Redaktions-Schicht, in
der Menschen schreiben; einen Speicher für große Dateien wie Bilder und Videos;
und einen Such-Verbund für die Millionen Dokumente, dessen Daten bei Bedarf auf
mehrere Server aufgeteilt werden (**Sharding**).

Für die Redaktions-Schicht kommen oft **Headless-CMS** zum Einsatz, zum Beispiel
**Strapi** oder **Directus**. **Headless** heißt wörtlich „ohne Kopf": Das System
verwaltet nur die Inhalte und liefert sie über Schnittstellen (REST, GraphQL),
zeigt sie aber nicht selbst an – das Aussehen baut jede Website selbst. Mehr dazu
auf der Seite [CMS im Vergleich](cms-im-vergleich.md). Für die großen Dateien
nutzt man einen **Objektspeicher** wie S3 oder das quelloffene MinIO – einen
Dienst, der beliebig viele Dateien unter festen Adressen ablegt.

So ein Schichten-Aufbau ist eine Maßanfertigung: Die Bausteine sind erprobt, die
Kombination baut jedes Projekt selbst. Konkrete Überlegungen, welche
Programmiersprachen und Ökosysteme dafür taugen – Rust, Go, JVM, ASP.NET Core –,
zeigt [Ein Wissenssystem selbst bauen](wissenssystem-selbst-bauen.md).

## Eine mögliche Sicht: Generationen von Wissenssystemen

Man kann die vier Familien auch als zeitliche Abfolge lesen: von der Wiki-Familie
über die Docs-as-Code-Familie und die Suche-Familie bis zu **agentischen**
Systemen, in denen KI-Programme selbstständig recherchieren und schreiben.

Das ist ausdrücklich **eine mögliche Einteilung, kein Fachstandard**. Belegt ist
vor allem die jüngste Stufe: Eine Übersichtsarbeit zu „Agentic RAG" beschreibt
die Entwicklung von einfacher zu immer eigenständigerer Nachschlage-KI. Wie so
eine agentische Stufe konkret aussieht, zeigt die Seite
[LLM Wiki](llm-wiki.md).

## Vier Familien auf einen Blick

| Familie | Bis 1 Mio.+ Artikel | Bis 10 Mio.+ Artikel | Volltextsuche eingebaut | Semantische / RAG-Suche | Viele gleichzeitige Autoren | Quelloffen & kostenlos |
|---|---|---|---|---|---|---|
| **Wiki-Engines** (MediaWiki u. a.) | Ja | Ja (Wikipedia, viele Mio. Seiten) | Teilweise (große Wikis über Zusatz-Suchdienst) | Nein (nur über Zusatz) | Ja | Ja |
| **Docs-as-Code / SSG** | Ja | Teilweise (vom Generator abhängig) | Teilweise (je nach Generator/Theme) | Nein | Nein | Ja |
| **Suche & semantische Systeme** | Ja | Ja | Ja (das ist ihr Zweck) | Ja | Nein (kein Schreib-System) | Ja |
| **Selbstgebaute Schichten-Systeme** | Ja | Ja | Ja (Such-Schicht) | Teilweise (je nach Aufbau) | Ja (Redaktions-Schicht) | Teilweise (Bausteine ja, Lizenzen unterschiedlich) |

Die quelloffenen Bausteine stehen unter verschiedenen freien Lizenzen
(OpenSearch und RAGFlow unter Apache 2.0, Meilisearch unter MIT, pgvector unter
der PostgreSQL-Lizenz, Wikibase und Semantic MediaWiki unter der GPL), während
die Headless-CMS Strapi und Directus in neueren Versionen Einschränkungen haben
(siehe [CMS im Vergleich](cms-im-vergleich.md)).

## Verbreitete Missverständnisse

Über die Grenzen dieser Systeme kursieren einige Faustregeln, die so nicht
stimmen. Drei davon.

### „Meilisearch funktioniert nur bis 5–10 Millionen Dokumente"

Woher diese Zahl stammt, ist unklar – belegt ist sie nicht. Die offizielle
Dokumentation nennt als hartes Limit **4.294.967.296 Dokumente pro Index** (das
ist zwei hoch 32, also gut vier Milliarden). Der Hersteller-Blog beschreibt einen
Fall, in dem ein Firmen-Team die Marke von 100 Millionen Dokumenten überschritten
hatte; die Lösung war dort Sharding, also das Aufteilen des Bestands auf mehrere
Server. Richtig ist also: Meilisearch ist auf einfache Einrichtung und
Tippfehler-Toleranz ausgelegt, und sehr große Bestände brauchen auch hier mehrere
Server – nicht aber, dass bei zehn Millionen Schluss wäre.

### „Static-Site-Generatoren brechen bei über 100.000 Seiten ab"

Für einen langsamen, speicherhungrigen Generator kann das zutreffen. Als
allgemeines Prinzip ist es falsch. Hugo etwa ist in der Sprache Go geschrieben
und gilt als schnellster verbreiteter Generator; es gibt Berichte über
Hugo-Websites mit rund einer Million Seiten. Ob ein Generator bei großen
Beständen einbricht, ist also eine Frage des **Werkzeugs**, nicht der Familie.

### „Es gibt einen bewährten Standard-Stack für große Wikis"

Den gibt es nicht. Öffentlich nachweisbaren Groß-Referenzbetrieb hat nur
**MediaWiki mit CirrusSearch** bei der Wikimedia-Stiftung. Alle anderen
Schicht-Kombinationen – Wiki plus Wissensdatenbank plus Suchverbund, oder
Redaktions-CMS plus Objektspeicher plus RAG-Pipeline – sind plausibel, aber
Maßanfertigungen. Ein „One size fits all" für Millionen-Wikis existiert nicht.

## Was heißt das für dieses Wiki?

Dieses Wiki nutzt heute den Doku-Generator **mdBook** – Familie 2, Docs as Code.
Das passt gut zu einem überschaubaren Bestand und zur Zusammenarbeit mit KI, weil
alle Inhalte einfache Markdown-Dateien sind. Sollte das Projekt einmal auf
zehntausende Artikel wachsen, käme ein echtes Wiki-System oder ein zusätzlicher
Such-Verbund in Frage; welche Programme dann wie abschneiden, steht auf den vier
Schwesterseiten
([Wiki-Programme](wikis-im-vergleich.md), [CMS](cms-im-vergleich.md),
[Doku-Generatoren](doku-generatoren-im-vergleich.md) und der Übersicht
[Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)).
Wie selbst betriebene CMS technisch mit sechs- und siebenstelligen Beständen
umgehen – Partitioning, Connection-Pooler, Lese-Kopien, ausgelagerte Suche,
Vorschalt-Caches –, vertieft die Seite
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md).
Für einen selbstgebauten Stack mit eigenem Anwendungs-Server spielt zudem die
Wahl der Programmiersprache und des Webframeworks eine zentrale Rolle, dargestellt
auf [Webframeworks im Vergleich](webframeworks-im-vergleich.md).
Der eigentliche eigene Weg dieses Projekts ist aber kein bestimmtes Programm,
sondern die geregelte Zusammenarbeit von Mensch und KI – beschrieben unter
[Co-Wiki: Mensch & KI](co-wiki.md) und [LLM Wiki](llm-wiki.md).

## Quellen

- [Write the Docs – Docs as Code](https://www.writethedocs.org/guide/docs-as-code/)
- [Antora – Startseite](https://antora.org/)
- [Antora – Dokumentation](https://docs.antora.org/antora/latest/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Hugo – offizielle Website](https://gohugo.io/)
- [CSS-Tricks – Comparing Static Site Generator Build Times](https://css-tricks.com/comparing-static-site-generator-build-times/)
- [Backstage – TechDocs](https://backstage.io/docs/features/techdocs/)
- [MediaWiki – Manual: MediaWiki architecture](https://www.mediawiki.org/wiki/Manual:MediaWiki_architecture)
- [MediaWiki – Extension: CirrusSearch](https://www.mediawiki.org/wiki/Extension:CirrusSearch)
- [Wikibase](https://wikiba.se/)
- [Semantic MediaWiki](https://www.semantic-mediawiki.org/)
- [OpenSearch – Startseite und Lizenz (Apache 2.0)](https://opensearch.org/)
- [OpenSearch – Dokumentation](https://docs.opensearch.org/latest/)
- [OpenSearch – AI und Vektor-Suche](https://docs.opensearch.org/latest/vector-search/ai-search/index/)
- [RAGFlow – GitHub](https://github.com/infiniflow/ragflow)
- [Strapi – Dokumentation](https://docs.strapi.io/)
- [Directus – Dokumentation](https://directus.com/docs/)
- [Meilisearch – Known limitations](https://www.meilisearch.com/docs/learn/resources/known_limitations)
- [Meilisearch – Blog: Sharding und Replication](https://www.meilisearch.com/blog/sharding-replication)
- [ClickHouse – Scaling vector search with Postgres](https://clickhouse.com/resources/engineering/scale-vector-search-postgres)
- [Crunchy Data – HNSW-Indizes mit Postgres und pgvector](https://www.crunchydata.com/blog/hnsw-indexes-with-postgres-and-pgvector)
- [A Survey on Agentic RAG (arXiv:2501.09136)](https://arxiv.org/abs/2501.09136)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
