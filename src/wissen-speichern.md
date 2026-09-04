# Wissen speichern

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Wissen speichern heißt: Texte so ablegen, dass man sie in vielen Jahren
noch lesen, durchsuchen und weiterverwenden kann. Für ein Wiki wie dieses
kommen zwei Wünsche dazu. Erstens soll der ganze Textbestand frei im
Internet nutzbar bleiben, also für jeden herunterladbar und kopierbar.
Zweitens sollen dabei keine Daten über die Leserinnen und Leser
gespeichert werden – keine Konten, keine Cookies, kein Mitschreiben, wer
was liest. Diese Seite erklärt die Grundbegriffe für Einsteiger: Was
gehört in einen guten Artikel, wo legt man ihn ab, wie findet man ihn
wieder, und wie gibt man alles weiter, ohne Nutzerdaten mitzugeben.

Es geht hier nur um die Konzepte. Den Vergleich der vier großen Familien
von Wissenssystemen bringt
[Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md), den
technischen Eigenbau Schicht für Schicht
[Ein Wissenssystem selbst bauen](wissenssystem-selbst-bauen.md). Diese
Seite doppelt beides bewusst nicht.

## Was einen guten Wissensartikel ausmacht

### Faustregel: ein Thema in zwei, drei Sätzen

Vor dem Speichern steht das Schreiben. Eine bewährte Regel in diesem
Projekt: Wenn sich der Kern eines Artikels nicht in zwei bis drei Sätzen
sagen lässt, steckt mehr als ein Thema darin – dann sollte man ihn
aufteilen. Das ist wie ein Schulranzen: Passt nichts mehr rein, nimmt man
ein zweites Fach. Ein enger Zuschnitt macht den Artikel leichter zu
finden, zu pflegen und für eine Suchmaschine oder eine KI zu verarbeiten.
Das ist eine Projekt-Faustregel, kein offizieller Standard; sie deckt
sich aber mit der Praxis, jeder Seite eine einzeilige Zusammenfassung
voranzustellen.

### Aufbau: Struktur, Schritte, Tabellen

Ein guter Artikel hat eine feste Form: ein kurzer Einstieg, der Thema und
Abgrenzung nennt, dann benannte Abschnitte mit sprechenden Überschriften.
Für praktische Abläufe eignet sich eine Schritt-für-Schritt-Liste wie ein
Kochrezept. Für Fragen mit mehreren Möglichkeiten – „Welche Ablage nehme
ich wofür?" – eignet sich eine Tabelle, weil man dort Zeile für Zeile
vergleichen kann. Alle Geschwisterseiten dieses Wikis folgen diesem
Muster.

## Drei Wege, Wissen zu speichern

Für die eigentliche Ablage gibt es drei gängige Wege. Sie schließen sich
nicht aus – oft nutzt ein Projekt mehrere gleichzeitig.

### Markdown und Textdateien – für Menschen gemacht

**Markdown** ist ein einfaches Notizformat: normaler Text mit wenigen
Sonderzeichen, etwa `#` für eine Überschrift oder `*` für kursiv. Eine
strenge, eindeutige Fassung davon heißt **CommonMark**; sie legt mit über
500 Beispielen genau fest, wie die Zeichen zu deuten sind.

Das Bild dazu: eine Schachtel mit Notizkarten, eine Karte je Seite – man
kann jede Karte herausnehmen, lesen, kopieren und woanders einordnen.

- **Stärken:** Für Menschen und Maschinen gut lesbar. Versionierbar mit
  **Git**, einer Versionsverwaltung (Zeitmaschine für jede Änderung).
  Keine Datenbank nötig.
- **Schwächen:** Keine feine Rechteverwaltung. Bei zehntausenden Dateien
  und vielen Autoren wird der Ordner unübersichtlich, das Bauen dauert
  länger, und Änderungen an derselben Datei muss jemand von Hand
  zusammenführen.

Verwandte Notizformate sind Wiki-Text (MediaWiki), reStructuredText
(Sphinx) und AsciiDoc (Antora).

### SQL-Datenbank – für schnelle, exakte Suche

Eine **Datenbank** ist ein Programm, das große Datenmengen sortiert
speichert und schnell durchsuchbar hält. Das Bild dazu: ein alphabetisch
geordneter Karteikasten mit Registerreitern – man blättert nicht alles
durch, sondern springt direkt zum richtigen Buchstaben.

Zwei bekannte kostenlose Vertreter: **SQLite** ist eine serverlose
Datenbank in einer einzigen Datei – gedacht als Ersatz für das einfache
Öffnen einer Datei, nicht für riesige Firmen-Systeme. **PostgreSQL**
arbeitet nach dem Client-Server-Prinzip: ein Server läuft dauerhaft,
viele Nutzer greifen gleichzeitig zu, die Sicherung ist aufwendiger als
das Kopieren einer Datei.

- **Stärken:** Schnell auch bei sehr vielen Seiten. Viele Autoren können
  gleichzeitig schreiben. Exakte Filter nach Titel, Schlagwort oder
  Datum. Eingebaute Rechteverwaltung.
- **Schwächen:** Bei PostgreSQL läuft ein Server, den jemand betreuen
  muss. Der Inhalt ist nicht „einfach lesbar" wie eine Textdatei. Eine
  Volltextsuche quer über Millionen Artikel direkt in der Datenbank wird
  langsam.

### Vektorspeicher und RAG – Suche nach Bedeutung

Beim dritten Weg wird jeder Textabschnitt in eine lange Zahlenreihe
übersetzt, ein sogenanntes **Embedding** oder **Vektor**. Man kann sich
das wie Koordinaten vorstellen: Texte mit ähnlicher Bedeutung landen nah
beieinander. „Auto", „Kraftfahrzeug" und „Pkw" liegen dicht zusammen,
obwohl kein Buchstabe übereinstimmt.

Der Ablauf: Das System zerlegt den langen Text in Stücke (**Chunking**),
jedes Stück bekommt einen Vektor, alle Vektoren wandern in einen
**Vektorspeicher**. Kommt eine Frage, sucht das System die nächsten
Nachbarn dieser Frage und gibt die gefundenen Textstellen einem großen
Sprachmodell – kurz **LLM** – als Hintergrund mit. Dieser Ablauf heißt
**RAG**; sinngemäß: erst nachschlagen, dann antworten.

Offene Bausteine dafür sind zum Beispiel `pgvector` (eine PostgreSQL-
Erweiterung), OpenSearch, Meilisearch oder RAGFlow.

- **Stärken:** Findet nach Bedeutung statt nach exakten Wörtern. Gut für
  Fragen in Alltagssprache. Grundlage für KI-Antworten mit Quellenbezug.
- **Schwächen:** Zusätzliche Technik, die gepflegt werden muss. Die
  Vektoren müssen berechnet und bei Änderungen neu berechnet werden. Der
  richtige Zuschnitt der Chunks ist heikel. Der Speicherbedarf liegt grob
  bei wenigen bis mehreren zehn Gigabyte je Million Vektoren.

RAG ist nicht dasselbe wie ein KI-gepflegtes Wiki. RAG sucht bei jeder
Frage neu über die Rohdaten. Ein LLM-Wiki baut daraus eine dauerhafte
Markdown-Zwischenschicht – siehe [LLM Wiki](llm-wiki.md).

## Wann welche Ablageform?

| Ablageform | Beste für | Nicht so gut für | Beispiel |
|---|---|---|---|
| Markdown / Textdateien | überschaubare Bestände, freie Weitergabe, Git-Versionierung, KI-Zugriff | zehntausende Dateien, viele gleichzeitige Autoren, feine Rechte | dieses Wiki (mdBook) |
| SQL-Datenbank | viele Seiten, viele Autoren, exakte Filter nach Feldern | einfache Lesbarkeit der Rohdaten, Volltext über Millionen Artikel in der DB | MediaWiki hinter Wikipedia |
| Vektorspeicher (RAG) | Bedeutungssuche, Fragen in Alltagssprache, KI-Antworten mit Quellen | knappe Technikpflege, exakte Wort-für-Wort-Treffer | KI-Assistent über einem Dokumentbestand |

## Wissen wiederfinden – Suchstrategien

Zum Speichern gehört das Wiederfinden. Auch hier gibt es drei
Grundverfahren, passend zu den drei Ablageformen.

### Dateisuche und grep – schnell, lokal, exakt

Auf dem eigenen Rechner findet die Dateisuche eines Editors – oder das
Kommandozeilen-Werkzeug **grep** – eine exakte Zeichenkette in Sekunden,
quer über tausende Dateien. Gut für Menschen, die die Texte ohnehin lokal
vorliegen haben, etwa bei der Redaktionsarbeit. Es findet nur, was genau
so geschrieben steht.

### SQL-Volltextsuche – Websites mit vielen Artikeln

Datenbanken können einen **Volltextindex** anlegen, ein eingebautes
Stichwortverzeichnis über alle Texte (bei SQLite heißt die Funktion FTS5,
PostgreSQL bringt eine eigene Volltextsuche mit). Das trägt gut von
tausenden bis in den Millionenbereich. Die Grenze: Eine Suche direkt in
der Datenbank über Millionen Artikel wird langsam. Große Websites stellen
dann einen eigenen Suchdienst daneben (ausführlich erläutert auf
[Wie CMS mit Millionen Artikeln umgehen](cms-millionen-artikel.md)).

### Semantische Vektorsuche – Bedeutung statt Wort

Die Vektorsuche findet Texte nach Bedeutung. Die Frage „Wie behalte ich
meine Notizen, wenn mein Laptop kaputtgeht?" führt auch zu einem Text
über „Backups", obwohl das Wort in der Frage nicht vorkommt. Das ist gut
für Fragen in Alltagssprache und die Grundlage für KI-Antworten mit
Quellen. Eine **Hybrid-Suche** kombiniert Stichwort- und Bedeutungssuche.

Ergänzend: mdBook und Material for MkDocs bringen eine Volltextsuche mit,
die im Browser läuft. Sehr große Wikis suchen dagegen über einen
getrennten Suchdienst statt über die Datenbank.

## Wann welche Suchstrategie?

| Suchstrategie | Beste für | Nicht so gut für | Passt zu welcher Ablageform |
|---|---|---|---|
| Dateisuche / grep | lokale Redaktionsarbeit, exakte Zeichenketten | Suche über eine Website, Synonyme und Umschreibungen | Markdown / Textdateien |
| SQL-Volltextsuche | Websites mit tausenden bis Millionen Artikeln, Feldfilter | Volltext über Millionen direkt in der DB, Bedeutungssuche | SQL-Datenbank |
| Semantische Vektorsuche | Fragen in Alltagssprache, Synonyme, KI-Antworten | exakte Wort-für-Wort-Treffer, minimaler Technikaufwand | Vektorspeicher (RAG) |

## Wissen exportieren – ohne Nutzerdaten

### Statische Auslieferung: frei nutzbar, ohne Nutzerkonten

Dieses Wiki wird einmal aus Textdateien zu festem HTML gebaut. Danach
zeigt der Server die Seiten nur noch an. Es gibt keine Datenbank im
Betrieb, keine Nutzerkonten, keine Registrierung und keine Bearbeitung
durch Besucher über die Website. Server-Protokolle entstehen nur beim
Hoster (hier GitHub Pages). Die Folge: Der gesamte Textbestand ist frei
herunterladbar und kopierbar.

Damit das gefahrlos möglich ist, sollten die Inhalte frei von
persönlichen Daten sein – also keine privaten Namen, E-Mail-Adressen oder
Zugangsdaten im Text. Autoren-Konten und Passwörter gehören ohnehin nicht
in den Inhalt, sondern in ein getrenntes System. Was dieses Wiki dazu
regelt, steht auf [Datenschutz](datenschutz.md).

### Welches Exportformat?

Das Ziel: Der komplette Bestand lässt sich in eine einzige,
datenbank-neutrale, lesbare Datei exportieren.

- **PDF:** Schlecht weiterverwendbar, weil das Layout fest eingebrannt
  ist und sich der Text nur mühsam herauslösen lässt.
- **HTML:** Gut lesbar und überall anzeigbar, aber schlecht
  weiterzubearbeiten, weil viel Layout-Ballast im Weg steht. Es ist das
  Endprodukt der Website-Generatoren.
- **XML, JSON, YAML oder eine REST-Schnittstelle:** Strukturiert, von
  Mensch und Programm verstehbar – die gute Wahl für einen vollständigen,
  wiederverwendbaren Export.
- **Rohes Markdown-Archiv:** Der Markdown-Ordner selbst ist die
  Sicherungsdatei. Einfacher geht Langzeitsicherung kaum.

Ein konkretes Beispiel ist der XML-Export von MediaWiki: Er enthält die
Seiten, ihre Änderungsgeschichte und die Benutzernamen der Autoren, aber
keine Konten, Passwörter, E-Mail-Adressen oder Bilddateien.

| Format | lesbar | bearbeitbar | strukturiert | zur Langzeitsicherung | Beispiel |
|---|---|---|---|---|---|
| PDF | ja | schlecht | nein | schlecht | gedrucktes Handbuch |
| HTML | ja | schlecht | teils | mäßig | fertige Website |
| XML / JSON / YAML / REST | teils | ja | ja | gut | MediaWiki-XML-Export |
| Rohes Markdown-Archiv | ja | ja | teils | sehr gut | der `src/`-Ordner dieses Wikis |

PDF-/HTML-Wertung: Einordnung der Redaktion.

## Chunk-Länge für die KI-Suche (RAG)

Wer einen Vektorspeicher aufbaut, muss lange Texte in Stücke schneiden.
Die wichtigste Regel ist inhaltlich: **ein Gedanke oder ein Arbeitsschritt
pro Chunk**. Ein Stück soll für sich verständlich bleiben.

Zur Länge kursieren Faustzahlen. Manche Empfehlungen nennen etwa 300 bis
500 Wörter, andere eher 256 bis 512 Token, dazu 10 bis 25 Prozent
Überlappung zwischen benachbarten Stücken. Das sind nur grobe
Anhaltspunkte – der beste Zuschnitt hängt vom Sprachmodell und von der
Art der Fragen ab. Eine feste Gleichung „so viele Wörter sind so viele
Token" gibt es nicht; ein Token ist im Schnitt etwas kürzer als ein Wort,
und im Deutschen mit seinen langen zusammengesetzten Wörtern ist das
Verhältnis noch ungünstiger. Mehr dazu steht auf
[Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md).

## Werkzeuge – kurze Orientierung

Zu jedem der drei Wege gibt es fertige Programme – hier nur eine
Einordnung, die ausführlichen Vergleiche stehen auf den
Geschwisterseiten.

- **Notiz-Apps:** **Obsidian** ist eine lokale, dateibasierte Markdown-
  App, stark im Verlinken von Notizen. **Logseq** arbeitet als Outliner
  (verschachtelte Stichpunkte) und eignet sich als persönliche
  Wissensbasis. Zum Veröffentlichen solcher Notizen siehe
  [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md).
- **Website-Generatoren:** Hugo, Sphinx, MkDocs, Astro Starlight und
  Quartz bauen aus Textdateien statische Websites. Der Vergleich steht auf
  [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md).
- **Wiki-Systeme:** **MediaWiki** ist das große System hinter Wikipedia,
  ausgelegt auf viele Autoren gleichzeitig und mit eigener Datenbank.
  Siehe [Wiki-Programme im Vergleich](wikis-im-vergleich.md).
- **Editor:** **VS Code** ist ein verbreiteter Texteditor zum Bearbeiten
  der Markdown-Dateien – kein Ablagesystem, sondern das Werkzeug davor.

## Was heißt das für dieses Wiki?

Dieses Wiki speichert sein Wissen als Markdown-Dateien in einem Git-Lager
und baut daraus mit **mdBook** eine statische Website – „Docs as Code",
also kein Framework und keine Datenbank im Betrieb. Für rund sechzig
Artikel plus die Zusammenarbeit mit KI ist das die passende Grundlage. Es
gibt keine eigenen Cookies, kein Tracking, keine Registrierung und keine
Bearbeitung durch Besucher; die Versionsgeschichte steckt in Git, die
Lizenz ist CC BY-SA 4.0, der ganze Textbestand ist frei kopierbar. Ein
Vektorspeicher mit RAG kommt nur in der Entwurfsphase zum Einsatz, wenn
die KI recherchiert; dauerhaft gespeichert wird immer das Markdown-Wiki.
Wie dieser Aufbau bei starkem Wachstum aussähe, steht auf
[Ein Wissenssystem selbst bauen](wissenssystem-selbst-bauen.md).

## Verwandte Seiten

- [Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md) – die
  vier großen Familien aus der Vogelperspektive
- [Ein Wissenssystem selbst bauen](wissenssystem-selbst-bauen.md) – der
  technische Eigenbau Schicht für Schicht
- [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md) –
  Werkzeuge, die aus Markdown eine Website bauen
- [Wiki-Programme im Vergleich](wikis-im-vergleich.md) – MediaWiki und
  Alternativen, XML-Export
- [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)
  – Zielliste und Fachwörter-Liste
- [Co-Wiki: Mensch & KI](co-wiki.md) · [LLM Wiki](llm-wiki.md) · [Neue
  Artikel aus Rohfassungen erstellen](neue-artikel-erstellen.md) – der
  Ablauf, mit dem die Artikel hier entstehen und gepflegt werden

## Quellen

- [CommonMark](https://commonmark.org/) ·
  [CommonMark-Spezifikation (GitHub)](https://github.com/commonmark/commonmark-spec)
  · [Smashing Magazine – CommonMark: A Formal Specification For Markdown](https://www.smashingmagazine.com/2020/12/commonmark-formal-specification-markdown/)
- [SQLite – About](https://www.sqlite.org/about.html) ·
  [SQLite – FTS5](https://www.sqlite.org/fts5.html)
- [PostgreSQL – Full Text Search](https://www.postgresql.org/docs/current/textsearch.html)
- [pgvector – GitHub](https://github.com/pgvector/pgvector)
- [Unstructured – Semantic Chunking for RAG](https://unstructured.io/insights/semantic-chunking-for-rag)
  · [Multimodal – Semantic Chunking for RAG](https://www.multimodal.dev/post/semantic-chunking-for-rag)
  · [Firecrawl – Best Chunking Strategies for RAG](https://www.firecrawl.dev/blog/best-chunking-strategies-rag)
- [Prem AI – RAG Chunking Strategies: The 2026 Benchmark Guide](https://www.premai.io/blog/rag-chunking-strategies-the-2026-benchmark-guide/)
  · [Machine Learning Plus – Optimizing RAG Chunk Size](https://machinelearningplus.com/gen-ai/optimizing-rag-chunk-size-your-definitive-guide-to-better-retrieval-accuracy/)
- [MediaWiki – Help:Export](https://www.mediawiki.org/wiki/Help:Export)

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
