---
type: Audit Report
title: Urheberrechts- und Plagiatsprüfung vom 14. November 2026
description: Vollständiges Dateiscreening, gezielte externe Quellenvergleiche und durchgeführte Korrekturen.
tags:
  - urheberrecht
  - validation
  - co-wiki
---

# Prüfbericht: Urheberrechts- und Plagiatsprüfung

**Datum:** 2026-11-14  
**Bereich:** 65 Markdown-Dateien unter `src/`, davon 59 redaktionelle Inhaltsseiten, ein Inhaltsverzeichnis, zwei Pflichttextseiten und drei generierte OpenWiki-Spiegelungen.  
**Auftrag:** Prüfung und direkte Überarbeitung auffälliger Stellen. Die ausdrückliche Änderungsanweisung des Nutzers geht dem reinen Berichtsmodus der Skill vor. Veröffentlichung gehört nicht zu diesem Auftrag.

## Ergebnisübersicht

- **HOCH:** 0 nachgewiesene kritische Übernahmen in den geprüften Vergleichen.
- **MITTEL:** 3 Verdachts- oder Zitatbefunde; alle bearbeitet.
- **NIEDRIG:** 4 redaktionelle Befundgruppen; alle bearbeitet.
- **Offene konkrete Korrekturen aus diesen sieben Befunden:** 0.

Das Ergebnis ist kein Nachweis, dass der gesamte Bestand frei von Rechtsverletzungen ist. Insbesondere wurde nicht jeder Absatz mit sämtlichen denkbaren Vorlagen abgeglichen. Die mittleren Befunde sind keine gerichtlich oder anwaltlich festgestellten Urheberrechtsverletzungen. Tatsachenähnlichkeiten und übliche Formulierungen wurden nicht als Plagiate gezählt.

## Umfang und Methode

Alle 65 Dateien wurden nach Quellenlinks, Wikipedia-Herkunftsblöcken, Zitaten, Bildverweisen, internen Links und längeren identischen Absätzen gescreent. Das Inhaltsverzeichnis wurde als Katalog hinzugezogen. Die öffentliche Prosa und auffällige Quellenverweise wurden gezielt gesichtet; historische und technische Themen erhielten zusätzliche externe Quellenstichproben durch zwei Recherche-Agenten gemäß `AGENTS.md`.

Die acht vorhandenen Abschnitte `Wikipedia als Quelle` enthalten jeweils Artikelverweise, Autorenverweis über die Versionsgeschichte, Lizenzlink, Bearbeitungshinweis und Weitergabe unter gleicher Lizenz. Ein fehlender solcher Abschnitt bei einem bloßen Wikipedia-Weblink ist für sich kein Lizenzverstoß. Die tatsächlich früher verwendeten Wikipedia-Revisionsnummern sind nicht dokumentiert und wurden nicht nachträglich erfunden.

Die Pflichttexte `datenschutz.md` und `impressum.md` wurden inventarisiert, aber nicht rechtlich umfassend geprüft. `SUMMARY.md` dient als Katalog. Die drei OpenWiki-Spiegelungen wurden nicht redaktionell verändert. Ein Suchmaschinenabgleich kann unbekannte, nicht indexierte, kostenpflichtige oder gedruckte Vorlagen nicht ausschließen. Ein systematischer Übersetzungsabgleich fand nicht statt.

## Übersicht der auffälligen Stellen

Zeilen beziehen sich auf den Arbeitsstand vor den Änderungen dieses Audits, einschließlich bereits vorhandener Nutzeränderungen.

| Nr. | Datei / Zeile vorher | Quelle oder Prüfmaßstab | Befund | Grad | Ergebnis |
|---|---|---|---|---|---|
| 1 | `src/ahrensburger-tunneltal.md:11` | LANU-Faltblatt zum Alfred-Rust-Wanderweg | Verdacht auf zu quellennahe Auswahl und Abfolge | MITTEL | Absatz neu aufgebaut und gekürzt |
| 2 | `src/familie-schimmelmann.md:33` | Nicht identifizierte Rezension | Wörtliches Werturteil ohne überprüfbare Herkunft | MITTEL | Zitat entfernt, Datierungsunsicherheit benannt |
| 3 | `src/familie-schimmelmann.md:45` | Tobias von Pein, Rechenschaftsbericht 2020 | Unbelegtes politisches Wortzitat | MITTEL | Sachliche Aussage mit Primärnachweis |
| 4 | `src/ahrensburger-tunneltal.md:55` | Lizenznachweise der verlinkten Angebote | Nicht belegte gemeinsame Einordnung als frei lizenziert | NIEDRIG | Neutrale Quellenüberschrift |
| 5 | `src/hauptseite.md:15`, `src/wissen-speichern.md:264`, `src/urheberrecht-und-duplicate-content.md:11/19/74/80/85`, `src/llm-wiki.md:239` | UrhG und CC-Lizenz | Zu pauschale Aussagen über Nutzungsrechte und Prüferfolg | NIEDRIG | Eingeschränkt und erläutert |
| 6 | `src/stadtwappen.md:57/66/67/83` | Wappenrolle und Hauptsatzung | Indirekter Quellenverweis; falscher Paragraph; zu pauschale Freigabe | NIEDRIG | Direkte Belege, § 1 und präzisierter Hinweis |
| 7 | `src/llm-wiki.md:165–188` | Nicht genau zugeordnete Erfahrungsberichte | Unbelegte Größen- und Wartungsangaben | NIEDRIG | Ohne unbelegte Zahlen neu formuliert |

## Detaillierte Befunde und ausgeführte Maßnahmen

### 1. Entstehung des Tunneltals

- **Wiki-Auszug vorher:** „das Eis wird bei Ahrensburg auf rund 300 Meter Dicke geschätzt“.
- **Vorlage:** [LANU: Alfred-Rust-Wanderweg im Stellmoor-Ahrensburger Tunneltal](https://umweltanwendungen.schleswig-holstein.de/Natura2000/pdf/bis/alfred_rust_wanderweg_im_stellmoor_ahrensburger_tunneltal.pdf).
- **Befundart / Grad:** Verdacht auf enge Paraphrase, **MITTEL**.
- **Begründung:** Der lange Absatz folgte einer auffälligen Kette aus Eisdicke, Schmelzwasserrinne, Toteis, örtlichem See, Verlandung und Wasserscheide. Diese Abfolge begründet eine redaktionelle Prüfung, beweist aber keine geschützte Übernahme. Der behördliche Herausgeber allein belegt keine Gemeinfreiheit des Faltblatts.
- **Umgesetzt:** Die ausführliche Nacherzählung wurde durch eine kurze Erklärung der Landschaftsmerkmale ersetzt; besondere Zahlen und die konkrete Detailkette entfallen. Das Faltblatt bleibt als weiterführender Link erhalten. Wikipedia-Attribution bleibt erhalten.

### 2. Nicht identifizierte Rezension

- **Wiki-Auszug vorher:** „eine besondere Auszeichnung unter den holsteinischen adligen Gütern“.
- **Vermutete Quelle:** Im Text nur als Rezension der Forschungsliteratur bezeichnet; Autor, Titel und Fundstelle fehlen.
- **Befundart / Grad:** Quellen- und Zitatlücke, **MITTEL**; keine gesicherte unzulässige Übernahme.
- **Umgesetzt:** Das fremde Werturteil wurde entfernt. Für die örtliche Aufhebung der Leibeigenschaft wird keine unbelegte genaue Datierung behauptet. Ein Nachweis der ursprünglichen Rezension bleibt für die jetzt entfernte Passage entbehrlich; sie darf ohne Prüfung nicht wieder eingefügt werden.

### 3. Politisches Wortzitat

- **Wiki-Auszug vorher:** „keine Ehrung, sondern Mahnung und Aufarbeitung“.
- **Abgleich:** [Tobias von Pein: Rechenschaftsbericht 2020, Seite 7](https://www.spd-stormarn.de/wp-content/uploads/2021/08/2020_Rechenschaftsbericht-Tobias-von-Pein-MdL.pdf).
- **Befundart / Grad:** Nicht belegtes Wortzitat, **MITTEL**. Der Bericht belegt die politische Forderung, nicht den behaupteten Wortlaut.
- **Umgesetzt:** Zitat und nicht nachgewiesene genaue zeitliche Zuschreibung entfallen. Die Forderung nach Mahnmal und Straßenumbenennung wird sachlich mit dem Bericht belegt.

### 4. Quellenüberschrift

- **Wiki-Auszug vorher:** „Amtliche und frei lizenzierte Quellen“.
- **Grad:** **NIEDRIG**.
- **Begründung / Maßnahme:** Für sämtliche darunter verlinkten Vereins- und Forschungstexte war keine freie Lizenz nachgewiesen. Die Überschrift lautet nun „Quellen und Hintergrund“. Ein Link ist keine Erlaubnis zur Textübernahme.

### 5. Pauschale Freigaben und rechtliche Erläuterungen

- **Wiki-Auszüge vorher:** „der ganze Textbestand ist frei kopierbar“; „Die Share-Alike-Bedingung ist damit automatisch erfüllt“.
- **Maßstab:** [CC BY-SA 4.0, Abschnitt 3](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de#s3), [§ 2 UrhG](https://www.gesetze-im-internet.de/urhg/__2.html), [§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html), [§ 23 UrhG](https://www.gesetze-im-internet.de/urhg/__23.html), [§ 87b UrhG](https://www.gesetze-im-internet.de/urhg/__87b.html).
- **Befundart / Grad:** Redaktionelle Überdehnung der Freigabe, **NIEDRIG**; keine nachgewiesene Textübernahme.
- **Umgesetzt:** Lizenzhinweise unterscheiden eigene Texte, fremde Zitate und verlinkte Angebote. Gleiche Lizenzen ersetzen keine Herkunftsangaben. Behörden-Websites sind nicht pauschal gemeinfrei. Einzelne Fakten erlauben keine beliebige Übernahme ganzer Datenbestände. Eine feste Anzahl gleicher Wörter oder die Satzanzahl einer Zusammenfassung entscheidet nicht über die rechtliche Zulässigkeit. Die unbelegte pauschale Entwarnung eines früheren Audits wurde durch den dokumentierten Umfang dieses Audits ersetzt.

### 6. Amtliche Wappen- und Flaggenbeschreibungen

- **Wiki-Auszug vorher:** „§ 2 der Hauptsatzung“.
- **Nachweise:** [Kommunale Wappenrolle, Datenblatt 374](https://efi2.schleswig-holstein.de/wr/wr.asp?Aktion=Datenblatt&ID=374), [Hauptsatzung, § 1](https://www.ahrensburg.de/media/custom/2603_1227_1.PDF?1531379840=).
- **Befundart / Grad:** Quellen- und Darstellungshinweis, **NIEDRIG**, kein Plagiatvorwurf gegen die amtlichen Beschreibungen.
- **Umgesetzt:** Quellen direkt verlinkt, Paragraph korrigiert, Genehmigungsregel näher am Satzungswortlaut beschrieben. Keine pauschale Freigabe von Bildern und erläuternden Texten der Wappenrolle.

### 7. Nicht zugeordnete Erfahrungsberichte

- **Wiki-Auszug vorher:** „alle paar Wochen einige Minuten bis eine halbe Stunde“.
- **Vermutete Quelle:** Ein Erfahrungsbericht wird erwähnt, aber nicht eindeutig der Aussage zugeordnet. Der Vergleich mit der verlinkten Karpathy-Notiz und dem Erfahrungsbericht von Leandro Bernardo ergab keinen konkreten Beleg für eine geschützte Wortübernahme.
- **Befundart / Grad:** Nachweislücke, **NIEDRIG**.
- **Umgesetzt:** Unbelegte Wartungszeiten und Seitengrenzen entfernt; Fehlerfortpflanzung und Wartungsbedarf eigenständig als betriebliche Aufgaben erklärt.

## Weitere Prüfergebnisse und Grenzen

- Die Betriebsbezeichnungen im Schimmelmann-Artikel ähneln einer Aufzählung im [Stormarn-Lexikon](https://www.stormarnlexikon.de/heinrichcarlschimmelmann/). Die Nennung von Brauerei, Brennerei und Mühlen ist hier eine Tatsachenüberschneidung; daraus wurde kein Plagiatbefund abgeleitet.
- Verweise auf Zeitungsangebote in `ahrensburg-nachrichten-website.md` sind kurze Linkbeschreibungen. Eine Übernahme von Zeitungspassagen wurde dort nicht nachgewiesen.
- Gezielte Suchphrasen aus Natur-, Stadtwerdungs- und Technikartikeln ergaben keine weiteren belastbaren exakten Fremdtreffer. Unspezifische Suchergebnisse trotz Anführungszeichen wurden nicht als Treffer gewertet.
- Die Veranstalterseite [Music for free 2025](https://www.ahrensburger-stadtforum.de/termine/music-for-free/) bestätigt Veranstaltungsdaten, die im Wiki verkürzt wiedergegeben sind. Gleiche Zahlen und Veranstaltungsnamen begründen keinen geschützten Sprachübernahmebefund.
- Die Technikprüfung umfasste zwölf Dateien einschließlich der sechs Vergleichsartikel, `cms-millionen-artikel`, `llm-wiki`, `wissen-speichern`, `wissenssystem-selbst-bauen`, `co-wiki`, `neue-artikel-erstellen` und `software-fuer-ein-grosses-wissensprojekt`; die Überschneidungen dieser Gruppen werden nicht doppelt gezählt. Geprüft wurden unter anderem die [Karpathy-Originalnotiz](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) und der [verlinkte Erfahrungsbericht](https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a). Der verlinkte Codecentric-Artikel war im Recherchewerkzeug nicht abrufbar; sein vollständiger Vergleich bleibt eine Prüfgrenze.
- Längere identische Absätze im Bestand beschränken sich beim exakten Absatzvergleich auf wiederkehrende interne Fachwort-Wegweiser. Transparenz- und Herkunftsbausteine wurden als beabsichtigte Wiederholungen ausgenommen.
- Im Markdown-Screening wurden keine eingebetteten Bildverweise gefunden. Eine eigenständige Rechteprüfung sämtlicher sonstiger Repository-Assets oder externer Websites gehört nicht zu diesem Textaudit.
- Nicht Gegenstand dieses Audits sind die vollständige Faktenprüfung aller Angaben, Datenschutzkonformität, Markenrechte und sämtliche Vorgaben des EU AI Act.

## Validierung und Veröffentlichung

Die Herkunftsblöcke und relativen Dateilinks wurden nach den Änderungen erneut geprüft. Zwei durch bereits vorhandene Seitenzusammenlegungen veraltete Links in `alltag-leben-in-ahrensburg.md` wurden auf die erhaltenen Seiten umgestellt. Bekannte relative Verweise der generierten OpenWiki-Spiegelung bleiben als ausgenommene Fremdstruktur unverändert. Ein Build oder Deploy wurde nicht ausgeführt; laut Co-Wiki-Regel erfordert dies eine ausdrückliche Anweisung.

Vor einer Veröffentlichung muss die Redaktion den Diff und die Belege prüfen. Eine unabhängige rechtliche Beurteilung kann erforderlich sein, wenn belastbare Rechtefreiheit über den hier dokumentierten Quellenvergleich hinaus verlangt wird. Es wird keine pauschale Rechtssicherheitsgarantie abgegeben.

## Vollständiges Dateiinventar

Die folgende Tabelle dokumentiert das Screening je Datei. „Screening“ bedeutet die oben beschriebenen heuristischen Kontrollen, keinen vollständigen externen Absatzvergleich. Der SHA-256-Präfix bezeichnet den geprüften Endstand der jeweiligen Datei.

| Datei | Prüfumfang | Wikipedia-Block | SHA-256 (Präfix) |
|---|---|---|---|
| `src/SUMMARY.md` | Katalog und Dateilinks | — | `5c97553772b3` |
| `src/ahrensburg-nachrichten-website.md` | Screening | — | `2c39aabc2d97` |
| `src/ahrensburg-ns-zeit.md` | Screening | vollständig im formalen Check | `7e9786b27c69` |
| `src/ahrensburger-tunneltal.md` | Screening | vollständig im formalen Check | `678567732e78` |
| `src/alltag-leben-in-ahrensburg.md` | Screening | — | `a0e2962b293f` |
| `src/buergermeister-und-stadtvertretung.md` | Screening | — | `b42ceb6bc152` |
| `src/cms-im-vergleich.md` | Screening | — | `9a8a9b05d2c5` |
| `src/cms-millionen-artikel.md` | Screening | — | `e1e65d375142` |
| `src/co-wiki.md` | Screening | — | `a6dd41d55560` |
| `src/datenschutz.md` | Inventar; Pflichttext ausgenommen | — | `2e9c98b14733` |
| `src/demografie.md` | Screening | vollständig im formalen Check | `0b2ca8a3132c` |
| `src/die-stadtteile-im-portraet.md` | Screening | — | `12bb8af48440` |
| `src/doku-generatoren-im-vergleich.md` | Screening | — | `819954ba8e35` |
| `src/einkaufen-in-ahrensburg.md` | Screening | — | `8c8cf5e02979` |
| `src/familie-bildung.md` | Screening | — | `3158adcd97f7` |
| `src/familie-rantzau.md` | Screening | vollständig im formalen Check | `97c3b0fc765f` |
| `src/familie-schimmelmann.md` | Screening | vollständig im formalen Check | `724f72b10acf` |
| `src/fauna-und-flora.md` | Screening | — | `aec2970d2af1` |
| `src/gastronomie-fuehrer.md` | Screening | — | `c14b5f7ff84a` |
| `src/geografie.md` | Screening | — | `6c180ea89514` |
| `src/geschichte-allgemeines.md` | Screening | — | `bbf25ef19fa1` |
| `src/geschichte-der-stadt-ahrensburg.md` | Screening | — | `e0da4c6d65dd` |
| `src/gesundheit.md` | Screening | — | `4aea285d6bde` |
| `src/gewaesser-und-seen.md` | Screening | — | `1e541aa1e459` |
| `src/gewerbegebiete.md` | Screening | — | `7f913229c500` |
| `src/gottesbuden.md` | Screening | vollständig im formalen Check | `2286004b1ddd` |
| `src/hauptseite.md` | Screening | — | `1cc10db066ad` |
| `src/impressum.md` | Inventar; Pflichttext ausgenommen | — | `a9dbb7a7dc60` |
| `src/infrastruktur-wirtschaft.md` | Screening | — | `dc07b5ab4791` |
| `src/kirchen-und-religioese-gemeinschaften.md` | Screening | — | `d1e315fbddd9` |
| `src/llm-wiki.md` | Screening | — | `8005d0a9a4ca` |
| `src/musik-und-theater.md` | Screening | — | `ff78d7175775` |
| `src/naherholungsgebiete.md` | Screening | — | `c0f815d89177` |
| `src/natur-freizeit.md` | Screening | — | `48492c7dbac9` |
| `src/naturschutzgebiete.md` | Screening | — | `d79295c3ce16` |
| `src/neue-artikel-erstellen.md` | Screening | — | `10ee01877944` |
| `src/openwiki/architecture.md` | Inventar; generiert, ausgenommen | — | `41086e8c2325` |
| `src/openwiki/overview.md` | Inventar; generiert, ausgenommen | — | `cc449bbae084` |
| `src/openwiki/source-map.md` | Inventar; generiert, ausgenommen | — | `09d900693425` |
| `src/ortsname-ahrensburg.md` | Screening | vollständig im formalen Check | `1105c5b91419` |
| `src/persoenlichkeiten.md` | Screening | vollständig im formalen Check | `9cfc8914ed7f` |
| `src/regelmaessige-feste-veranstaltungen.md` | Screening | — | `1daf3994d2a5` |
| `src/restaurant.md` | Screening | — | `74489ac06405` |
| `src/schloss-ahrensburg.md` | Screening | — | `5f75cd31352c` |
| `src/schlosskirche-ahrensburg.md` | Screening | — | `5650c2a71c7d` |
| `src/sehenswuerdigkeiten-kultur.md` | Screening | — | `a63b9659632c` |
| `src/sehenswuerdigkeiten.md` | Screening | — | `e2abfe2a6486` |
| `src/seniorentreff.md` | Screening | — | `01ec7cd4e2f6` |
| `src/software-fuer-ein-grosses-wissensprojekt.md` | Screening | — | `6b7494eeae67` |
| `src/spielplaetze.md` | Screening | — | `cd3284fd30c0` |
| `src/stadtverwaltung.md` | Screening | — | `554e3d649ebd` |
| `src/stadtwappen.md` | Screening | — | `18fe94e0fa64` |
| `src/stadtwerdung-1949.md` | Screening | — | `00e0b9d953ca` |
| `src/uebernachtungsmoeglichkeiten-in-ahrensburg.md` | Screening | — | `b3c0cdf16e94` |
| `src/urheberrecht-und-duplicate-content.md` | Screening | — | `9079f939a627` |
| `src/vereinsleben.md` | Screening | — | `ac13e70db152` |
| `src/verkehrsanbindung.md` | Screening | — | `ce94a014653d` |
| `src/wander-und-radwege.md` | Screening | — | `4ed079a36395` |
| `src/webframeworks-im-vergleich.md` | Screening | — | `51c7ce60f045` |
| `src/wichtige-unternehmen-arbeitgeber.md` | Screening | — | `6df17013b594` |
| `src/wikis-im-vergleich.md` | Screening | — | `4c479412e86a` |
| `src/wissen-speichern.md` | Screening | — | `1fa1e1348d01` |
| `src/wissenssystem-selbst-bauen.md` | Screening | — | `94c8f150d716` |
| `src/wissenssysteme-im-vergleich.md` | Screening | — | `b2c287f2f85e` |
| `src/wochenmarkt.md` | Screening | — | `f69920ed3b37` |

## Related pages

- [AGENTS.md](../AGENTS.md)
- [Verwendete Prüf-Skill](../.agents/skills/urheberrecht-pruefung/SKILL.md)
- [Co-Wiki-Skill](../.agents/skills/co-wiki/SKILL.md)
- [Urheberrecht und Duplicate Content](../src/urheberrecht-und-duplicate-content.md)
