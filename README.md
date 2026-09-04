# Dedizierte KI-Code-Wiki-Tools (direkt im Repository)

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

Dieses Dokument beschreibt die Werkzeugkategorie **„dedizierte KI-Code-Wiki-Tools“**, die eine
maschinell erzeugte Wissensbasis über eine Codebasis anlegen und diese **direkt im Repository**
ablegen – als versionierte Markdown-Dateien neben dem Quellcode. In diesem Repository wird
dieser Ansatz über **OpenWiki** genutzt (Ordner [`openwiki/`](openwiki/), Agent-Hinweise in
[`AGENTS.md`](AGENTS.md)).

## Inhalt

- [Worum geht es?](#worum-geht-es)
- [Das LLM-Wiki-Pattern (Karpathy-Muster)](#das-llm-wiki-pattern-karpathy-muster)
- [Google Open Knowledge Format (OKF)](#google-open-knowledge-format-okf)
- [Abgrenzung](#abgrenzung)
- [Vor- und Nachteile](#vor--und-nachteile)
- [Eigenständige Knowledge-Bases & Wikis mit KI](#eigenständige-knowledge-bases--wikis-mit-ki)
- [Kombination mit KI-Prompt-Bundlern](#kombination-mit-ki-prompt-bundlern)
- [Gehostete KI-Code-Wiki-Dienste](#gehostete-ki-code-wiki-dienste)
- [Vergleich der Ansätze](#vergleich-der-ansätze)
- [Nutzung in diesem Repository](#nutzung-in-diesem-repository)
- [Weiterführend](#weiterführend)

## Worum geht es?

Ein KI-Code-Wiki analysiert Quellcode, Konfiguration, Tests und vorhandene Dokumentation und
erzeugt daraus eine strukturierte, verlinkte Wissensbasis: Überblick, Architektur, Datenflüsse,
zentrale Module, oft mit automatisch generierten Diagrammen (meist Mermaid).

Bei der hier gemeinten Variante gilt:

- Die Ausgabe wird **in das Repository committet** (nicht nur auf einer externen Website gehostet).
- Die Aktualisierung läuft **automatisiert**, typischerweise über einen geplanten CI-Lauf
  (z. B. GitHub Actions), der die Seiten neu generiert und per Commit/PR einspielt.
- Die Seiten sind **generiert** und werden nicht von Hand gepflegt – Änderungen gehören in den
  Quellcode bzw. die Quelldokumentation, das Wiki wird danach neu erzeugt.

## Das LLM-Wiki-Pattern (Karpathy-Muster)

Der gemeinsame Kern dieser Werkzeuge geht auf ein von **Andrej Karpathy** beschriebenes Muster
zurück ([Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)): Statt bei
jeder Frage roh über die Quellen zu suchen (RAG), pflegt ein LLM-Agent **inkrementell ein
persistentes, quervernetztes Markdown-Wiki**. Man kuratiert die Quellen und stellt Fragen – der
Agent übernimmt die Buchführung: neue Quelle lesen, in typisierte Seiten einordnen, Verweise
setzen.

Kennzeichen des Musters:

- **Markdown-Dateien** als Format – für Menschen wie für LLMs gut lesbar, versionierbar.
- **Typisierte Seiten** mit Frontmatter (`type`, `title`, `description`, `tags`) und benannten
  Abschnitten.
- **Interlinks** zwischen den Seiten; das Wiki ist ein Graph, kein flacher Ordner.
- **Der Agent schreibt, der Mensch kuratiert** – die Pflege ist ein wiederholbarer Lauf, kein
  manuelles Redigieren.

In diesem Repository folgen `openwiki/*.md` sowie [`CLAUDE.md`](CLAUDE.md) und
[`AGENTS.md`](AGENTS.md) diesem Schema. Verwandt, aber nach außen gerichtet, ist
[`llms.txt`](https://llmstxt.org/) (Jeremy Howard): eine Datei, die externen LLMs die
Website/Repo-Struktur erklärt.

**Google Code Wiki** (<https://codewiki.google>) ist eine gehostete Umsetzung desselben
Gedankens: Ein Gemini-Agent erzeugt aus einem GitHub-Repository ein interaktives Wiki mit
Architektur-, Klassen- und Sequenzdiagrammen, Modul-Rundgängen und einem Chatbot über den Code,
und regeneriert es nach jedem Commit. Zugriff für öffentliche Repos über
`codewiki.google/github.com/owner/repo`.

## Google Open Knowledge Format (OKF)

Googles Open Knowledge Format (OKF) ist ein offener, herstellerneutraler Standard, den Google
Cloud im Juni 2026 eingeführt hat
([Spezifikation](https://github.com/GoogleCloudPlatform/open-knowledge-format)). Er strukturiert
Unternehmenswissen und -kontext in portable Verzeichnisse von Markdown-Dateien für KI-Agenten.

OKF formalisiert das oben beschriebene Muster:

- **Ein Verzeichnis von Markdown-Dateien** mit YAML-Frontmatter, für Menschen wie für Agenten
  lesbar.
- **Minimales Schema**: ein Pflichtfeld (`type`), optionale Metadaten (`title`, `description`,
  `resource`, `tags`, `timestamp`), darunter ein frei formulierter Markdown-Text.
- **Produzenten und Konsumenten sind entkoppelt**: Wer OKF schreibt (Mensch, Agent,
  Export-Pipeline) und wer es liest (Dateiserver, Wissens-Oberfläche, LLM-Kontext, Suchindex,
  Graph-Viewer), müssen sich nicht kennen – kein Aufwand für individuelle Integrationen.
- Ziel ist das „Context-Assembly-Problem“: verstreutes Wissen in **ein** Format bringen, das
  jeder Agent ohne Übersetzung konsumieren kann. v0.1 im Juni 2026, v0.2 im Juli 2026.

Die `openwiki/`-Seiten dieses Repositories nutzen bereits dasselbe Frontmatter-Schema
(`type` / `title` / `description` / `tags`) und sind damit OKF-nah.

## Abgrenzung

| Ansatz | Ablageort | Beispiele |
|---|---|---|
| **Dediziert, im Repository** (dieses Dokument) | Markdown im Repo, versioniert | OpenWiki, DeepWiki‑Open (self‑hosted), AIGNE DocSmith |
| Gehostet / extern | Externe Website, nicht im Repo | DeepWiki.com (Cognition), Google Code Wiki |
| In den Code eingebettet | Doku-Snippets neben dem Code, an Code-Zeilen gekoppelt | Swimm |
| Klassische Doku-Generatoren | Aus Docstrings/Kommentaren, kein KI-Verständnis | Doxygen, Sphinx, TypeDoc |

## Vor- und Nachteile

**Vorteile**

- Wiki ist **offline und versioniert** verfügbar, Diffs pro Änderung nachvollziehbar.
- Funktioniert bei **privaten Repositories**, ohne Code an einen Drittanbieter-Dienst zu geben
  (abhängig vom gewählten Modell-Backend).
- Nutzbar als **Just-in-time-Kontext für Agenten** (siehe `AGENTS.md`), ohne Netzabruf.
- Kein Vendor-Lock-in am Hosting: Die Dateien bleiben, auch wenn das Tool wechselt.

**Nachteile**

- **Repo-Rauschen**: generierte Dateien und regelmäßige Commits/PRs.
- **Veralten** zwischen zwei Generierungsläufen; Stand ist immer der des letzten Laufs.
- **Kosten/Token** für das verwendete Sprachmodell bei jedem Lauf.
- Gefahr, generierte Aussagen für autoritativ zu halten – **Quellcode und Tests bleiben maßgeblich**.

## Eigenständige Knowledge-Bases & Wikis mit KI

Neben den code-orientierten Werkzeugen oben steht eine breitere Kategorie: **allgemeine
Wissensdatenbanken und Wikis, die KI einsetzen** – für Inhaltserstellung, Zusammenfassung,
semantische Suche oder ein Frage-Antwort-Interface über den gesamten Bestand. Sie sind nicht an
eine Codebasis gebunden und dienen Redaktion, Team-Dokumentation oder persönlichem Wissen.

| Typ | Beispiele | KI-Rolle |
|---|---|---|
| KI-natives Team-Wiki | Notion (Q&A, Agents), Guru, Slite, Tettra | Antworten, Verifikation, Entwurf |
| Open-Source-Wiki / KB | MediaWiki, Outline, BookStack, Wiki.js, Docmost | KI über Erweiterungen/Plugins |
| Persönliche Wissensbasis | Obsidian, Logseq, Mem | lokale Notizen, Verlinkung, KI-Assistenz |
| KI-Orchestrierung über Quellen | Dust, Glean | Agenten lesen/suchen in vorhandenem Wissen |
| Statische, KI-gestützte KB | mdBook / Docusaurus / MkDocs + LLM-Autoren | Autoren-Workflow, Text KI-assistiert |

**Dieses Repository** gehört in die letzte Zeile: eine eigenständige, öffentlich publizierte
Wissensdatenbank (mdBook über Ahrensburg), deren Texte KI-assistiert entstehen und redaktionell
geprüft werden – mit Transparenzhinweis nach Art. 50 EU AI Act. Der `openwiki/`-Index ist davon
getrennt und beschreibt das Repository selbst, nicht die Stadt Ahrensburg.

Abgrenzung zu den Repo-Code-Wikis:

- **Zielgruppe**: Menschen/Redaktion statt Entwickler und Agenten.
- **Quelle der Wahrheit**: die kuratierten Inhalte selbst, nicht ein Quellcode-Stand.
- **Pflege**: laufende redaktionelle Arbeit, nicht ein Regenerierungslauf.

## Kombination mit KI-Prompt-Bundlern

KI-Prompt-Bundler wie [Repomix](https://github.com/yamadashy/repomix) oder
[Gitingest](https://github.com/cyclotruc/gitingest) fassen ein ganzes Repository in einer einzigen,
LLM-tauglichen Textdatei zusammen (XML, Markdown oder Plain Text). Zusammen mit einem
KI-Code-Wiki ergibt das einen praktikablen Ablauf:

1. **Bündeln** – Repomix/Gitingest erzeugen einen kompakten Repository-Snapshot als Kontext.
2. **Generieren** – ein CLI-Agent schreibt bzw. aktualisiert daraus die Wiki-Kapitel als Markdown.
3. **Versionieren** – die Markdown-Dateien werden im Git-Repository eingecheckt und mitentwickelt.
4. **Aktualisieren** – bei Änderungen am Code läuft der Zyklus (geplant oder pro PR) erneut.

So bleibt die Dokumentation als Markdown im Repository versioniert, während CLI-Agenten die
Kapitel automatisch generieren und aktuell halten. Der Bündler liefert den Kontext, das Wiki-Tool
die Struktur, Git die Historie.

## Gehostete KI-Code-Wiki-Dienste

Das Gegenmodell zum Ansatz „direkt im Repository“: Ein externer Dienst indiziert das Repository
und stellt das Wiki auf **seiner eigenen Plattform** bereit – nichts wird ins Repository
committet.

| Dienst | Zugang | Merkmale |
|---|---|---|
| [DeepWiki](https://deepwiki.com) (Cognition/Devin) | `github.com` → `deepwiki.com` in der URL ersetzen | Auto-Wiki für öffentliche Repos, Architektur­diagramme, Chat über den Code, MCP-Server für Cursor/Claude Code; private Repos über ein Devin-Konto |
| [Google Code Wiki](https://codewiki.google) | `codewiki.google/github.com/owner/repo` | Gemini-generiertes Wiki, Architektur-/Klassen-/Sequenzdiagramme, Codebase-Chat, Regenerierung nach jedem Commit; öffentliche Repos gratis, private per Gemini-CLI (Warteliste) |
| [GitBook](https://gitbook.com), [Mintlify](https://mintlify.com) | gehostete Doku-Plattform + Repo-Sync | KI-Suche und Q&A über gepflegte Doku, teils Auto-Entwürfe aus dem Code |

**Vorteile**

- **Kein Repo-Rauschen**, keine CI-Pipeline, keine Wartung der Generierung.
- Sofort nutzbar; für populäre Open-Source-Repos oft schon vorindiziert.
- Interaktives Q&A/Chat-Interface über die Codebasis ohne eigenes Setup.

**Nachteile**

- **Code verlässt die eigene Infrastruktur** – für private/vertrauliche Repos meist ein Ausschlusskriterium
  (bzw. nur mit kostenpflichtigem Konto und Vertrauensstellung).
- **Nicht versioniert im Repo**: kein Diff, kein Offline-Zugriff, keine Nutzung als lokaler Agenten-Kontext.
- **Abhängigkeit vom Anbieter**: Verfügbarkeit, Preismodell, Einstellung des Dienstes.
- Stand richtet sich nach dem Indizierungs-Rhythmus des Anbieters, nicht nach eigenen Läufen.

Für dieses Repository ist der In-Repo-Ansatz (OpenWiki) gewählt; ein gehosteter Dienst wie
DeepWiki funktioniert hier zusätzlich, weil das Repository öffentlich ist.

## Vergleich der Ansätze

| Ansatz | Im Repo versioniert | Aktualisierung | Code bleibt lokal | Q&A-/Chat-Interface | Zielgruppe | Beispiele |
|---|---|---|---|---|---|---|
| Dediziert, im Repository | ja | CI-Lauf / pro PR | ja | nur über einen Agenten | Entwickler & Agenten | OpenWiki, DeepWiki-Open (self-hosted), AIGNE DocSmith |
| Gehosteter Dienst | nein | Indizierungs-Rhythmus des Anbieters (Code Wiki: nach jedem Commit) | nein (bei öffentlichen Repos unkritisch) | ja | Entwickler | DeepWiki.com, Google Code Wiki |
| Prompt-Bundler + CLI-Agent | ja | Skript / CI | ja | nein | Entwickler & Agenten | Repomix / Gitingest + CLI-Agent |
| In den Code eingebettet | ja, an Code-Zeilen gekoppelt | manuell, CI prüft auf Drift | ja | nein | Entwickler beim Lesen des Codes | Swimm |
| Eigenständige KI-Wissensbasis | statisch: ja · SaaS: nein | laufende redaktionelle Arbeit | statisch: ja · SaaS: nein | SaaS: ja | Redaktion, Team, Leserschaft | mdBook/MkDocs + LLM-Autoren, Notion, MediaWiki, Outline |
| Klassischer Doku-Generator | ja | Build aus Docstrings/Kommentaren | ja | nein | Entwickler | Doxygen, Sphinx, TypeDoc |

Dieses Repository nutzt Zeile 1 (OpenWiki für `openwiki/`) und ist zugleich selbst ein Fall von
Zeile 5 (die mdBook-Wissensdatenbank über Ahrensburg, KI-assistiert verfasst).

## Nutzung in diesem Repository

- Der generierte Index liegt unter [`openwiki/`](openwiki/):
    - [`openwiki/overview.md`](openwiki/overview.md) – Projektüberblick
    - [`openwiki/architecture.md`](openwiki/architecture.md) – Build- und Content-Architektur
    - [`openwiki/source-map.md`](openwiki/source-map.md) – Verzeichnis der Quelldateien
    - [`openwiki/INSTRUCTIONS.md`](openwiki/INSTRUCTIONS.md) – Kurzbeschreibung des Wikis
- [`AGENTS.md`](AGENTS.md) beschreibt, wie Agenten das Wiki behandeln sollen: optionaler
  Kontext, keine Startpflichtlektüre, generierte Seiten **nicht** von Hand editieren.
- Ein geplanter OpenWiki-GitHub-Actions-Workflow aktualisiert die Seiten. Inhaltliche
  Korrekturen erfolgen im Quellcode bzw. in den Quelltexten unter `src/`, danach regeneriert
  OpenWiki.
- `src/openwiki/{overview,architecture,source-map}.md` sind **manuelle Kopien** dieser Seiten,
  damit sie in `src/SUMMARY.md` verlinkt und mit ins mdBook gebaut werden können (mdBook baut nur
  Dateien unter `src/`). Sie tragen den Transparenzhinweis und einen Kopie-Vermerk. Der
  OpenWiki-Workflow aktualisiert `openwiki/`, **nicht** diese Kopien – bei Änderungen an den
  Originalen von Hand nachziehen. Verifikations-Screenshots liegen unter
  [`docs/verification/`](docs/verification/).

## Weiterführend

- LLM Wiki (Karpathy) – das ursprüngliche Muster als Gist:
  <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Google Code Wiki – gehostete Gemini-Umsetzung: <https://codewiki.google>
- Open Knowledge Format (OKF) – herstellerneutraler Markdown-Standard von Google Cloud:
  <https://github.com/GoogleCloudPlatform/open-knowledge-format>
- llms.txt (Jeremy Howard) – nach außen gerichtetes Gegenstück: <https://llmstxt.org/>
- DeepWiki-Open – Open-Source-Wiki-Generator für Git-Repositories:
  <https://github.com/AsyncFuncAI/deepwiki-open>
- DeepWiki (gehosteter Dienst, Cognition/Devin): <https://deepwiki.com>
- GitBook – gehostete Doku-Plattform mit KI-Suche und Repo-Sync: <https://gitbook.com>
- Mintlify – gehostete Doku-Plattform mit KI-Q&A und Auto-Entwürfen aus dem Code: <https://mintlify.com>
- Swimm – an Code-Zeilen gekoppelte Doku: <https://swimm.io>
- Repomix – Repository in eine KI-taugliche Datei bündeln: <https://github.com/yamadashy/repomix>
- Gitingest – Repository als Prompt-Text extrahieren: <https://github.com/cyclotruc/gitingest>
