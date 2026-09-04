# Ein Wissenssystem selbst bauen

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Die Seite [Webframeworks im Vergleich](webframeworks-im-vergleich.md) sagt: Das
Framework ist nur der **Dirigent**, die eigentliche Last liegt in der Schicht
darunter. Diese Seite geht eine Ebene tiefer und dreht die Frage um: Wenn ein
Projekt seinen Auslieferungs- **und** seinen Redaktionsstack wirklich selbst
baut – was schenkt einem jedes große Ökosystem an fertigen Bausteinen? Das ist
der technische Tiefgang unter der Vergleichsseite, so wie
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md) der Tiefgang
unter [CMS im Vergleich](cms-im-vergleich.md) ist. Betrachtet werden zwei
Ausbaustufen – (1) ein durchsuchbares Wissenssystem mit KI-Anbindung und (2) ein
vollwertiges CMS mit Redaktions-Oberfläche.

Betrachtet werden nur die vier Ökosysteme, die bei sehr großen Beständen erprobt
sind: **ASP.NET Core** (Sprache C#), die **JVM** (Java und verwandte Sprachen),
**Go** und **Rust**. **Python** und **Node.js** kommen hier nicht als
Auslieferungs-Framework vor – nicht weil sie untauglich wären, sondern weil ihre
Stärke woanders liegt: Python taucht im LLM-Teil weiter unten als
Bibliotheks-Ökosystem auf, und für ein fertiges CMS sind Django/Wagtail (Python)
und die Node-Headless-CMS oft der kürzere Weg.

Dieses Wiki nutzt heute mdBook mit Git und Markdown – „Docs as Code", also gar
kein Framework und keine Datenbank. Die Grundkonzepte, wie Wissensprojekte ihre
Daten speichern und durchsuchbar halten, erklärt die Seite
[Wissen speichern](wissen-speichern.md). Alles Folgende ist Einordnung und Ausblick
und greift erst, wenn ein Projekt in die Nähe von Millionen Artikeln käme. Einen
fertigen, bewährten Standard-Aufbau für Millionen-Wikis gibt es dabei nicht.

> Fachwörter wie *Open Source*, *Schnittstelle* (*API*), *REST*, *GraphQL*,
> *Datenbank*, *Markdown*, *Git*, *Node.js*, *MCP* oder *RAG* sind in
> [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md#fachwörter-kurz-erklärt)
> in einer kurzen Liste erklärt.

## Was bei allen gleich bleibt

Die schwere Arbeit bei Millionen Artikeln liegt nicht im Framework, sondern in
der Schicht darunter – und die sieht in allen vier Ökosystemen ähnlich aus. In
jedem gilt: fürs massenhafte **Lesen** keine schwere Abbildungsschicht zwischen
Datenbank und Programm verwenden. Eine **objektrelationale Abbildung** (englisch
*Object-Relational Mapping*, ORM) behandelt Datenbankzeilen als Programmobjekte
und verfolgt jede Änderung mit; für reine Lese-Massen ist dieser
Änderungs-Nachlauf unnötiger Ballast. Jedes Ökosystem hat einen schlanken Weg
daran vorbei: in .NET `AsNoTracking()` oder die schmale Bibliothek Dapper, in der
JVM-Welt rein lesende Transaktionen oder jOOQ, in Go `database/sql` mit `pgx` oder
`sqlc`, in Rust `sqlx`. Alles Weitere – große Tabellen aufteilen, Verbindungen
bündeln, Lese-Kopien, die Suche auslagern, ein Vorschalt-Cache oder CDN – ist vom
Framework unabhängig und steht ausführlich auf
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md). Wie sich die
Lizenzlage bei Speicher- und Such-Bausteinen 2024/25 verschoben hat, steht auf
[Webframeworks im Vergleich](webframeworks-im-vergleich.md).

## Die vier großen Sprach-Ökosysteme

Kurze Steckbriefe – es geht um den selbst betriebenen Auslieferungs-Server in
einer dieser Sprachen. Die Mechanik der Speicherverwaltung – ob eine Sprache
einen **Garbage Collector** hat (ein Hintergrundprogramm, das ungenutzten
Speicher automatisch einsammelt und dabei kurze Pausen verursachen kann) – sowie
Reifegrad und Durchsatz im Detail stehen für JVM, Go und Rust auf
[Webframeworks im Vergleich](webframeworks-im-vergleich.md); hier steht ASP.NET
Core im Vordergrund, das dort nicht vorkommt. Die folgenden Steckbriefe
verweisen darauf nicht noch einmal einzeln.

### ASP.NET Core (C#)

ASP.NET Core ist das quelloffene Web-Framework von Microsoft, unter der
permissiven MIT-Lizenz. Es bringt den eigenen Webserver **Kestrel** und die
**Minimal APIs** mit – eine knappe Schreibweise für einzelne HTTP-Endpunkte. Wie
JVM und Go hat die .NET-Laufzeit einen Garbage Collector. Als Gegenstück zum
Native Image der JVM (mit dem Werkzeug GraalVM) gibt es **Native AOT**
(*Ahead-of-Time*, „vorab übersetzt"): ein vorab in Maschinensprache übersetztes,
eigenständiges Programm mit schnellem Start und geringem Arbeitsspeicherbedarf.
Einschränkung laut Microsoft-Dokumentation: Nicht jede Bibliothek ist
AOT-tauglich. Als Praxisbeispiel für .NET unter Last gilt Stack Overflow; die
öffentlich dokumentierten Zahlen stammen allerdings aus dem Jahr 2016 (rund
209 Millionen Anfragen pro Tag auf etwa 25 Servern, damals noch ASP.NET MVC 5) –
sie belegen qualitativ einen Betrieb in Millionengröße, mehr nicht.

### JVM (Java)

Auf der Java Virtual Machine laufen Spring Boot (der De-facto-Standard) sowie die
jüngeren Quarkus und Micronaut, alle unter Apache 2.0. Der Garbage Collector der
JVM hat Stop-the-World-Anteile; im klassischen Betrieb ist der
Arbeitsspeicherbedarf höher, mit einem GraalVM Native Image deutlich niedriger.

### Go

Go bringt **Goroutinen** mit – sehr leichtgewichtige „Fäden" für viele
gleichzeitige Anfragen – und ist seit Version 1.0 im Server- und Netzwerkbereich
fest etabliert. Sein Garbage Collector arbeitet überwiegend nebenläufig, ist aber
nicht ganz pausenfrei. Große Anwendungen mit Redaktions-Oberfläche wie
Gitea/Forgejo oder Mattermost sind in Go geschrieben; öffentliche
Millionen-Artikel-Referenzzahlen gibt es dafür nicht.

### Rust

Rust hat keinen Garbage Collector: Der Compiler entscheidet schon beim Übersetzen
anhand fester Regeln (dem *Ownership*-Modell), wann Speicher frei wird – dadurch
keine GC-Pausen, dafür eine steile Lernkurve und eine junge Community.
Web-Frameworks sind Axum und Actix-web. Discord hat 2020 einen einzelnen Dienst
wegen kurzer, aber regelmäßiger GC-Latenz von Go auf Rust umgestellt – ein
Dienst, nicht die ganze Plattform. Als weiteres Rust-Projekt unter Last gilt
Cloudflares **Pingora** (Apache 2.0), das Cloudflare-intern nginx ersetzt; das
ist ein Baukasten für Proxy-Dienste, kein Artikel-Stack.

## Ausbaustufe 1 — Wissenssystem mit LLM und RAG

Die erste Ausbaustufe ist ein durchsuchbares Wissenssystem: Bedeutungssuche, ein
Nachschlage-Ablauf für KI-Antworten (**RAG**, „erst nachschlagen, dann
antworten") und eventuell Agenten. Auf dem Auslieferungs-Ökosystem sitzt dafür
eine LLM-Schicht aus SDKs (fertigen Programmbibliotheken der Modell-Anbieter),
RAG-Orchestrierung und der Anbindung an die Bedeutungssuche.

Zwei Dinge sind für alle Sprachen gleich. Erstens der **Vektor-Speicher**: Für
rund eine Million Artikel reicht die PostgreSQL-Erweiterung `pgvector` in
derselben Datenbank – ausgeführt auf
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md). Zweitens
**MCP** (Model Context Protocol), die offene Andockstelle zwischen Modell und
Werkzeugen, hat offizielle SDKs quer durch alle hier genannten Sprachen und ist
damit **kein** Auswahlkriterium (Details zu MCP auf [LLM Wiki](llm-wiki.md)).

Wo die Ökosysteme sich unterscheiden, ist die Reife der RAG-Werkzeuge darüber.
Die folgende Reihenfolge ist eine Einschätzung nach unserer Recherche, kein
Messergebnis.

- **Python** – die reichste Auswahl: LangChain (Version 1.0 seit Oktober 2025),
  dazu LlamaIndex, Haystack und die offiziellen SDKs `anthropic` und `openai`.
  Nach verbreiteter Erfahrung landen neue Modell-Funktionen hier zuerst –
  eine Erfahrungsaussage, keine Regel.
- **TypeScript/Node.js** – gut ausgestattet: Das Vercel AI SDK (Version 5 seit
  Juli 2025) gilt als stabil, dazu LangChain.js und Mastra.
- **.NET** – `Microsoft.Extensions.AI` (allgemein verfügbar seit Mai 2025) bietet
  eine einheitliche Schnittstelle über verschiedene Modelle. Semantic Kernel ist
  stabil, doch für neue Projekte lenkt Microsoft auf dessen Nachfolger, das
  **Microsoft Agent Framework**; **Kernel Memory** führt Microsoft ausdrücklich
  als „Research project" – ein gepflegter RAG-Baustein, kein zugesichertes
  Produkt.
- **Java/JVM** – Spring AI (1.0 seit Mai 2025) gilt als stabil, LangChain4j ist
  mit der 1.x-Reihe etabliert, und Quarkus hat eine erstklassige
  LangChain4j-Erweiterung.
- **Go** – dünner bei viel RAG-Orchestrierung: offizielle SDKs `anthropic-sdk-go`
  und `openai-go`, aber `langchaingo` ist ein Community-Projekt. Das Zerlegen,
  Heraussuchen und Neu-Sortieren langer Texte baut man eher selbst – Einschätzung.
- **Rust** – am unreifsten für diese Aufgabe: `rig`, `async-openai` und das
  offizielle MCP-SDK `rmcp`. Für reine Auslieferung tauglich, für komplexe
  RAG-Ketten noch wenig Fertiges – Einschätzung.

## Ausbaustufe 2 — Ein vollwertiges CMS

Die zweite Ausbaustufe ist ein vollwertiges Redaktionssystem. Dafür kommt eine
ganze Baustein-Ebene dazu: Anmeldung und **Rollenrechte** (englisch *Role-Based
Access Control*, RBAC – wer darf was), eine Redaktions-Oberfläche (idealerweise
automatisch aus dem Datenmodell erzeugt, sodass man die Eingabemasken nicht von
Hand baut – kurz „Auto-Admin"), eine Medien-Bibliothek mit Bildbearbeitung, ein
Freigabe-Workflow (Entwurf → Prüfung → Veröffentlichung), Versionierung und
Hintergrund-Aufgaben. Wie viele dieser Bausteine fertig vorliegen – und wie
sauber sie lizenziert sind – ist der eigentliche Unterschied zwischen den vier
Ökosystemen.

Die Reife-Angaben in diesem Abschnitt sind Einschätzungen nach unserer
Recherche, keine öffentlich belegten Benchmarks; die Eignung für rund eine
Million Artikel ist bei fast allen genannten Bausteinen technisch plausibel, aber
nicht mit einer Großreferenz belegt (wie schon auf den Schwesterseiten). Die
Systematik trägt die Tabelle am Ende des Abschnitts; die Absätze nennen nur, wie
weit man kommt und wo der eine Vorbehalt liegt, der in keine Tabellenzelle passt.

**.NET.** Am weitesten kommt man mit einem fertigen CMS-Framework – Orchard Core,
Piranha oder Umbraco (siehe Tabelle) –, das Anmeldung, Rollen, Workflow und Admin
schon mitbringt. Der eine Reibungspunkt sitzt bei der Bildbearbeitung:
**ImageSharp** steht unter einer Split-Lizenz (für Non-Profits mit unter
1 Mio. USD Umsatz kostenlos, ab Version 4 aber mit einem Build-Lizenzschlüssel),
während **SkiaSharp** (MIT) reibungsfrei ist.

**JVM.** Das Enterprise-Erbe zeigt sich hier am deutlichsten: **Apache Jackrabbit
Oak** – das Standard-Backend hinter Adobe AEM – ist eine hierarchische
Inhalts-Datenbank nach dem Standard **JCR** (Java Content Repository) und bringt
Versionierung, feingranulare Rechte und Volltextsuche mit; Apache Sling legt die
REST-Schicht darüber. Beim Workflow ist die Lizenzlage der Haken: **Flowable**
(Apache 2.0) ist die freie Option, während bei **Camunda** die Community Edition
von Version 7 seit Oktober 2025 abgekündigt ist (keine Sicherheits-Patches mehr)
und Version 8 nur „source available" ist und im Selbstbetrieb eine
Produktionslizenz braucht.

**Go.** Fertige Rundum-Bausteine sind seltener; am weitesten kommt **PocketBase**
(MIT), ein komplettes Backend in einer Datei (Auto-REST-API, Admin, Anmeldung,
Datei-Ablage). Die zwei Vorbehalte: Es steht weiterhin bei Version 0.x ohne
zugesicherte Aufwärtskompatibilität und ist an die eingebettete Datenbank SQLite
gebunden. Die Suche über **Bleve** bleibt eingebettet und ohne separaten Dienst –
ab welcher Bestandsgröße ein externer Suchdienst besser ist, hängt vom Fall ab
(siehe „Suche früh auslagern" auf
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md)).

**Rust.** Am wenigsten Fertiges. **Loco.rs** (Apache 2.0, „Rails für Rust", auf
Axum und SeaORM) hat am 25. Juli 2026 Version 1.0 erreicht und gilt seither als
stabil, doch die Community bleibt klein. Die eingebettete Volltextsuche
**tantivy** (MIT) ist für rund eine Million Artikel plausibel (die Suchmaschine
Quickwit baut darauf), aber ohne öffentliche Zahlen – Einschätzung. Ein
Gegenstück zu Orchard Core oder Wagtail, also ein fertiges CMS-Framework mit
Auto-Admin, gibt es nach unserer Recherche nicht.

### CMS-Bausteine der vier Ökosysteme

Qualitative Übersicht, kein Sieger. Lizenz-Kürzel in Klammern.

| Baustein | .NET | JVM | Go | Rust |
|---|---|---|---|---|
| CMS-Framework / Plattform | Orchard Core (BSD-3), Piranha (MIT), Umbraco (MIT) | Jackrabbit Oak + Sling (Apache 2.0), JHipster (Apache 2.0) | PocketBase (MIT, v0.x) | Loco.rs (Apache 2.0, 1.0) |
| Anmeldung / Rollen (RBAC) | ASP.NET Identity; OpenIddict (Apache 2.0); Duende (kommerziell, mit Community Edition) | Keycloak (Apache 2.0) | Casbin (Apache 2.0) | `axum-login` (MIT), RBAC selbst |
| Admin- / Schema-Oberfläche | in Orchard Core / Umbraco enthalten | JHipster erzeugt sie | qor5 (Einschätzung) | – (nach unserer Recherche keins) |
| Medien / Bildbearbeitung | ImageSharp (Split-Lizenz) oder SkiaSharp (MIT) | Ablage über Jackrabbit Oak | Datei-Ablage in PocketBase | `object_store`-Bibliothek |
| Freigabe-Workflow | Elsa 3 (MIT) | Flowable (Apache 2.0); Camunda mit Lizenz-/EoL-Vorbehalt | in qor5 enthalten (Einschätzung) | selbst bauen |
| Volltextsuche | Lucene.NET (Apache 2.0) | Hibernate Search (LGPL 2.1); besser extern auslagern | Bleve (Apache 2.0, eingebettet) | tantivy (MIT, eingebettet) |
| Hintergrund-Aufgaben | Quartz.NET (frei); Hangfire (Kern frei, „Pro" kostenpflichtig) | Spring Batch / Quartz / JobRunr (Kern frei) | asynq (Redis) / River (PostgreSQL), beide MIT | apalis (permissiv) |

Eine vollständig permissiv lizenzierte Zusammenstellung ist in jedem Ökosystem
möglich – man muss nur pro Zeile die freie Variante wählen: in .NET etwa
OpenIddict statt Duende und SkiaSharp statt ImageSharp, in der JVM Flowable statt
Camunda. Vor einer „voll frei"-Gesamtaussage lohnt bei einzelnen
Nischen-Bausteinen (Elsa 3, Squidex, Hibernate Search, JobRunr-Kern) ein kurzer
Blick ins jeweilige Repository.

## Ehrlich über den Tellerrand

Für „ein eigenes CMS bauen" führt an zwei Optionen kaum ein Weg vorbei, die hier
bewusst außen vor bleiben. **Django** mit **Wagtail** (Python) liefert mit
`django-admin` praktisch geschenkt eine Redaktions-Oberfläche; Wagtail steht
unter der BSD-3-Clause-Lizenz. Und die **Node.js-Headless-CMS** – Strapi,
Directus, Payload – bringen Schema-Verwaltung, API und Admin fertig mit. Zur
Auswahl unter den fertigen CMS (einschließlich der Node-Headless-Welt) siehe
[CMS im Vergleich](cms-im-vergleich.md); zur Skalierung von Django/Wagtail auf
große Bestände siehe
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md). Die vier hier
betrachteten Ökosysteme sind also vor allem dann die Wahl, wenn ohnehin ein
selbst gebauter Auslieferungs-Server in einer dieser Sprachen läuft.

## Was heißt das für dieses Wiki?

Für rund sechzig Artikel plus KI-Zusammenarbeit ist mdBook mit Git und Markdown –
Docs as Code, kein CMS, keine Datenbank – die passende Grundlage. Bei starkem
Wachstum käme eher ein echtes Wiki-System oder ein zusätzlicher Suchverbund in
Frage als ein Framework-Eigenbau. Eine Redaktions-Oberfläche würde am ehesten als
schlanker Redaktions-Aufsatz auf das Git-Lager entstehen, nicht als selbst
gebautes CMS. Der eigentliche eigene Weg dieses Projekts ist ohnehin
die geregelte Zusammenarbeit von Mensch und KI – beschrieben unter
[Co-Wiki: Mensch & KI](co-wiki.md) und [LLM Wiki](llm-wiki.md). Die vier Familien
von Wissenssystemen aus der Vogelperspektive – und warum es keinen fertigen
Standard-Stack für große Wikis gibt – behandelt
[Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md).

## Verwandte Seiten

- [Webframeworks im Vergleich](webframeworks-im-vergleich.md) – die Elternseite
  (Framework als Dirigent, GC-Mechanik der Sprach-Familien, Lizenzlage 2024/25)
- [Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md) – Skalierung,
  pgvector, Bezug zu Django/Wagtail
- [CMS im Vergleich](cms-im-vergleich.md) – fertige CMS inklusive Node-Headless
- [Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md) – die vier
  Familien, „kein Standard-Stack"
- [LLM Wiki](llm-wiki.md) · [Co-Wiki: Mensch & KI](co-wiki.md) – der agentische
  Ansatz dieses Projekts, MCP als Andockstelle
- [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)
  – Übersicht und Fachwörter-Liste
- [Wiki-Programme im Vergleich](wikis-im-vergleich.md) ·
  [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md) –
  Schwesterseiten

## Quellen

Auslieferung und Praxis:

- [ASP.NET Core – Kestrel](https://learn.microsoft.com/aspnet/core/fundamentals/servers/kestrel)
- [ASP.NET Core – Minimal APIs](https://learn.microsoft.com/aspnet/core/fundamentals/minimal-apis)
- [.NET – Native AOT deployment](https://learn.microsoft.com/dotnet/core/deploying/native-aot/)
- [Nick Craver – Stack Overflow: The Architecture – 2016 Edition](https://nickcraver.com/blog/2016/02/17/stack-overflow-the-architecture-2016-edition/)
- [High Scalability – Stack Overflow Update: 560M Pageviews A Month, 25 Servers](https://highscalability.com/stackoverflow-update-560m-pageviews-a-month-25-servers-and-i/)
- [Discord – Why Discord is switching from Go to Rust](https://discord.com/blog/why-discord-is-switching-from-go-to-rust)
- [Cloudflare – Open sourcing Pingora](https://blog.cloudflare.com/pingora-open-source/)
- [Gitea](https://gitea.io/) · [Mattermost – GitHub](https://github.com/mattermost/mattermost)
- [TechEmpower Framework Benchmarks](https://www.techempower.com/benchmarks/)
- [Entity Framework Core – Tracking vs. No-Tracking Queries](https://learn.microsoft.com/ef/core/querying/tracking)

CMS-Bausteine .NET:

- [Orchard Core – LICENSE (BSD-3-Clause)](https://github.com/OrchardCMS/OrchardCore/blob/main/LICENSE)
- [Piranha CMS – LICENSE (MIT)](https://github.com/PiranhaCMS/piranha.core/blob/master/LICENSE)
- [Umbraco CMS – LICENSE](https://github.com/umbraco/Umbraco-CMS/blob/contrib/LICENSE.md) · [Umbraco 9 Release](https://umbraco.com/blog/umbraco-9-release)
- [ASP.NET Core – Identity](https://learn.microsoft.com/aspnet/core/security/authentication/identity)
- [OpenIddict – Dokumentation](https://documentation.openiddict.com/)
- [Duende – Licensing](https://docs.duendesoftware.com/general/licensing/) · [Duende – Community Edition](https://duendesoftware.com/products/communityedition)
- [Elsa Workflows – Dokumentation](https://docs.elsaworkflows.io/)
- [Six Labors – Pricing](https://sixlabors.com/pricing/) · [Announcing ImageSharp 4.0.0](https://sixlabors.com/posts/announcing-imagesharp-400/)
- [SkiaSharp – GitHub](https://github.com/mono/SkiaSharp)
- [Hangfire](https://www.hangfire.io/) · [Quartz.NET](https://www.quartz-scheduler.net/)
- [Lucene.NET](https://lucenenet.apache.org/)

CMS-Bausteine JVM:

- [Apache Jackrabbit Oak](https://jackrabbit.apache.org/oak/) · [Apache Sling](https://sling.apache.org/)
- [JHipster](https://www.jhipster.tech/)
- [Keycloak – LICENSE](https://github.com/keycloak/keycloak/blob/main/LICENSE.txt)
- [Flowable – Open Source](https://www.flowable.com/open-source)
- [camunda-bpm-platform – GitHub](https://github.com/camunda/camunda-bpm-platform) · [Camunda – Licensing update: Camunda 8 Self-Managed](https://camunda.com/blog/2024/04/licensing-update-camunda-8-self-managed/)
- [Hibernate Search](https://hibernate.org/search/)
- [jOOQ – Licensing](https://www.jooq.org/legal/licensing)
- [Spring Batch](https://spring.io/projects/spring-batch) · [JobRunr](https://www.jobrunr.io/)

CMS-Bausteine Go:

- [PocketBase](https://pocketbase.io/) · [PocketBase – GitHub](https://github.com/pocketbase/pocketbase)
- [sqlc](https://sqlc.dev/) · [Casbin](https://casbin.org/)
- [qor5/admin – GitHub](https://github.com/qor5/admin)
- [asynq – GitHub](https://github.com/hibiken/asynq) · [River](https://riverqueue.com/)
- [Bleve](https://blevesearch.com/)

CMS-Bausteine Rust:

- [Loco 1.0.0 – Release](https://github.com/loco-rs/loco/releases/tag/v1.0.0) · [Loco – LICENSE (Apache 2.0)](https://github.com/loco-rs/loco/blob/master/LICENSE) · [loco.rs](https://loco.rs/)
- [SeaORM](https://www.sea-ql.org/SeaORM/) · [sqlx – GitHub](https://github.com/launchbadge/sqlx)
- [axum-login – GitHub](https://github.com/maxcountryman/axum-login)
- [tantivy – GitHub](https://github.com/quickwit-oss/tantivy)
- [apalis – GitHub](https://github.com/geofmureithi/apalis) · [object_store](https://docs.rs/object_store/)

LLM-Ökosystem:

- [Model Context Protocol – SDKs](https://modelcontextprotocol.io/docs/sdk)
- [.NET – AI and vector data extensions GA](https://devblogs.microsoft.com/dotnet/ai-vector-data-dotnet-extensions-ga/)
- [Microsoft Agent Framework – Overview](https://learn.microsoft.com/en-us/agent-framework/overview/)
- [Kernel Memory – GitHub](https://github.com/microsoft/kernel-memory)
- [Spring AI 1.0 GA](https://spring.io/blog/2025/05/20/spring-ai-1-0-GA-released/)
- [LangChain4j – Releases](https://github.com/langchain4j/langchain4j/releases) · [Quarkus LangChain4j](https://docs.quarkiverse.io/quarkus-langchain4j/dev/)
- [LangChain 1.0 – now generally available](https://changelog.langchain.com/announcements/langchain-1-0-now-generally-available)
- [Vercel – AI SDK 5](https://vercel.com/blog/ai-sdk-5)
- [rig – GitHub](https://github.com/0xPlaygrounds/rig) · [langchaingo – GitHub](https://github.com/tmc/langchaingo)
- [pgvector – GitHub](https://github.com/pgvector/pgvector)

Django/Wagtail (nur Bezug):

- [Wagtail – LICENSE (BSD-3-Clause)](https://github.com/wagtail/wagtail/blob/main/LICENSE)
- [Django – The Django admin site](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
