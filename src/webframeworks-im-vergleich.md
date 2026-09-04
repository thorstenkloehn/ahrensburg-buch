# Webframeworks im Vergleich

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Dieses Wiki ist heute klein – rund sechzig Artikel. Aber was, wenn ein
Nachschlagewerk aus **Hunderttausenden oder Millionen** Artikeln bestünde, dazu
noch aus vielen Millionen einzelner Inhaltsblöcke? Wer eine große
Content-Plattform baut, muss früh die Frage stellen, mit welcher Programmiersprache
und welchem **Web-Framework** – dem Programmgerüst, das die Anfragen aus dem
Internet entgegennimmt – der Server laufen soll.

Diese Seite ist ein **Blick nach oben**, eine Einordnung und Zukunftsbetrachtung –
kein Ratgeber für die nächste Entscheidung dieses Projekts und keine Anleitung.
Dieses Wiki nutzt [mdBook](doku-generatoren-im-vergleich.md) mit **Git** und
**Markdown** – „Docs as Code", also **gar kein** Web-Framework. Die folgenden
Überlegungen greifen erst, wenn ein Projekt einen echten Anwendungs-Server
betreiben würde.

Vorweg die Kernbotschaft, damit sie nicht untergeht: Das Web-Framework ist nur der
**Dirigent**. Bei Millionen Inhalten liegt die eigentliche Last nicht bei ihm,
sondern bei der **Speicher-, Such- und Cache-Architektur** dahinter – und die ist
weitgehend unabhängig davon, in welcher Sprache der Server geschrieben ist.

> Fachwörter wie *Open Source*, *Schnittstelle* (*API*), *REST*, *GraphQL*,
> *Datenbank*, *Markdown*, *Git*, *Node.js*, *MCP* oder *RAG* sind in
> [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md#fachwörter-kurz-erklärt)
> in einer kurzen Liste erklärt.

## Was ist ein Web-Framework?

Ein **Web-Framework** ist ein fertiges Programmgerüst, das die immer gleichen
Aufgaben eines Servers übernimmt: Es nimmt eine Anfrage aus dem Netz entgegen,
erkennt anhand der Adresse, welcher Programmteil zuständig ist (**Routing**, das
Zuordnen von Adressen zu Funktionen), packt die eingehenden Daten aus, ruft die
eigene Fachlogik auf und verpackt die Antwort wieder in ein Format wie JSON oder
XML (**Serialisierung**, das Umwandeln von Programmdaten in eine übertragbare
Zeichenkette). Das Framework sitzt damit ganz oben in der Verarbeitungskette. Die
schwere Arbeit – das Zusammenbauen der Seiten, das Zwischenspeichern, die
Datenbankzugriffe – findet darunter statt, oft sogar außerhalb des eigentlichen
Servers, wie der nächste Abschnitt zeigt.

## Nicht das Framework ist das Nadelöhr

Wenn ein Bestand auf Millionen Artikel wächst, wird gern zuerst über die Sprache
gestritten: Rust oder Go oder Java? Das ist selten die entscheidende Frage. Zum
Nadelöhr wird fast immer die Schicht darunter – die Datenbank, die Suche, der
Cache. Diese Engpässe entstehen unabhängig vom Framework, und sie lassen sich auch
nur dort lösen.

Das beste öffentlich nachvollziehbare Beispiel ist die Wikipedia selbst. Sie läuft
auf **MediaWiki**, und MediaWiki ist in **PHP** geschrieben – einer Sprache, die
nicht für maximale Rechenleistung bekannt ist. Trotzdem trägt dieser Aufbau viele
Millionen Seiten. Nicht wegen PHP, sondern wegen der Architektur drumherum: Schon
seit 2004 verteilt sich die Datenbank auf einen Server für Schreibzugriffe und
beliebig viele **Lese-Kopien**; zusätzlich fängt eine vorgeschaltete Cache-Schicht
(bei Wikimedia übernehmen das die Werkzeuge Varnish und Apache Traffic Server)
den Großteil der Leseanfragen ab, bevor sie überhaupt beim Anwendungs-Server
ankommen. Und die Volltextsuche läuft nicht
über die Hauptdatenbank, sondern über einen getrennten Suchverbund (die
MediaWiki-Erweiterung CirrusSearch spricht dafür Elasticsearch beziehungsweise das
quelloffene OpenSearch an). Kurz: **Architektur schlägt Sprache.** Die Einzelheiten
dieser Technik stehen auf
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md) und
[Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md).

Diese Werkzeuge – große Tabellen aufteilen, Daten auf mehrere Server verteilen,
Verbindungen bündeln, Lese-Kopien einsetzen, die Suche auslagern, Zwischenspeicher
vorschalten – sind auf jede Sprache übertragbar. Das Aufteilen der Daten und ihr
Verteilen auf mehrere Server sowie das Arbeiten mit Lese-Kopien sind, wie es das
Standardwerk *Designing Data-Intensive Applications* von Martin Kleppmann
beschreibt, die allgemeinen Mittel gegen Datenmengen, die über eine einzelne
Maschine hinauswachsen: Man verteilt die Abfragelast auf viele Rechner. Mit diesen
Mitteln skaliert auch ein „langsames" Framework. Ohne sie kommt auch das
„schnellste" nicht weit.

## Die drei Sprach-Familien: qualitative Unterschiede

Für einen selbst gebauten Anwendungs-Server werden heute meist drei Sprach-Familien
genannt. Sie unterscheiden sich weniger im Alltagstempo als in einigen
grundlegenden Mechanismen: ob und wie sie ungenutzten Speicher automatisch
aufräumen, wie sie viele gleichzeitige Anfragen bearbeiten, wie viel
Arbeitsspeicher sie brauchen und wie lange sie zum Starten benötigen.

### Rust – Frameworks wie Axum und Actix-web

Rust hat **keinen Garbage Collector** – kein Hintergrundprogramm, das während des
Laufs automatisch ungenutzten Speicher einsammelt. Stattdessen prüft der Compiler
schon beim Übersetzen anhand fester Regeln (dem Eigentums- oder *Ownership*-Modell),
wann Speicher freigegeben werden darf. Zur Laufzeit gibt es dadurch keine
**GC-Pausen** – keine kurzen Momente, in denen das Programm für die
Aufräumarbeit innehält. Von den drei Familien ist Rust die einzige ohne solchen
Sammler.

**Axum** ist ein bewusst dünnes Framework auf dem HTTP-Baustein *hyper*; es nutzt
die Laufzeitumgebung *tokio*, um viele Anfragen gleichzeitig zu bearbeiten, und
bezieht Zusatzfunktionen wie Zeitlimits oder Kompression aus dem *tower*-Baukasten. Der
Preis ist eine steile Lernkurve. Das Ökosystem ist außerdem jung: Axum erschien
2021 in Version 0.1, und die 0.x-Reihe brachte wiederholt Änderungen, die
bestehenden Code brechen. Die Lizenzen sind für ein freies Projekt unkritisch –
Axum steht unter der MIT-Lizenz, Actix-web wahlweise unter MIT oder Apache 2.0.

### Go – Frameworks wie Gin, Chi und Fiber

Go bringt **Goroutinen** mit: sehr leichtgewichtige „Fäden", die der Go-eigene
Ablaufplaner verwaltet und auf wenige Betriebssystem-Fäden verteilt. Eine Goroutine
kostet kaum mehr als etwas Stapelspeicher, sodass ein Server problemlos sehr viele
davon gleichzeitig führen kann. Das Prinzip ähnelt dem, was tokio für Rust leistet.

Anders als Rust **hat Go einen Garbage Collector**. Er arbeitet größtenteils
nebenläufig zur Anwendung, um Wartezeiten kurz zu halten, ist aber **nicht
pausenfrei**: Es bleiben kurze Momente, in denen alle Goroutinen angehalten werden.
Wie lang diese Pausen sind, hängt laut offizieller Go-Dokumentation vor allem von
der Zahl der Prozessorkerne und der laufenden Goroutinen ab, nicht so sehr von der
Größe des belegten Speichers; in der Praxis sind sie typischerweise sehr kurz,
aber eben nicht null. Nebenläufiges Aufräumen hat zudem seinen Preis – es führt oft
zu einem geringeren Gesamtdurchsatz als ein Sammler, der die Anwendung
komplett anhält.

Go gilt weithin als Sprache mit **schnellen Entwicklungszyklen** und ist seit
Version 1.0 aus dem Jahr 2012 im Server- und Netzwerkbereich fest etabliert. Der
Ruf des zügigen Arbeitens ist eine verbreitete Einschätzung von Entwicklerinnen
und Entwicklern, keine gemessene Größe. Die Frameworks Gin, Chi und Fiber stehen
unter der MIT-Lizenz.

### JVM – Frameworks wie Spring Boot, Quarkus und Micronaut

Diese Familie läuft auf der **Java Virtual Machine** (JVM), der
Laufzeitumgebung für Java und verwandte Sprachen wie Kotlin. Im klassischen
Betrieb übersetzt die JVM den Code erst während des Laufs in Maschinensprache
(**JIT**, „just in time", also just rechtzeitig) und wird dabei mit der Zeit
schneller – es gibt also eine Aufwärmphase. Auch hier räumt ein Garbage Collector
mit Stop-the-World-Anteilen auf, und der Arbeitsspeicherbedarf ist im klassischen
Modus höher als bei Go oder Rust.

**Aber** die neueren Frameworks relativieren das. Quarkus und Micronaut sind darauf
ausgelegt, möglichst viel schon beim Übersetzen zu erledigen und dann ein
**Native Image** zu erzeugen – ein vorab in Maschinensprache übersetztes,
eigenständiges Programm (mit dem Werkzeug GraalVM), das keine JVM mehr braucht.
Nach Angaben der Projekte sinkt die Startzeit damit in den zweistelligen
Millisekundenbereich, der Arbeitsspeicherbedarf deutlich unter den klassischen
JVM-Betrieb. Spring Boot unterstützt diesen Weg ebenfalls (unter dem Stichwort
Spring AOT). Das Spring-Framework ist seit 2003 der De-facto-Standard im
Java-Unternehmensumfeld, Spring Boot seit 2014; Micronaut (2018) und Quarkus
(2019) sind jung. Alle drei stehen unter der Apache-2.0-Lizenz.

### Was sich daraus ableiten lässt – und was nicht

Belastbare Aussagen über Tempo brauchen einen genauen Kontext: welche Hardware,
welche Art von Last, welche Version. Ohne das ist eine pauschale Rangfolge nach dem
Muster „Rust vor Go vor Java" nicht seriös, und konkrete Durchsatzzahlen erst
recht nicht. Belegbar sind nur die **Mechanismen**: Garbage Collector ja oder nein,
JIT-Aufwärmphase, Native Image, Art der Nebenläufigkeit, Startzeit,
Arbeitsspeicherbedarf. Für sehr große Lasten sind alle drei Familien grundsätzlich
geeignet – vorausgesetzt, die Datenbank- und Cache-Schicht stimmt.

Zur Orientierung dienen die **TechEmpower Framework Benchmarks**, ein quelloffener
Dauervergleich vieler Frameworks bei Grundaufgaben wie JSON-Serialisierung,
einzelnen Datenbankabfragen oder dem Füllen einer Vorlage. Das ist nützlich, um die
Mechanismen zu verstehen, aber ein **synthetischer Mikro-Vergleich**: künstliche
Einzelaufgaben, kein Ersatz für die Messung einer echten Anwendung mit ihrem
tatsächlichen Zuschnitt.

## Speicher, Suche, Cache

Die schwere Arbeit liegt, wie oben gesagt, in der Schicht unter dem Framework. In
Stichworten sind das: große Tabellen **aufteilen** (Partitioning) und bei Bedarf
über mehrere Server verteilen (**Sharding**); **Lese-Kopien** der Datenbank für die
überwiegend lesenden Zugriffe; einen **Verbindungs-Pooler** (etwa PgBouncer), der
viele Client-Verbindungen auf wenige echte Datenbankverbindungen bündelt; die
**Suche auslagern** an einen eigenen Dienst statt sie die Hauptdatenbank erledigen
zu lassen; und **Vorschalt-Caches** (ein *Reverse Proxy* wie Varnish oder Nginx –
ein Server, der vor der Anwendung steht und fertige Seiten zwischenspeichert). Bei
PostgreSQL gibt es die eingebaute Tabellenaufteilung seit Version 10 (2017);
automatisches Verteilen über mehrere Server leistet erst die Erweiterung Citus.

All das ist auf der Seite
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md) ausführlich
beschrieben – mit den drei Skalierungsstufen, dem Zähl-Problem und der
Vektor-Erweiterung pgvector. Diese Seite hält sich hier absichtlich kurz.

### Lizenzverschiebungen bei Speicher- und Such-Bausteinen

Ein Punkt ist für ein freies Projekt trotzdem wichtig: Bei den Speicher- und
Such-Bausteinen hat sich die **Lizenzlage 2024 und 2025 stark verschoben**.
CockroachDB hat seine kostenlose Kern-Ausgabe eingestellt; ScyllaDB ist auf „source
available" umgestellt (quelloffen einsehbar, aber nicht mehr nach den Kriterien der
Open Source Initiative frei); rund um Redis gab es Streit um die Lizenz – als
Reaktion entstand das frei lizenzierte Abspaltungsprojekt Valkey unter der Linux
Foundation; DragonflyDB steht unter der einschränkenden BSL; Elasticsearch war
jahrelang nicht mehr quelloffen und ist es seit 2024 zusätzlich unter der AGPL
wieder. Verlässlich frei und
permissiv lizenziert bleiben unter anderem PostgreSQL, OpenSearch, Meilisearch,
Varnish und Nginx – die Rust-, Go- und JVM-Frameworks dieser Seite ohnehin.

## Was vorher geklärt sein muss

Die Framework-Frage lässt sich nicht isoliert beantworten. Vorher gehören einige
Dinge geklärt: Wird der Bestand überwiegend **gelesen** oder viel **geschrieben**?
Bestehen die Inhalte aus freien Textblöcken (Markdown) oder aus **relationalen
Strukturen** – festen Feldern mit vielen Verknüpfungen zwischen Tabellen? Soll ein
**Fertigsystem** wie Drupal die Grundlage sein oder ein selbst gebauter
Schichten-Aufbau? Je nach Antwort kommen ganz andere Kandidaten in Frage. Die
technischen Möglichkeiten eines selbst gebauten Aufbaus zeigt
[Ein Wissenssystem selbst bauen](wissenssystem-selbst-bauen.md). Diese Fragen zu
beantworten ist die Voraussetzung, nicht das Ergebnis der Sprachwahl.

## Drei Familien auf einen Blick

Qualitative Einordnung, keine Zahlen und kein Sieger.

| Familie | Garbage Collector | Startzeit / Arbeitsspeicher | Reifegrad | Lizenz | Oft genannte Stärke |
|---|---|---|---|---|---|
| **Rust** (Axum, Actix-web) | Nein (Prüfung beim Compilieren) | schneller Start, sparsam | jung (Axum ab 2021, häufige Brüche in 0.x) | permissiv (MIT bzw. MIT/Apache 2.0) | Speichereffizienz, keine GC-Pausen |
| **Go** (Gin, Chi, Fiber) | Ja, überwiegend nebenläufig, nicht pausenfrei | schneller Start, sparsam | produktionsreif seit 2012 | permissiv (MIT) | Nebenläufigkeit über Goroutinen; Ruf als zügig in der Entwicklung |
| **JVM** (Spring Boot, Quarkus, Micronaut) | Ja, mit Stop-the-World-Anteilen | klassisch: langsamer Start, mehr Speicher; mit Native Image deutlich schlanker | Spring Framework seit 2003 / Spring Boot seit 2014; Quarkus/Micronaut jung | permissiv (Apache 2.0) | großes Ökosystem, Werkzeuge, Native-Image-Option |

## Was heißt das für dieses Wiki?

mdBook mit Git und Markdown ist „Docs as Code": kein Web-Framework, keine
Datenbank, kein Anwendungs-Server. Das passt zum überschaubaren Bestand von rund
sechzig Artikeln und zur Zusammenarbeit mit KI, weil alle Inhalte einfache
Textdateien sind. Erst wenn das Projekt einmal auf zehntausende oder Millionen
Artikel wüchse, käme ein echtes Wiki-System oder ein zusätzlicher Suchverbund in
Frage – und dann wären die Fragen dieser Seite zu stellen: welche Sprach-Familie,
welche Datenbank-Architektur, welche Cache-Schicht. Einen fertigen, bewährten
Standard-Aufbau für Millionen-Wikis gibt es dabei nicht; öffentlich
nachvollziehbaren Großbetrieb hat vor allem MediaWiki bei der Wikimedia-Stiftung
(siehe [Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md)).

Der eigentliche eigene Weg dieses Projekts ist ohnehin kein bestimmtes Programm,
sondern die geregelte Zusammenarbeit von Mensch und KI – beschrieben unter
[Co-Wiki: Mensch & KI](co-wiki.md) und [LLM Wiki](llm-wiki.md).

## Verwandte Seiten

- [Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md) – die vier Familien
  von Wissenssystemen (übergeordnete Ebene)
- [Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md) – technischer
  Tiefgang zu Datenbank, Cache und Suche
- [CMS im Vergleich](cms-im-vergleich.md) – fertige CMS an den Zielen dieses
  Projekts
- [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)
  – Übersicht und Fachwörter-Liste
- [Wiki-Programme im Vergleich](wikis-im-vergleich.md) ·
  [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md) –
  Schwesterseiten
- [Co-Wiki: Mensch & KI](co-wiki.md) · [LLM Wiki](llm-wiki.md) – der agentische
  Ansatz dieses Projekts

## Quellen

Frameworks und Laufzeit:

- [axum – GitHub](https://github.com/tokio-rs/axum)
- [Tokio – „Announcing axum"](https://tokio.rs/blog/2021-07-announcing-axum)
- [Tokio – Tutorial](https://tokio.rs/tokio/tutorial)
- [actix-web – GitHub](https://github.com/actix/actix-web)
- [Gin – GitHub](https://github.com/gin-gonic/gin)
- [Chi – GitHub](https://github.com/go-chi/chi)
- [Fiber – GitHub](https://github.com/gofiber/fiber)
- [The Rust Programming Language – What Is Ownership?](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)
- [A Guide to the Go Garbage Collector](https://go.dev/doc/gc-guide)
- [Effective Go – Goroutines](https://go.dev/doc/effective_go#goroutines)
- [Go – FAQ](https://go.dev/doc/faq)
- [Java – Garbage Collection Tuning Guide (Oracle)](https://docs.oracle.com/en/java/javase/21/gctuning/introduction-garbage-collection-tuning.html)
- [Quarkus – Container First](https://quarkus.io/container-first/)
- [Quarkus – Building a Native Executable](https://quarkus.io/guides/building-native-executable)
- [Micronaut – GraalVM](https://docs.micronaut.io/latest/guide/#graal)
- [Spring Boot – Native Image](https://docs.spring.io/spring-boot/reference/packaging/native-image/index.html)
- [Vergleichsprojekt GraalVM: Quarkus/Micronaut/Spring Boot](https://github.com/ivangfr/graalvm-quarkus-micronaut-springboot)
- [Spring Framework – Wikipedia](https://en.wikipedia.org/wiki/Spring_Framework)
- [TechEmpower Framework Benchmarks](https://www.techempower.com/benchmarks/)
- [TechEmpower Framework Benchmarks – GitHub](https://github.com/TechEmpower/FrameworkBenchmarks)

Architektur und Last:

- [MediaWiki – Manual: MediaWiki architecture](https://www.mediawiki.org/wiki/Manual:MediaWiki_architecture)
- [Wikitech – MediaWiki at WMF](https://wikitech.wikimedia.org/wiki/MediaWiki_at_WMF)
- [MediaWiki – Extension: CirrusSearch](https://www.mediawiki.org/wiki/Extension:CirrusSearch)
- [Martin Kleppmann – Designing Data-Intensive Applications](https://dataintensive.net/)

Datenbank:

- [PostgreSQL – Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)
- [Citus Data – Understanding partitioning and sharding in Postgres and Citus](https://www.citusdata.com/blog/2023/08/04/understanding-partitioning-and-sharding-in-postgres-and-citus/)
- [Citus – GitHub](https://github.com/citusdata/citus)
- [ScyllaDB – Why We're Moving to a Source Available License](https://www.scylladb.com/2024/12/18/why-were-moving-to-a-source-available-license/)
- [Cockroach Labs – Licensing FAQs](https://www.cockroachlabs.com/docs/stable/licensing-faqs)
- [InfoQ – Concerns Rise as CockroachDB Ends Core Free Edition](https://www.infoq.com/news/2024/09/cockroachdb-license-concerns/)

Suche und Cache:

- [Elastic – Elasticsearch is Open Source, Again](https://www.elastic.co/blog/elasticsearch-is-open-source-again)
- [OpenSearch – Startseite](https://opensearch.org/)
- [OpenSearch – Moves to the Linux Foundation](https://opensearch.org/blog/opensearch-moves-to-linux-foundation/)
- [Meilisearch – Known limitations](https://www.meilisearch.com/docs/learn/resources/known_limitations)
- [Redis – Redis is Open Source, Again](https://redis.io/blog/redis-is-open-source-again/)
- [Linux Foundation – Launches Open Source Valkey Community](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community)
- [DragonflyDB – License](https://www.dragonflydb.io/docs/about/license)
- [Varnish Cache – Startseite](https://varnish-cache.org/)
- [Nginx – Lizenz](https://nginx.org/LICENSE)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
