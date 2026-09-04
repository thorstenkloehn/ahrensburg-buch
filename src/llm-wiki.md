# LLM Wiki

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Diese Seite erklärt drei Dinge. Zuerst geht es um die Grundlagen: Was ist ein
**LLM** (großes Sprachmodell, die Technik hinter Chat-KI), was kann es gut, was
nicht, und wie stellt man gute Fragen. Danach geht es um ein bestimmtes Muster,
das der KI-Fachmann Andrej Karpathy im April 2026 vorgeschlagen hat: das
**LLM-Wiki**. Zum Schluss steht, wie genau dieses Ahrensburg-Wiki dieses Muster
anwendet. Vorwissen aus dem Bereich des maschinellen Lernens ist nicht nötig.

## Was ist ein LLM? (Sprachmodelle verstehen)

**LLM** ist die Abkürzung für *Large Language Model*, auf Deutsch „großes
Sprachmodell". Ein solches Programm erzeugt Text Stück für Stück. Es fügt immer
das nächste Sprach-Bruchstück an, das am wahrscheinlichsten passt – Fachleute
nennen das *Next-Token-Prediction*, also „Vorhersage des nächsten Textbausteins".
Wichtig dabei: Das Modell **schlägt nichts in einer Antwort-Datenbank nach**, es
**erzeugt** die Antwort neu. Deshalb kommt bei derselben Frage manchmal eine
andere Antwort heraus – ein kleiner Zufallsanteil ist eingebaut.

Ein LLM hat aus sehr vielen Büchern, Webseiten, Programmtexten und Anleitungen
gelernt. Dabei hat es vor allem **Sprachmuster** aufgenommen, keinen sauber
sortierten Faktenspeicher. Das erklärt auch eine unangenehme Eigenschaft: Das
Modell antwortet selbst dann souverän und flüssig, wenn es etwas gar nicht weiß.
Ein hilfreiches Bild ist: ein **belesener Assistent mit gutem Sprachgefühl und
unzuverlässigem Gedächtnis**.

Wie es dazu kommt, dass ein LLM Dinge überzeugend erfindet (sogenannte
Halluzinationen), ist ausführlich in
[Neue Artikel aus Rohfassungen erstellen](neue-artikel-erstellen.md) beschrieben.

### Begriffe A–Z

Diese Wörter tauchen im Zusammenhang mit Sprachmodellen immer wieder auf.

| Begriff | Kurz erklärt |
|---|---|
| **Agent** | Ein LLM, das mehrere Schritte hintereinander abarbeitet, Werkzeuge benutzt und Zwischenergebnisse selbst bewertet. |
| **Fine-Tuning** | Nachtraining eines Modells auf eigene Daten. Aufwendig und selten der erste Schritt. |
| **Halluzination** | Eine erfundene, aber überzeugend formulierte Angabe. |
| **Knowledge Cutoff** | Stichtag der Trainingsdaten. Was später passiert ist, kennt das Modell nur mit einer Suchfunktion. |
| **Kontextfenster** | Die Textmenge, die das Modell gleichzeitig verarbeiten kann – Frage, Anhänge und Antwort zusammen. |
| **Multimodal** | Das Modell verarbeitet nicht nur Text, sondern auch Bilder, PDFs oder Audio. |
| **Prompt** | Die Eingabe an das Modell: Frage, Anweisung, Text oder Datei. |
| **RAG** | „Erst nachschlagen, dann antworten": Passende Dokumente werden gesucht und dem Prompt beigelegt. |
| **System-Prompt** | Eine vorab gesetzte Rolle und Verhaltensregel für das Modell. |
| **Temperature** | Ein Zufallsregler: niedrig = vorhersehbar, hoch = sprunghaft. |
| **Token** | Die kleinste Verarbeitungseinheit, meist ein Wortteil. |
| **Tool / Function Calling** | Das Modell darf externe Werkzeuge aufrufen, etwa Suche, Rechner oder interne Systeme. |

Als **grobe Faustregel** wird oft „ungefähr ¾ Wort je Token" genannt. Diese Regel
stammt aus dem englischen Sprachraum; im Deutschen fällt das Verhältnis wegen der
langen zusammengesetzten Wörter ungünstiger aus. Die Zahl ist also nur ein grober
Anhaltspunkt, kein genauer Umrechnungsfaktor.

Eine kürzere Fachwort-Tabelle mit Schwerpunkt auf der Technik dahinter steht in
[Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md).

## Wofür taugt ein LLM? (Stärken und Grenzen)

**Gut geeignet** sind Sprachmodelle für Aufgaben, bei denen es auf Formulierung
und Struktur ankommt:

- Texte umformulieren, kürzen, zusammenfassen oder übersetzen.
- Erste Entwürfe schreiben: Mails, Protokolle, Gliederungen, Textbausteine.
- Fachtexte, Verträge oder Programmcode in einfacher Sprache erklären.
- Unordentliche Notizen und Daten in eine übersichtliche Form bringen.
- Ideen sammeln, Gegenargumente finden, als Sparringspartner dienen.

**Schlecht geeignet** sind sie überall dort, wo es auf geprüfte Genauigkeit
ankommt:

- Exakte Fakten, Zahlen, Zitate oder Rechtsstände ohne Quelle.
- Rechnen und Zählen ohne ein echtes Werkzeug.
- Aktuelle Ereignisse ohne Zugriff auf eine Suche.
- Entscheidungen mit rechtlichen, medizinischen oder personellen Folgen.
- Aufgaben, deren Ergebnis am Ende niemand prüft.

Die einfache Faustregel dazu: **Der Nutzen steigt mit der Fähigkeit, das Ergebnis
selbst zu beurteilen.** Wer ein Thema gut kennt, erkennt Fehler sofort und spart
viel Zeit. Wer es nicht kennt, übernimmt die Fehler ungeprüft.

## Wie man LLMs besser nutzt (Prompting-Basics)

Unabhängig vom Einsatzzweck gilt: Die Qualität der Antwort hängt stark von der
Eingabe ab. Ein paar Grundregeln helfen:

- **Kontext mitgeben:** wer fragt, für wen ist das Ergebnis, was ist vorher
  passiert.
- **Aufgabe konkret benennen** statt „mach was mit dem Text".
- **Format vorgeben:** Länge, Ton, Tabelle oder Fließtext.
- **Beispiele zeigen:** ein gutes und ein schlechtes.
- **Iterieren:** die Antwort nachschärfen, statt jedes Mal neu anzufangen.
- **Eigenes Material anhängen:** angehängte Dokumente sind zuverlässiger als das
  Gedächtnis des Modells.

Ein Beispiel macht den Unterschied deutlich. Schwacher Prompt: „Schreib eine Mail
wegen des Termins." Besserer Prompt: „Kurze, freundliche Kundenmail. Der Workshop
am 14.10. verschiebt sich krankheitsbedingt auf November. Zwei Alternativtermine
anbieten. Höchstens 120 Wörter, Sie-Form."

## Das LLM-Wiki: eine Idee von Andrej Karpathy

Am 4. April 2026 veröffentlichte der KI-Fachmann Andrej Karpathy einen kurzen
Text mit dem Namen `llm-wiki.md` als sogenannten GitHub-Gist – eine kurze,
öffentlich einsehbare Notiz auf GitHub, einer Plattform, auf der Programmiererinnen
und Programmierer ihren Code austauschen. Das ist **kein Programm**, sondern eine
Ideen- und Musterbeschreibung in Prosa, gedacht zum Einbauen in einen KI-Agenten.

Ein herkömmliches **RAG-System** sucht für eine konkrete Frage passende Stellen
in seinen Unterlagen und formuliert daraus eine Antwort. Das LLM-Wiki verfolgt
ein anderes Ziel: Aus ausgewählten Unterlagen entsteht schrittweise ein
redigierter Bestand aus miteinander verknüpften Markdown-Seiten. Spätere Fragen
können auf diesen bereits geordneten Bestand zurückgreifen. Neue Quellen führen
nicht zu einem kompletten Neubeginn, sondern zu gezielten Ergänzungen und
Korrekturen.

Der praktische Unterschied liegt damit weniger im Dateiformat als in der
Pflegearbeit. RAG ist vor allem ein Verfahren zum Auffinden von Belegstellen;
ein LLM-Wiki hält zusätzlich fest, wie die Redaktion diese Belege eingeordnet
hat. Dadurch bleibt Wissen über mehrere Arbeitssitzungen erhalten. Zugleich kann
eine falsche Einordnung dauerhaft weiterwirken, weshalb Quellenbezug,
Versionsgeschichte und menschliche Prüfung unverzichtbar sind.

Karpathys Text verweist außerdem auf einen alten Gedanken: den „Memex", ein
1945 von Vannevar Bush beschriebenes ideales Wissensgerät.

### Bausteine und redaktioneller Betrieb

Für eine Umsetzung müssen vier Aufgaben getrennt geregelt sein:

1. **Quellen bewahren:** Originale wie PDFs, Notizen oder Datensätze bleiben
   unverändert, damit jede Aussage später überprüft werden kann.
2. **Wissen ordnen:** Themenseiten fassen belegte Aussagen zusammen und
   verweisen untereinander. Eine Übersichtsseite erleichtert den Einstieg.
3. **Änderungen dokumentieren:** Neue, geänderte und verworfene Aussagen werden
   mit Zeitpunkt und Anlass nachvollziehbar festgehalten.
4. **Arbeitsregeln festlegen:** Eine eigene Anleitung bestimmt Seitenaufbau,
   Quellenstandard, Zuständigkeiten und Freigabe. In diesem Repository erfüllen
   `AGENTS.md` und `CLAUDE.md` diese Funktion.

Im Alltag wechseln sich drei Tätigkeiten ab. Bei der **Aufnahme** einer Quelle
werden nur die betroffenen Seiten ergänzt. Bei einer **Recherchefrage** sucht
der Agent zuerst im geordneten Bestand und führt die Antwort zu den Belegen
zurück. Eine regelmäßige **Bestandsprüfung** sucht schließlich nach
Widersprüchen, veralteten Angaben und verwaisten Seiten. Karpathys Gist nennt
für diese Tätigkeiten die englischen Kurzbezeichnungen *ingest*, *query* und
*lint*; die hier beschriebene Rollen- und Freigabeverteilung ist die Umsetzung
dieses Projekts.

Eine einfache Übersichtsdatei und Volltextsuche können für einen überschaubaren
Bestand genügen. Erst wenn Navigation und Trefferqualität messbar nachlassen,
lohnt sich zusätzliche Suchtechnik. Eine allgemeingültige Seitenzahl als Grenze
gibt es nicht; Dokumentlänge, Verlinkung und Modellkontext sind ebenso wichtig.

Es gibt bereits fertige Programme, die diese Idee umsetzen – etwa das frei
lizenzierte Community-Werkzeug `nashsu/llm_wiki` (GNU GPL v3.0), das Dokumente
automatisch vernetzt und unveränderte Dateien überspringt. Es ist eines von
mehreren und nicht „der Standard".

## Risiken und Grenzen

**Halluzinationen und Fehlerfortpflanzung.** Ein LLM erfindet gelegentlich
überzeugend klingende Angaben. Quellenangaben eines Modells sind nur etwas wert,
wenn sie geprüft wurden. Beim LLM-Wiki kommt eine besondere Gefahr hinzu, die als
**Error Drift** („Fehler-Abdrift") bezeichnet wird: Ein einmaliges Missverständnis
wandert in eine Wiki-Seite und breitet sich still weiter aus, während das Wiki
weiterhin sauber und geordnet aussieht. Bei klassischem RAG kann sich ein solcher
Fehler bei der nächsten Frage von selbst korrigieren, weil wieder am Original
begonnen wird – im LLM-Wiki bleibt er eingegraben. Gegenmittel sind eine strikte
Trennung von Entwurf und Freigabe sowie **Quellentreue**: Jede Seite verweist auf
ihre Rohquellen. Der verwandte Risikokomplex **Model Collapse** ist in
[Neue Artikel aus Rohfassungen erstellen](neue-artikel-erstellen.md) beschrieben.

**Skalierung und Kontextlimit.** Ab einer gewissen Größe – nach Erfahrungsberichten
einige hundert Seiten – kann der Agent nicht mehr alle Seiten gleichzeitig
überblicken. Er übersieht Seiten, erzeugt Dubletten und verpasst Querverweise.
Der übliche Behelf ist ein Master-Index mit einzeiligen Zusammenfassungen.

**Wartungsaufwand und Veralten.** Ohne regelmäßige Lint-Läufe veralten Aussagen
unbemerkt. Nach einem Erfahrungsbericht fallen alle paar Wochen einige Minuten
bis eine halbe Stunde für Widerspruchsprüfung, Vereinheitlichung der Begriffe und
Aufräumen an – weniger als reine Handarbeit, aber nicht wartungsfrei.

**Nachvollziehbarkeit.** Man arbeitet ein bis zwei Schritte von der Quelle
entfernt – mit der Interpretation des Modells statt mit dem Original. Die Frage
„woher kommt das?" wird dadurch schwerer zu beantworten.

**Kurz genannt:**

- **Datenschutz:** Vertrauliche und personenbezogene Daten gehören ohne Freigabe
  nicht an externe Modell-Anbieter (siehe [Datenschutz](datenschutz.md)).
- **Bias:** Trainingsdaten enthalten Verzerrungen.
- **Scheinsicherheit:** Ein sicherer, flüssiger Ton sagt nichts darüber aus, ob
  die Aussage stimmt.
- **Verantwortung:** Wer einen Text weitergibt, hat ihn geschrieben – „die KI
  war's" zählt nicht.

## Offene Fragen der Fachwelt

Seit Karpathys Veröffentlichung wird das Muster diskutiert. Einige Punkte sind
grundsätzlich:

- **„Nur eine umbenannte Cache-Schicht"?** In der Debatte wird eingewandt, das
  Muster benenne bekannte Cache-Probleme (Deduplizierung, Erkennen veralteter
  Einträge) nur neu.
- **Wo liegt die Quelle der Wahrheit?** Ungelöst ist, ob das LLM ausschließlich
  aus unveränderten Rohquellen „kompiliert" oder ob Menschen auch direkt im Wiki
  schreiben. Sobald beides passiert, gibt es kein sauberes Neu-Kompilieren mehr –
  genau dieser Mischfall trifft auf dieses Projekt zu (siehe unten).
- **Abdrift durch Personalisierung.** Ein noch nicht begutachteter Fachaufsatz
  vom April 2026 argumentiert, dass persönliche Wiki-Gedächtnisse je nach Nutzer
  unterschiedlich viel behalten und dadurch widersprechende Belege verdrängen
  können.
- **Technische Detailfragen:** Formate ohne Verlust von Tabellen und Links
  umwandeln, Texte sinnvoll zerteilen, exakte Suchtreffer für Fachbegriffe,
  Versionierung, satzgenaue Quellenangaben, Umgang mit widersprüchlichen Seiten,
  ob schreibende Agenten direkt speichern dürfen oder nur Vorschläge einreichen.

## Rechtlicher Rahmen (knapp)

Diese Seite ist keine Rechtsberatung. Vier Punkte sind aber wichtig:

- **Urheberrecht an KI-Texten.** Nach § 2 Abs. 2 des deutschen
  Urheberrechtsgesetzes (UrhG) sind Werke „nur persönliche geistige
  Schöpfungen". Dass hinter einer solchen Schöpfung ein Mensch stehen muss, ist
  herrschende Meinung, steht aber nicht wörtlich im Gesetz. Nach dieser
  Auffassung genießen rein KI-erzeugte Texte ohne schöpferische menschliche
  Prägung keinen Schutz; erst eine substantielle menschliche Bearbeitung
  begründet ein eigenes Urheberrecht, das bloße Formulieren eines Prompts genügt
  dafür nicht.
- **Text und Data Mining (§ 44b UrhG).** Das automatisierte Auswerten
  rechtmäßig zugänglicher Werke ist zulässig, sofern der Rechtsinhaber sich diese
  Nutzung nicht vorbehalten hat; bei online zugänglichen Werken wirkt ein solcher
  Vorbehalt nur, wenn er in maschinenlesbarer Form erfolgt. Ob das **Training**
  von KI-Modellen unter diese Schranke fällt und ob ein Vorbehalt in normaler
  Sprache „maschinenlesbar" ist, ist Gegenstand von Rechtsstreitigkeiten.
- **Freie Lizenz und Share-Alike.** Dieses Wiki steht unter der Lizenz
  CC BY-SA 4.0. „BY" verlangt die Namensnennung der Autoren, „SA" (*Share-Alike*)
  verlangt, dass abgeleitete Werke unter derselben Lizenz stehen. Ungeklärt ist,
  ob eine Zwei-Satz-Zusammenfassung durch ein LLM schon ein „abgeleitetes Werk"
  ist und wie man Dutzende Autoren einer Quelle korrekt nennt.
- **Kennzeichnungspflicht.** Der Transparenzhinweis am Anfang und Ende jeder
  Seite setzt Artikel 50 der EU-Verordnung über Künstliche Intelligenz
  (EU AI Act) um.

Mehr zum Aufbau dieses Projekts steht im
[Überblick](openwiki/overview.md).

## Wie dieses Wiki das Muster nutzt

Das Wiki wissen-ahrensburg.de ist selbst ein Co-Wiki nach diesem Muster: Die
Inhalte liegen als Markdown-Dateien, gebaut mit dem Programm mdBook, ohne
Datenbank; die Versionsgeschichte übernimmt das Werkzeug **Git**. Die drei
Schichten haben hier eine direkte Entsprechung:

| Karpathys Muster | In diesem Projekt |
|---|---|
| Rohquellen (read-only) | `raw/<thema>.md` – menschliche Rohfassungen, außerhalb des gebauten Buchs |
| Wiki / Ausgabe | `src/*.md` und das Inhaltsverzeichnis `src/SUMMARY.md` |
| Schema | `CLAUDE.md`, `AGENTS.md`, die Agenten-Profile im Ordner `.claude/` und der Ordner `openwiki/` |
| `index.md` | `src/SUMMARY.md` als Inhaltsverzeichnis; `openwiki/source-map.md` als technische Repository-Karte |
| Ingest / Query / Lint | die Redaktionspipeline aus sieben spezialisierten `redaktion-*`-Agenten (Forscher, Architekt, Schreiberling, Faktenchecker, Lektor, Verlinker, Aktualisierer); die ereignisgesteuerte Pflege übernimmt der Aktualisierer |

Diese Rollen und der Ablauf sind in [Co-Wiki: Mensch & KI](co-wiki.md) und in
[Neue Artikel aus Rohfassungen erstellen](neue-artikel-erstellen.md) beschrieben.

Zwei Abweichungen vom reinen Muster seien ehrlich benannt. Erstens nutzt dieses
Projekt **beides** – eine RAG-Recherche in der Entwurfsphase und das dauerhafte
Markdown-Wiki –, und Menschen schreiben direkt in `src/`, nicht nur der Agent
(der oben erwähnte Mischfall). Zweitens ist Karpathys Wiki als persönliches
Gedächtnis für eine Person gedacht, während dieses hier ein öffentliches,
redaktionell geprüftes Nachschlagewerk unter freier Lizenz ist; die Abdrift
durch Personalisierung wird durch Mehr-Augen-Prinzip und Belegpflicht gedämpft.

Dieses Projekt wird auch im Abschnitt „Sonderfall: LLM-Wiki / Co-Wiki" von
[Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)
eingeordnet; dort ist außerdem beschrieben, wie viele Seiten das Programm mdBook
verträgt – dieselbe Skalierungsfrage wie beim Kontextlimit des LLM-Wikis.

## Verwandte Seiten

- [Co-Wiki: Mensch & KI](co-wiki.md)
- [Neue Artikel aus Rohfassungen erstellen](neue-artikel-erstellen.md)
- [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md)
- [Wissenssysteme im Vergleich](wissenssysteme-im-vergleich.md)
- [Überblick](openwiki/overview.md)

## Quellen

- [Andrej Karpathy: „llm-wiki.md" (GitHub Gist, 4. April 2026)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [nashsu: „llm_wiki" (GitHub-Repository mit README)](https://github.com/nashsu/llm_wiki)
- [codecentric: „Wissensmanagement mit KI – Andrej Karpathys llm-wiki"](https://www.codecentric.de/wissens-hub/blog/wissensmanagement-mit-ki-andrej-karpathys-llm-wiki)
- [Stefan Miteski: „Memory as Metabolism: A Design for Companion Knowledge Systems" (arXiv:2604.12034, 13. April 2026)](https://arxiv.org/abs/2604.12034)
- [§ 44b UrhG – Text und Data Mining (dejure.org)](https://dejure.org/gesetze/UrhG/44b.html)
- [CMS Law: „Text und Data Mining nach dem neuen Urheberrecht"](https://cms.law/de/deu/legal-updates/Text-und-Data-Mining-nach-dem-neuen-Urheberrecht)
- [Universität Bremen: „Inhalte Dritter zum Training von KI"](https://www.uni-bremen.de/urheberrecht/leitfragen/11-inhalte-dritter-rechtssicher-mit-ki-verwenden/antwort-inhalte-dritter-zum-training-von-ki)

### Weiterführendes

- [Towards AI: „I built Karpathy's LLM Wiki twice"](https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a)

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
