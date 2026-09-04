---
type: Reference
title: Agent-Notizen
description: Betriebswissen für coding agents in diesem Repo — Deploy & Verifikation, die OpenWiki-src-Kopien, die handgepflegten Co-Wiki-Kopien und der .agents/-Mirror. Spiegelt den Memory-Store der Claude-Code-Sessions.
tags:
  - agents
  - operations
  - deploy
  - openwiki
  - co-wiki
audience: coding agents
---

# Agent-Notizen

Betriebswissen, das ein Agent für die Arbeit an diesem Repo braucht und das sich nicht direkt
aus Code oder Git-Historie ergibt. Diese Seite spiegelt die Memory-Notizen der
Claude-Code-Sessions, damit sie auch versioniert im Repo stehen. `docs/` liegt außerhalb von
`src/` und ist nicht Teil des mdBook.

## 1. Deploy & Verifikation

Vollständiges Runbook: [`deploy-verification.md`](deploy-verification.md). Kern:

- **Deploy-Sequenz:** `npm install` (das `gh-pages`-Binary ist eine gitignorierte devDependency)
  → `mdbook build` → `npm run ver`.
- **Toolchain in der Claude-Code-Umgebung.** `mdbook` + `mdbook-mermaid` sind seit dem ersten
  Nachinstallieren am 2026-09-03 **persistent vorhanden** (`~/.cargo/bin/`, `mdbook v0.4.52`);
  die Umgebung übersteht Sessions. Erst `which mdbook mdbook-mermaid` prüfen; nur falls weg,
  neu: `cargo install mdbook --version '^0.4'` und `cargo install mdbook-mermaid --version
  0.14.0` (je ~1 Min Compile; `0.14.0` exakt pinnen, siehe [`../CLAUDE.md`](../CLAUDE.md)).
  `cargo` liegt unter `~/.cargo/bin/cargo`. In jeder frischen Shell `export
  PATH="$HOME/.cargo/bin:$PATH"` voranstellen, sonst finden `mdbook build` und `npm run ver`
  das Binary nicht. `node`/`npm` und `google-chrome` (Headless, für die Render-Screenshots aus
  [`verification/README.md`](verification/README.md); gehen auch direkt gegen
  `file://$PWD/book/<seite>.html`, `mdbook serve` unnötig) sind vorhanden. Der komplette Deploy
  inkl. CNAME-only-Diff-Check und Live-Check läuft damit aus der Umgebung durch (erstmals
  verifiziert 2026-09-03, `gh-pages` `d5b22c3`; zuletzt `52107f5`).
- **„Published" heißt nicht „geändert".** `npm run ver` gibt immer `Published` aus. Das
  `gh-pages`-Tool legt nur dann einen neuen `gh-pages`-Commit an, wenn sich `book/`
  tatsächlich unterscheidet. Commits, die nur Meta-Docs (`CLAUDE.md`, `AGENTS.md`,
  `README.md`, `docs/**`, `.claude/**`, `raw/**`) oder die generierten `openwiki/`-Originale
  betreffen, ändern `book/` nicht → `gh-pages` und der `last-modified`-Header bleiben stehen.
  Erwartetes Verhalten.
  `last-modified` wandert erst bei einer Änderung unter `src/`.
- **CNAME-only-Diff-Check** (deployte Seite == frischer Build von `main`?):
  ```
  git fetch origin -q && rm -rf book && mdbook build
  tmp=$(mktemp -d); git archive origin/gh-pages | tar -x -C "$tmp"
  diff -rq book "$tmp" | grep -vE '\.git|/CNAME|\.nojekyll'
  rm -rf "$tmp"
  ```
  Ausgabe nur `Nur in <tmp>: CNAME.` → **PASS**. Jede andere Datei → **STALE**, neu deployen.
  Erwartete Nicht-Inhalts-Unterschiede: `CNAME` (nur im Deploy-Baum, via `--cname`),
  `.gitignore` (vom `gh-pages`-Tool), `.nojekyll` (unterschiedliche Bytes, bedeutungslos).
- **`gh-pages` kann `main` voraus sein.** `npm run ver` deployt den lokalen `book/`-Build,
  nicht `origin/main`. Wird aus einem dirty Working Tree deployt, enthält die Live-Site
  Inhalte, die nie committet wurden. Vor einem „sauberen" Deploy von `main` also **immer**
  den CNAME-only-Diff-Check laufen — sonst nimmt der Deploy live stehende Seiten wieder
  herunter. Trat am 2026-09-01 auf (siehe unten).

### Stand 2026-09-02 (Reconciliation + Deploy)

Am 2026-09-01 wurde die Site aus einem dirty Tree deployt: `gh-pages` enthielt 10 Seiten,
deren `src/*.md` nur als untracked Dateien lokal existierten. Am 2026-09-02 zusammengeführt und
neu deployt:

- **Letzter `src/`-Stand `f7f0d9d`** deployt als **`gh-pages` `5d137b2`** (Pages-Build `built`),
  <https://wissen-ahrensburg.de> verifiziert (alle 10 neuen Seiten HTTP 200, Inhaltsstichproben ok).
- Commit-Kette: `25b8e6f` (CLAUDE.md/AGENTS.md → Kurzfassung) → `c0c5d7a` (`.agents/`-Mirror +
  gitignore) → `15016c8` (agent-notes §6) → `c465fbd` (Beschreibungen straffen, Dubletten-Skill
  `wiki-ki-agenten` gelöscht) → `7b5d2e0` (README.md + Related-pages straffen) → `9702653`
  (10 neue Inhaltsseiten + Querverlinkung + Stadterhebung 1948→1949) → `f7f0d9d` (OpenWiki-Index
  auf 43 Seiten, `src/openwiki/`-Kopien nachgezogen) → `5320070` (dieser Abschnitt) → `b1a8d1f`
  (Co-Wiki-Render-Screenshot neu aufgenommen) → `d2784d6` (Commit-Kette hier bis `b1a8d1f`
  fortgeschrieben) → `9e67202` (CLAUDE.md 112→77 Z. + §3 straffen, Per-Session-Token senken) →
  `3c4b950` (`redaktion-*` `description:`-Felder ~28% kürzen).
- Alles ab `f7f0d9d` betrifft nur `docs/` bzw. `.claude/` → kein `src/`-Delta → `gh-pages` bleibt
  korrekt bei `5d137b2` (genau die Regel eine Ebene höher). `main` HEAD = `3c4b950`, gepusht.
- Site jetzt **43 Inhaltsseiten** (vorher 37).

### Stand 2026-09-03 (Vergleichsseiten-Familie + Deploys)

Mehrere Redaktionspipeline-Läufe (§3–§4) haben die „Software für ein großes Wissensprojekt"-
Familie ausgebaut, jeweils Commit → `mdbook build` → `npm run ver` → `main` push → Live-Check:

- `d5079b8` `src/wissenssysteme-im-vergleich.md`, `ca88ca0`+`bbc3624` `src/cms-millionen-artikel.md`
  (frühere Session).
- `3a4128f` `src/webframeworks-im-vergleich.md` (aus `raw/Webframework.md`) → deployt als
  `gh-pages` `c063a98`.
- `9fdeaf9` `src/wissenssystem-selbst-bauen.md` (aus `raw/webframeworks-im-vergleich.md`, der
  größeren der zwei ähnlich benannten Rohfassungen; Tiefgang-Seite unter
  `webframeworks-im-vergleich.md`) → `gh-pages` `71097d1`.
- `b4a2e0d` `src/SUMMARY.md`: die ganze „…im Vergleich"-Familie (Wissenssysteme · Wiki-Programme ·
  CMS · CMS-Millionen · Doku-Generatoren · Webframeworks · Ein Wissenssystem selbst bauen) aus der
  Verschachtelung unter „Software für ein großes Wissensprojekt" in den **oberen Prefix-Block**
  gezogen, flach nach „LLM Wiki", in Lesereihenfolge. Unter „# Wie dieses Wiki entsteht" bleiben
  nur `co-wiki.md` + `software-fuer-ein-grosses-wissensprojekt.md`. Keine Datei verschoben, keine
  `.md`-Links geändert. → `gh-pages` `7966e60`. **Neue Vergleichs-/Architektur-Seiten gehören ab
  jetzt in diesen Prefix-Block.**
- `8e8b05e` Co-Wiki-Render-Screenshot neu aufgenommen (nur `docs/` → kein `book/`-Delta →
  `gh-pages` bleibt `7966e60`).

`main` HEAD = `8e8b05e`, gepusht. CNAME-only-Diff-Check PASS (Live-Site == `main`,
`co-wiki.html` byte-identisch zum frischen Build). `SUMMARY.md` jetzt **64 Seiten**
(61 `src/*.md` + 3 `src/openwiki/`-Kopien).

- `f3b3877` `src/wissen-speichern.md` (aus `raw/wissenspeichern.md`, Redaktionspipeline;
  Einsteiger-Konzeptseite: Ablageformen Text/SQL/Vektor, Suchstrategien, Export ohne Nutzerdaten,
  Chunk-Länge). `SUMMARY.md`: oberer Prefix-Block **direkt nach `[LLM Wiki]`**, vor der
  „…im Vergleich"-Familie — die Seite ist deren konzeptionelle Grundlage. Rückverweise in
  `software-fuer-ein-grosses-wissensprojekt.md`, `wissenssystem-selbst-bauen.md`,
  `wissenssysteme-im-vergleich.md`. Rohfassung danach gelöscht (gitignoriert). → deployt als
  `gh-pages` `d5b22c3`, Pages-Build `built`, <https://wissen-ahrensburg.de/wissen-speichern.html>
  HTTP 200 verifiziert. CNAME-only-Diff-Check vor dem Deploy: nur `wissen-speichern.html` (neu) +
  die drei Rückverweis-Seiten + `llm-wiki.html` (nur „next chapter"-Link) + Aggregate
  (`toc.*`, `print.html`, `searchindex.js`) — erwartet.
- `908dff4` `docs/agent-notes.md` §1 (dieser Deploy-Eintrag).
- `3e542ff` Co-Wiki-Render-Screenshot neu aufgenommen (`verification/co-wiki-page-full.png` +
  README-Log): Seitenleiste zeigt „Wissen speichern" als 4. Eintrag nach „LLM Wiki", Co-Wiki-Seite
  selbst unverändert. Methode: `mdbook serve` (lokal) + Headless Chrome — beides in der
  Claude-Code-Umgebung verfügbar (§1, Toolchain-Absatz).
- `f734f51` / `65fb8d4` / `7d9deba` `docs/agent-notes.md` §1/§3 (Toolchain-Absatz, Deploy-Kette,
  Render-Zeiger, Post-Deploy-Nachkontrolle) — alle nur `docs/`, `gh-pages` blieb `d5b22c3`.
- `fe65f7c` `src/neue-artikel-erstellen.md` ↔ `src/wissen-speichern.md` gegenseitig verlinkt
  (je ein Eintrag in „Verwandte Seiten"). → deployt als `gh-pages` `78a35a3`, Pages-Build `built`,
  Live-Cross-Links + HTTP 200 verifiziert. Pre-/Post-Deploy-Diff: nur die zwei Seiten +
  `print.html`/`searchindex.js` — erwartet.
- `593eb66` `docs/agent-notes.md` §1 (dieser Deploy-Eintrag) — nur `docs/`.
- `main` HEAD = `593eb66`, gepusht. **Voller CNAME-only-Diff-Check am 2026-09-03 (nach `fe65f7c`):
  PASS.** `diff -rq` über den kompletten Baum — alle Inhaltsdateien byte-identisch, einziger
  gefilterter Rest `CNAME`. Ungefilterte Nicht-Inhalts-Unterschiede wie dokumentiert: `CNAME`
  (nur Deploy-Baum), `.gitignore` (vom `gh-pages`-Tool), `.nojekyll` (andere Bytes, bedeutungslos).
  Dateizahl frischer Build **110**, `gh-pages` **112** (= 110 + `CNAME` + `.gitignore`).
  `gh-pages` `78a35a3`, Pages-Build `built`. `SUMMARY.md` **65 Seiten**.

### Stand 2026-09-03 (Urheberrechts-Review → Quellenattribution + Deploys)

Durchgang durch alle `src/`-Inhalte auf Urheberrechtsprobleme. Ergebnis: **keine wörtliche
Übernahme** gefunden. Zwei Punkte nachgezogen, jeweils Commit → `mdbook build` → `npm run ver`
→ `main` push → Live-Check (fortlaufend von `gh-pages` `78a35a3`):

- `204afa5` `src/*.md` (8 Seiten): neuer Abschnitt **„## Wikipedia als Quelle"** (vor dem unteren
  Transparenzhinweis) mit CC-BY-SA-4.0-Hinweis, Autoren-Nachweis („laut Versionsgeschichte") und
  den konkreten Ursprungsartikeln — auf `schloss-ahrensburg`, `ahrensburger-tunneltal`,
  `familie-rantzau`, `familie-schimmelmann`, `ortsname-ahrensburg`, `ahrensburg-ns-zeit`,
  `demografie`, `persoenlichkeiten` (die Seiten, die substanziell aus der de-Wikipedia
  synthetisiert sind). → `gh-pages` `b66dbaa`, alle 8 Seiten live HTTP 200, Attribution sichtbar.
  **Regel ab jetzt:** Seite, die wesentlich auf einem Wikipedia-Artikel beruht → diesen Abschnitt
  anhängen (Anker `#wikipedia-als-quelle`).
- `05948e6` `src/ahrensburger-tunneltal.md`: **Alfred-Rust-Abschnitt** (Biografie + Grabungen) war
  eng an den Stormarn-Lexikon-Artikel angelehnt. **Das Stormarn-Lexikon (`stormarnlexikon.de`)
  steht unter „© alle Rechte vorbehalten"** — keine freie Lizenz; die kursierende CC-BY-NC-SA
  gilt nur für die Kreisarchiv-*Mediendatenbank*, nicht die Lexikon-Texte. Abschnitt neu
  formuliert auf Basis der frei lizenzierten Artikel *Alfred Rust (Prähistoriker)* /
  *Ahrensburger Kultur*; Weblinks getrennt in „amtlich / frei lizenziert" und „weiterführend
  (© geschützt)", die zwei SL-Links als `© Kreisarchiv Stormarn` gekennzeichnet.
  → `gh-pages` `58842c8`, live verifiziert.
- `92971d6` `src/ahrensburger-tunneltal.md`: Abschnitt **„Verbleib der Funde"** ebenso vom SL
  gelöst — neu auf Basis von *Meadows u. a. 2018, „Dating the lost arrow shafts from Stellmoor"*
  (Universität Aarhus, frei zugänglich), Museumsangaben umformuliert, Beleg in die Weblinks.
  → `gh-pages` `5fdaee8`, `ahrensburger-tunneltal.html` live verifiziert.
- `520b8cf` / `cb3a968` `docs/agent-notes.md` §1 (dieser Eintrag + Hash-Nachtrag) — nur `docs/`,
  `gh-pages` bleibt `5fdaee8`.
- `e59d0de` `src/{geografie,schloss-ahrensburg,stadtwappen,hauptseite}.md`: die übrigen sechs
  Stormarn-Lexikon-Verweise einheitlich mit **„© Kreisarchiv Stormarn, alle Rechte vorbehalten"**
  gekennzeichnet (wie `ahrensburger-tunneltal`), Schreibweise → „Stormarn-Lexikon". → `gh-pages`
  `ec7517e`, alle 5 Seiten live verifiziert. **Regel ab jetzt:** jeder Verweis auf
  `stormarnlexikon.de` (Weblink oder Quelle) trägt diesen Zusatz.
- `afc926d` `docs/agent-notes.md` §1 (`e59d0de`-Eintrag) — nur `docs/`.
- `e7cd2b7` **Prüfung der übrigen Seiten auf enge Wikipedia-Anlehnung** (WP-Artikel „Ahrensburg"
  u. a.). Ein echter Anlehnungsfall: `src/verkehrsanbindung.md` war eine enge Verdichtung von
  WP §Verkehr → neu formuliert (u. a. „fünf Stadtbus-/sechs Regionallinien" aufgelöst),
  Faktenfix **RE 8 → RE 80**, `## Wikipedia als Quelle` ergänzt. Block ebenfalls ergänzt auf
  `stadtwappen`, `stadtwerdung-1949`, `geschichte-der-stadt-ahrensburg`,
  `buergermeister-und-stadtvertretung` (Faktenüberschneidung mit WP „Ahrensburg";
  Blasonierungen bleiben amtliche Werke). `kirchen-und-religioese-gemeinschaften.md`: generische
  Konfessions-Definitionen (mögliche WP-Themenartikel-Echos) entfernt, auf die Ahrensburger
  Gemeinden fokussiert. Alle übrigen Seiten (`schlosskirche-ahrensburg`, `die-stadtteile-im-portraet`,
  `wichtige-unternehmen-arbeitgeber`, `familie-bildung`, NSG-/Geografie-Seiten): nur
  Tatsachenüberschneidung, eigenständige Formulierung — **kein** Attributionsbedarf.
  → `gh-pages` `88089c2`, alle 6 Seiten live HTTP 200, CNAME-only-Diff-Check **PASS** (110/112).
  Faktencheck nebenbei: Sitzverteilung 2023 (Grüne 9 / CDU 9 / SPD 6 / WAB 4 / FDP 3) ist
  **korrekt**, der WP-Wert war falsch.
- `main` HEAD = `e7cd2b7`, gepusht.

**Voller CNAME-only-Diff-Check nach `92971d6`, `e59d0de` und `e7cd2b7`: je PASS** — `diff -rq`
gefiltert nur `Nur in <tmp>: CNAME.`; frischer Build **110** Dateien, `gh-pages` **112** (+ `CNAME`
+ `.gitignore`). `SUMMARY.md` unverändert **65 Seiten** (keine `src/`-Datei angelegt/gelöscht).
Merke: **Stormarn-Lexikon nur als „weiterführend" verlinken, nie Text daraus übernehmen,
umschreiben oder übersetzen** — die Nutzungsbedingungen verbieten das ausdrücklich. Der Block
**„## Wikipedia als Quelle"** (Anker `#wikipedia-als-quelle`) sitzt vor dem unteren
Transparenzhinweis und steht jetzt auf 13 `src/`-Seiten.

### Stand 2026-09-03 (neue Seite „Urheberrecht und Duplicate Content" + Deploy)

Aus der menschlichen Rohfassung `raw/Ueberricht.md` über die volle Redaktionspipeline
(`redaktion-forscher` → `-architekt` → `-schreiber` → `-faktenchecker` ∥ `-lektor` → `-verlinker`,
Supervisor = Haupt-Thread) eine neue öffentliche Methodik-Seite gebaut:

- `d74f132` **`src/urheberrecht-und-duplicate-content.md`** (neu) + `SUMMARY.md`-Eintrag im **oberen
  Prefix-Block** nach „Wissen speichern" + Rückverweise in `src/{co-wiki,impressum,neue-artikel-erstellen}.md`.
  Inhalt: Ausdrucksform vs. Fakten (§ 2 II UrhG), manueller Urheberrechts-Review im Co-Wiki-Prozess
  (ausdrücklich **kein** automatischer Scanner — automatisierte Ähnlichkeitsprüfung nur als Ausblick),
  Wikipedia-Attribution (CC BY-SA 4.0, `Wikipedia:Weiternutzung`), Stormarn-Lexikon / amtliche Werke
  (§ 5 UrhG), Zitatrecht (§ 51 UrhG), Duplicate Content (Google-Kanonisierung, **kein** Penalty),
  Rechtsberatungs-Disclaimer (Stand 2026-09-03). Faktencheck: Gesetzeszitate §§ 2/5/23/51 wörtlich
  bzw. kernbegriffsgleich, § 24 a. F. Aufhebung 07.06.2021 bestätigt.
- Deploy: dieser Commit **plus** das noch nicht deployte `efd466f` (`gottesbuden.md` /
  `musik-und-theater.md` Textüberarbeitungen) → `npm run ver` → **`gh-pages` `52107f5`**.
  <https://wissen-ahrensburg.de/urheberrecht-und-duplicate-content.html> HTTP 200, Inhalts- und
  Nav-Stichproben ok; `gottesbuden.html` mit neuem `#weblinks` live.
- **CNAME-only-Diff-Check nach dem Deploy: PASS** — frischer Build **111** Dateien, `gh-pages`
  **113** (+ `CNAME` + `.gitignore`). `SUMMARY.md` jetzt **66 Seiten** (eine `src/`-Datei neu).
- `raw/Ueberricht.md` nach Fertigstellung gelöscht (gitignoriert, endgültig) — der verwertbare
  Inhalt steht vollständig in der neuen `src/`-Seite; Vermerk in [`../raw/README.md`](../raw/README.md)
  („Abgeschlossene Rohfassungen").
- `docs/`-Commits danach, `gh-pages` blieb `52107f5`: `15d8ce9` (dieser Eintrag),
  `3dd5219` (`verification/co-wiki-page-full.png` neu — Abschnitt „Verwandte Seiten" +
  Seitenleisten-Eintrag), `0849c0f` (Toolchain-Absatz §1: mdbook/mdbook-mermaid jetzt persistent),
  `487dc5f` (`raw/README.md` §„Abgeschlossene Rohfassungen"), `00537d1` (Log-Zeile).
- **`0121669`** `src/urheberrecht-und-duplicate-content.md`: Abschnitt **„Prüf-Prompts zum
  Selbernutzen"** ergänzt (aus `raw/Ueberricht.md`, Wunsch „Prompt Vorschläge") — fünf konkrete
  Prüf-Prompts nach „Wie dieses Wiki Urheberrechte prüft". → `npm run ver` → `gh-pages`
  `45d4143`, Live HTTP 200, Post-Deploy-CNAME-only-Diff-Check **PASS** (Build 111 / `gh-pages` 113).
- **`97ec4e0`** ebd.: Prompt **„Gesamtdurchgang (der Ausgangspunkt)"** vorangestellt — der
  ursprüngliche Ausgangs-Prompt der Rohfassung („Überprüfe alle Inhalt Urheberrecht verletzt"),
  in korrektem Deutsch, als umfassender erster Prüfschritt; die übrigen fünf arbeiten Treffer
  einzeln ab. → **`gh-pages` `80161f9`**, Live HTTP 200, CNAME-only-Diff-Check **PASS**.
  `SUMMARY.md` unverändert 66 Seiten.
- `main` HEAD = `97ec4e0` (+ dieser Nachtrag), gepusht.

## 2. OpenWiki-src-Kopien

`openwiki/*.md` erzeugt der OpenWiki-GitHub-Actions-Workflow. mdBook baut nur Dateien unter
`src/`, deshalb existieren `src/openwiki/*.md` als **manuelle Kopien**, die in `SUMMARY.md`
gelistet sind. Der Workflow aktualisiert `openwiki/`, nicht die Kopien — bei Änderungen von
Hand nachziehen.

**Kopier-Transformation pro Datei:**

- YAML-Frontmatter entfernen; ersetzen durch die kursive Transparenzhinweis-Zeile, danach ein
  Blockquote, das auf die manuelle Kopie von `openwiki/<datei>` hinweist (kann veraltet sein).
- Bei `overview.md` hat das Blockquote eine Extra-Zeile:
  „Sie beschreibt das Repository, nicht die Stadt Ahrensburg."
- Die Transparenzhinweis-Zeile am Ende noch einmal anhängen (Inhaltsseiten tragen sie oben
  und unten).
- Der Body dazwischen wird wörtlich übernommen.

**Drift-Check:** `diff src/openwiki/<f> openwiki/<f>` — erwartet sind **nur** der
Frontmatter↔Hinweis-Tausch oben und der Hinweis am Ende. Jeder Unterschied im Body heißt: Kopie
veraltet, neu synchronisieren. Stand 2026-08-31 waren alle drei (`architecture.md`,
`overview.md`, `source-map.md`) synchron. Hinweis: `architecture.md` enthält die
Transparenzhinweis-Zeichenkette in einem Codeblock als Beispiel — das ist echter Body-Inhalt in
beiden Dateien, kein Drift.

## 3. Handgepflegte Co-Wiki-Kopien

Der Co-Wiki-Text (Rollen Mensch/KI/Wiki, die vier Arbeitsmodelle, der typische Ablauf, die
technischen Bausteine und die zwei fortgeschrittenen Muster) liegt an **fünf Stellen**, alle
nicht aus einer Quelle generiert. Ändert sich die Formulierung, alle betroffenen nachziehen:

| # | Stelle | Umfang & Zweck |
|---|--------|----------------|
| 1 | `CLAUDE.md` → Abschnitt „Zusammenarbeit Mensch & KI (Co-Wiki)" | Knappe Kurzfassung für Claude Code (2026-09-02 auf ~4 Zeilen gekürzt: Rollen in einem Satz, Ablauf in einer Zeile), verweist auf die `co-wiki`-Skill und für die Redaktionsmuster auf §3–§4 dieser Datei. Volltext hier **nicht** — der liegt in der Skill. |
| 2 | `AGENTS.md` → Abschnitt „Die drei Betriebsmuster" (H3: Co-Wiki / Multi-Agenten-Redaktionspipeline / Event-Driven Documentation) | Ebenfalls seit 2026-09-02 auf eine Kurzfassung gekürzt, jede H3 wenige Sätze + Zeiger auf die passende `references/*.md`. Die alte kindgerechte Langprosa ist entfernt. |
| 3 | `.claude/skills/co-wiki/` (`SKILL.md` + `references/rollen.md` + `references/arbeitsmodelle.md` + `references/ablauf-und-technik.md` + `references/multi-agent-pipeline.md` + `references/event-driven-docs.md`) | operative Anleitung für Agenten; greift bei Arbeit an `src/`-Seiten, Rollenfragen, „Was ist ein Co-Wiki". Volle Detailfassung inkl. Arbeitsmodelle und der zwei fortgeschrittenen Muster. |
| 4 | `.claude/agents/` (`README.md` + `redaktion-forscher` / `-architekt` / `-schreiber` / `-lektor` / `-faktenchecker` / `-verlinker` / `-aktualisierer`) | die Subagenten der Redaktionspipeline; Rollenzuschnitt und Modellwahl (`haiku` für einfache Jobs, `sonnet` für Recherche/Schreiben/Faktencheck). Der Supervisor ist der Haupt-Thread, kein Subagent. |
| 5 | `src/co-wiki.md` (in `SUMMARY.md` unter „Wie dieses Wiki entsteht") | öffentliche Seite, <https://wissen-ahrensburg.de/co-wiki.html>. Rollen + Arbeitsmodelle + typischer Ablauf + technische Bausteine + die zwei fortgeschrittenen Muster (besucherfreundlich formuliert: „Das Roboter-Team", „Das Buch, das sich selbst aktualisiert"). |

Die öffentliche Seite ist Prosa für Besucher; Skill-Referenzen und Subagenten sind operative
Anleitung für Agenten; die Meta-Docs (`CLAUDE.md`, `AGENTS.md`) sind nur noch eine knappe
Kurzfassung mit Verweis auf die Skill — der Volltext lebt in `.claude/skills/co-wiki/`. Render-Verifikation der öffentlichen
Seite: `verification/co-wiki-page-full.png` (Stand **2026-09-03**, deckt alle acht Inhalts-Abschnitte
ab) — neu aufnehmen bei Abschnittsänderungen **oder wenn sich die `SUMMARY.md`-Seitenleiste ändert**
(zuletzt: `3e542ff` — Seitenleisten-Eintrag „Wissen speichern" nach „LLM Wiki", §1). Methode + Log:
`verification/README.md`.

## 4. Redaktions-Subagenten

Die Multi-Agenten-Redaktionspipeline ist als sieben `redaktion-*` Subagenten unter
[`../.claude/agents/`](../.claude/agents/) angelegt (Übersicht: `.claude/agents/README.md`):

| Agent | Rolle | Modell |
|-------|-------|--------|
| `redaktion-forscher` | Fakten sammeln, Info-Mappe anlegen | sonnet |
| `redaktion-architekt` | Überschriften-Bauplan | haiku |
| `redaktion-schreiber` | Fließtext schreiben, Korrekturen einarbeiten | sonnet |
| `redaktion-lektor` | Stil, Aufbau, Dopplungen (kein Faktencheck) | haiku |
| `redaktion-faktenchecker` | jede Aussage gegen die Info-Mappe | sonnet |
| `redaktion-verlinker` | Querverweise, Tags | haiku |
| `redaktion-aktualisierer` | Delta-Updates bei Neuerungen (Event-Driven) | sonnet |

Merksätze:

- **Der Supervisor ist der Haupt-Thread** (bzw. der Mensch), kein Subagent — nur der
  Haupt-Thread kann Subagenten starten.
- **Shared State** = eine Arbeitsdatei im Scratchpad (Info-Mappe, Bauplan, Review-Notizen),
  nicht Kontext-Weitergabe.
- **`forscher` / `architekt` / `faktenchecker` / `lektor` sind faktisch nur-lesend** (kein
  `Write`/`Edit` in dieser Umgebung) — sie liefern ihr Ergebnis als Text zurück, der Supervisor
  legt es in die Scratchpad-Datei. Nur `schreiber` (schreibt die `src/`-Seite + `SUMMARY.md`-
  Eintrag) und `verlinker` (Links, Rückverweise) fassen Dateien an.
- Neue Vergleichs-/Architektur-Seiten: Eintrag in den **oberen Prefix-Block** von `SUMMARY.md`
  (siehe §1, Stand 2026-09-03), nicht mehr verschachtelt unter „Software für ein großes
  Wissensprojekt". Tiefgang-Seiten stehen direkt hinter ihrer Elternseite.
- **Kritikschleife max. 2–3 Runden**, dann an den Menschen eskalieren.
- Kein Subagent veröffentlicht oder deployt — das entscheidet ein Mensch.

## 5. Roh-Ordner `raw/`

`raw/<thema>.md` ist die Ablage, in der **Menschen** Artikel und Notizen roh vorschreiben
(Vorlage `raw/_vorlage.md`). Vollständige Beschreibung: [`../raw/README.md`](../raw/README.md).

Für Agenten:

- `raw/` liegt außerhalb von `src/`, steht nicht in `SUMMARY.md`, wird nicht gebaut — nichts
  davon erreicht die Website. Kein Transparenzhinweis, solange es Rohfassung ist.
- Eine Datei in `raw/` ist ein **Auftrag zum Ausarbeiten**: Gliederung → Fließtext →
  Faktencheck gegen die im Roh-Text genannten Quellen → dem Menschen zur Freigabe vorlegen.
- Erst nach Freigabe: neue `src/<slug>.md` **und** `SUMMARY.md`-Eintrag, Transparenzhinweis
  oben und unten. Die Rohfassung nicht ungefragt löschen.
- **`raw/<thema>.md` ist gitignoriert** (nur `raw/README.md` + `raw/_vorlage.md` sind im Repo).
  Rohfassungen leben nur lokal; eine gelöschte ist endgültig weg, keine Wiederherstellung aus
  der Historie. Was bleiben soll, muss in die `src/`-Seite.

## 6. `.agents/`-Mirror

`.agents/` ist eine **Kopie** für Agent-Runner, die ihre Konfiguration unter `.agents/` statt
`.claude/` erwarten. `.claude/` ist die **Quelle der Wahrheit** — Änderungen immer dort machen,
danach in den Mirror spiegeln, nie umgekehrt.

**Was gespiegelt wird**:

| Quelle | Ziel im Mirror |
|--------|----------------|
| `.claude/agents/` | `.agents/agents/` |
| `.claude/skills/` | `.agents/skills/` |

> *Hinweis:* `AGENTS.md` bleibt nur im Repo-Root. Antigravity und moderne Agent-Runner laden
> automatisch sowohl `./AGENTS.md` als auch `.agents/AGENTS.md` — ein Duplikat im Mirror würde
> den gesamten Regeltext doppelt in jeden Context-Turn injizieren und unnötig Tokens verbrauchen.

`.agents/` ist **im Repo eingecheckt** — als byte-identische Kopie von `.claude/agents/` und
`.claude/skills/` (Stand: 14 Dateien). `.claude/` bleibt die **Quelle der Wahrheit**; der Mirror
wird mitversioniert, damit ein frischer Checkout ihn ohne Sync-Lauf hat. `.gitignore` enthält
für `.agents/` nur einen Kommentar, kein Ignore-Pattern. Die Root-`AGENTS.md` wird **nicht**
gespiegelt (siehe Hinweis oben). Nach jeder Änderung unter `.claude/agents/` oder
`.claude/skills/`: Sync + Verifikation laufen lassen und den Mirror mitcommitten.

**Sync (Quelle → Mirror):**

```
mkdir -p .agents
rsync -a --delete .claude/agents/ .agents/agents/
rsync -a --delete .claude/skills/ .agents/skills/
```

Ohne `rsync`: `rm -rf .agents/agents .agents/skills && cp -r .claude/agents .claude/skills .agents/`.

**Verifikation (Mirror == Quelle?):**

```
diff -rq .claude/agents .agents/agents
diff -rq .claude/skills .agents/skills
```

Beide ohne Ausgabe → **in Sync**. Jede Zeile → betroffene Datei aus `.claude/` neu kopieren. Nach
jeder Änderung an den `redaktion-*`-Subagenten oder der `co-wiki`-Skill den Sync + die Verifikation
laufen lassen.

## Related pages

- [`deploy-verification.md`](deploy-verification.md) — vollständiges Deploy-Runbook.
- [`verification/README.md`](verification/README.md) — Render-Verifikationsscreenshots.
- [`../raw/README.md`](../raw/README.md) — Roh-Ordner für menschliche Entwürfe.
- [`../CLAUDE.md`](../CLAUDE.md) / [`../AGENTS.md`](../AGENTS.md) — Konventionen und Agent-Regeln.
