---
type: Audit Report
title: Urheberrechtliche Fachprüfung vom 14. November 2026 (Aktualisierter Gesamtstand)
description: Vertiefte redaktionelle Rechteprüfung aller 66 Wiki-Dateien nach Kapitelausbau, mit Quellen- und Rechtematrix, Duplicate-Content-Abgleich und Veröffentlichungsempfehlung.
tags:
  - urheberrecht
  - fachpruefung
  - duplicate-content
  - validation
  - co-wiki
  - legal
---

# Urheberrechtliche Fachprüfung (Gesamtbestand: 66 Dateien)

**Datum:** 14. November 2026 (2. Prüfdurchlauf nach Inhaltsausbau)  
**Rechtsraum:** Bundesrepublik Deutschland (maßgeblich: [Urheberrechtsgesetz (UrhG)](https://www.gesetze-im-internet.de/urhg/), Gesetz über das Urheberrecht an Werken der bildenden Künste und der Photographie [KunstUrhG], [Creative Commons Attribution-ShareAlike 4.0 International [CC BY-SA 4.0]](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)).  
**Geprüfter Stand:** Basis-Commit `585822dd32aef9f8f96dea067f5af12ef000eb35` zuzüglich sämtlicher redaktionellen Bereinigungen, dem substanziellen Ausbau von 15 Orts- und Überblickskapiteln sowie der Neuanlage von `src/urheberrecht-pruefroutine-und-skills.md` vom 14. November 2026 (maßgeblich sind die dokumentierten SHA-256-Dateihashes).  
**Prüfumfang:** Vollständiger Bestand aller **66 Markdown-Dateien** unter `src/` (60 redaktionelle Inhaltsseiten, ein Inhaltsverzeichnis `SUMMARY.md`, zwei gesetzliche Pflichttextseiten sowie drei maschinell generierte OpenWiki-Dokumentationsspiegelungen). Keine eingebetteten Bild- oder Multimediadateien im Dateibestand vorhanden.  
**Art der Prüfung:** Redaktionelle Rechteprüfung, vertiefter Quellenabgleich und automatisierte Duplicate-Content-Kontrolle (keine anwaltliche Rechtsberatung, kein gerichtliches Gutachten).

---

## Kernfrage: Kann ich veröffentlichen?

### Empfehlung

> **Redaktionell zur Veröffentlichung empfohlen.**

### Entscheidende Gründe

1. **Vollständige Erfassung aller 66 Kapitel:** Der gesamte aktuelle Bestand unter `src/` – einschließlich der 15 neu ausgebauten Fach- und Überblickskapitel sowie des neu erstellten Leitfadens `src/urheberrecht-pruefroutine-und-skills.md` – wurde vollständig inventarisiert, mit SHA-256-Prüfsummen versehen und quellenbezogen abgeglichen.
2. **Lückenlose CC BY-SA 4.0-Rechtekette:** Alle acht Inhaltsseiten mit Vorlagen aus der deutschsprachigen Wikipedia (`ahrensburg-ns-zeit.md`, `ahrensburger-tunneltal.md`, `demografie.md`, `familie-rantzau.md`, `familie-schimmelmann.md`, `gottesbuden.md`, `ortsname-ahrensburg.md`, `persoenlichkeiten.md`) erfüllen die kumulativen Lizenzanforderungen von CC BY-SA 4.0 (Abschnitt 3):
   - Verlinkung der Wikipedia-Ursprungsartikel zur Autorennennung über die Versionsgeschichte,
   - Nennung und Verlinkung der Lizenz CC BY-SA 4.0,
   - Ausdrückliche Kennzeichnung der Vornahme von Bearbeitungen (Kürzung, Neugliederung, sprachliche Überarbeitung),
   - Lizenzierung der abgeleiteten Seiten unter derselben Lizenz (Share-Alike).
3. **Urheberrechtskonformer Ausbau der 15 erweiterten Kapitel:** Die im zweiten Arbeitsschritt umfassend ausgebauten 15 Seiten (`alltag-leben-in-ahrensburg.md`, `die-stadtteile-im-portraet.md`, `einkaufen-in-ahrensburg.md`, `gastronomie-fuehrer.md`, `geschichte-allgemeines.md`, `geschichte-der-stadt-ahrensburg.md`, `infrastruktur-wirtschaft.md`, `natur-freizeit.md`, `schlosskirche-ahrensburg.md`, `sehenswuerdigkeiten-kultur.md`, `sehenswuerdigkeiten.md`, `seniorentreff.md`, `spielplaetze.md`, `verkehrsanbindung.md`, `wochenmarkt.md`) stützen sich ausschließlich auf gemeinfreie Sachfakten ([§ 2 Abs. 2 UrhG](https://www.gesetze-im-internet.de/urhg/__2.html)) und weisen eine vollständig eigenständige Gliederung und Sprachgestaltung ([§ 23 UrhG](https://www.gesetze-im-internet.de/urhg/__23.html)) auf.
4. **Erfolgte Bereinigung sämtlicher Vorprüfungs-Befunde:** Alle sieben im ersten Screening identifizierten Auffälligkeiten (geologische Detailabfolge im Tunneltal, unbelegtes Werturteil und Wortzitat bei Schimmelmann, Wappenrollen- und Satzungsbelege, präzisierte Lizenzhinweise) sind vollständig behoben.
5. **Freiheit von internem Duplicate Content:** Der automatisierte N-Gramm-/Jaccard-Abgleich über alle 66 Dateien via `scripts/find_duplicate_content.py` bestätigt, dass im redaktionellen Fließtext keine unzulässigen Textdopplungen zwischen den Kapiteln bestehen.
6. **Kein Bildrechte-Risiko & keine unzulässige Datenbankentnahme:** Im gesamten `src/`-Verzeichnis sind keine Bilddateien (`![]()`) eingebunden. Lokale Übersichten (Gastro, Hotels, Einkaufen, Spielplätze) stellen punktuelle Sachauswahlen ohne Eingriff in geschützte Datenbanken ([§ 87a ff. UrhG](https://www.gesetze-im-internet.de/urhg/__87a.html)) dar.

---

## 1. Prüfrahmen und vollständiges Seiteninventar (66 Dateien)

### Rechtsgrundlagen und Prüfmaßstäbe

- **§ 2 UrhG (Geschützte Werke):** Sprachwerke genießen nur Schutz, wenn sie persönliche geistige Schöpfungen sind. Bloße Tatsachen, historische Jahreszahlen, geographische Angaben, Öffnungszeiten, Liniennummern und statistische Kennzahlen sind gemeinfrei.
- **§ 5 UrhG (Amtliche Werke):** Gesetze, Verordnungen, amtliche Erlasse und Bekanntmachungen (einschließlich amtlicher Wappenblasonierungen) genießen keinen urheberrechtlichen Schutz. Nicht-amtliche Begleittexte oder Fotos auf Behördenportalen fallen nicht pauschal unter § 5 UrhG.
- **§ 23 UrhG (Bearbeitungen und Umgestaltungen):** Bearbeitungen eines Werkes dürfen nur mit Einwilligung veröffentlicht werden. Wahrung eines hinreichenden inneren und äußeren Abstands begründet ein eigenständiges Werk.
- **§ 51 UrhG (Zitate):** Zulässig bei echtem Beleg- oder Auseinandersetzungszweck, unveränderter Wiedergabe, angemessenem Umfang und Quellenangabe (§ 63 UrhG).
- **§ 87a, § 87b UrhG (Datenbankherstellerrecht):** Untersagt die Entnahme nach Art oder Umfang wesentlicher Teile einer geschützten Datenbank.
- **Lizenzvertrag CC BY-SA 4.0:** Verlangt Autorennennung (BY), Lizenzangabe mit Link, Änderungshinweis sowie Weitergabe unter derselben Lizenz (SA).

### Vollständiges Seiteninventar mit Prüfsummen

| Lfd. | Relativer Pfad | Zeilen | Wörter | SHA-256 (Aktueller Prüfstand) |
|---|---|---|---|---|
| 1 | `src/SUMMARY.md` | 79 | 245 | `23e2e3caa82e60ec439d2999f392c09e53498b1e1a5c7a6b3837d0b0bf04a5d4` |
| 2 | `src/ahrensburg-nachrichten-website.md` | 33 | 240 | `2c39aabc2d97f1858e16b09e70a9e1df732119c45ef10e06347698c47eecc1a5` |
| 3 | `src/ahrensburg-ns-zeit.md` | 71 | 689 | `7e9786b27c6909cf5b68a3644b8fb39ae627a494291100cd34c81789771a8170` |
| 4 | `src/ahrensburger-tunneltal.md` | 78 | 945 | `678567732e787983dde338ab10d899e334487312b89396c9a7a62281c601413e` |
| 5 | `src/alltag-leben-in-ahrensburg.md` | 46 | 430 | `15bd7c289a5ad3af2356032d37a85bb1d8fc86f233f4256bddfbabc946931396` |
| 6 | `src/buergermeister-und-stadtvertretung.md` | 94 | 788 | `b42ceb6bc1527e26e020c4b6865b80b254cbc2198099385afd18af12be1eebeb` |
| 7 | `src/cms-im-vergleich.md` | 214 | 1550 | `9a8a9b05d2c522c5be817c7b18e8c5abdd1e6210779810f14629ae3f982f7294` |
| 8 | `src/cms-millionen-artikel.md` | 350 | 2574 | `e1e65d375142d0a985e833143391f06671e33af14603c22f50dc3dadf6f75bc6` |
| 9 | `src/co-wiki.md` | 102 | 1043 | `a6dd41d55560b30f116bfe2a9505bb6b561da8023f9ae3f2064eb8521cfe9542` |
| 10 | `src/datenschutz.md` | 47 | 636 | `2e9c98b14733b10c4e190e9b64cd7902812fce20fafc8b2c97e7b76a8ce22f01` |
| 11 | `src/demografie.md` | 89 | 830 | `0b2ca8a3132cda591d7dcf72cfa1d24004b997bcca4a640725942e1c76c0270e` |
| 12 | `src/die-stadtteile-im-portraet.md` | 80 | 620 | `2d82541e8890ec7be843431157b81bae7a2b681aca36cf2a6c63723e935b554f` |
| 13 | `src/doku-generatoren-im-vergleich.md` | 185 | 1306 | `819954ba8e353fdd37c16a72e5c9d757aff2b8da7f06726ebd228953ba5ce1d5` |
| 14 | `src/einkaufen-in-ahrensburg.md` | 69 | 499 | `af8754dfe471f40faa5a6e9160201706a53aaefb6b7c18f6794ddf264b3f1eee` |
| 15 | `src/familie-bildung.md` | 42 | 404 | `3158adcd97f73eb3fbfb0eb643df28d8f531dc6c66bedc15858cc044b7dbcf39` |
| 16 | `src/familie-rantzau.md` | 69 | 1002 | `97c3b0fc765fbb269cf21acfde7c010607a09475859de7c4f36bae0f466e2a62` |
| 17 | `src/familie-schimmelmann.md` | 60 | 1047 | `724f72b10acf3fbedb82229e1be53375c1b4801bfb5e451bee6c2102d603564b` |
| 18 | `src/fauna-und-flora.md` | 88 | 487 | `aec2970d2af12a605bdc6d048d0a84b0b0d05f427e11ada2bf27fd2ded290d5b` |
| 19 | `src/gastronomie-fuehrer.md` | 57 | 381 | `f8c574584f9b715a883e25e0e2e4fbf12fe7d3fe8f2c48f434a5ac43eb0eab4e` |
| 20 | `src/geografie.md` | 136 | 837 | `6c180ea89514d915c3495e005e652bc81bf6389008dbc9d02fa2b53666401226` |
| 21 | `src/geschichte-allgemeines.md` | 44 | 467 | `ed715ff948283fe005ac7f7bf52178c143925ac3cf57b31868357318ed8cfc16` |
| 22 | `src/geschichte-der-stadt-ahrensburg.md` | 40 | 469 | `ce189aedc3bdd3d828dccd3615053b24f49932fb8e6180af481fa0c5ed9fd1d4` |
| 23 | `src/gesundheit.md` | 30 | 228 | `4aea285d6bde056034ac19fb1eeadd5facfd56798dc612b3e145add7eb96feda` |
| 24 | `src/gewaesser-und-seen.md` | 111 | 952 | `1e541aa1e459ba94ea3716d7d00294a98116ec8c67428aef5a46eb931b21eaad` |
| 25 | `src/gewerbegebiete.md` | 19 | 218 | `7f913229c50081a11d379621936dc838a9d9dfe61bf747345685239839116ca0` |
| 26 | `src/gottesbuden.md` | 34 | 216 | `2286004b1ddddbfa3dc02a7f230f88331e3041bb60eccde537dd443174790163` |
| 27 | `src/hauptseite.md` | 63 | 455 | `1cc10db066ade7ed5b0892d1d6d704a047376e4256f7393d46cf6ba06c836fba` |
| 28 | `src/impressum.md` | 27 | 148 | `a9dbb7a7dc60f6898c1e50f05af910c4f9ed2bc73b0212c79415c50eda0951d8` |
| 29 | `src/infrastruktur-wirtschaft.md` | 38 | 367 | `c1f3fa3197c0fa5ce6c58095cf59bc1b06ba410928d3620b76088a714ec59d4a` |
| 30 | `src/kirchen-und-religioese-gemeinschaften.md` | 33 | 282 | `d1e315fbddd9aef4a51884b7123f6c321e95aa3268e6e8d5039931795a2b26a7` |
| 31 | `src/llm-wiki.md` | 304 | 2186 | `8005d0a9a4caf1332ee8dcdce42ab4c312a3ee0ef0b561b750d716855bc39327` |
| 32 | `src/musik-und-theater.md` | 29 | 315 | `ff78d7175775b2d2f545e160badc7f286f8714ad860f2b8bb2904d73e01c83e6` |
| 33 | `src/naherholungsgebiete.md` | 44 | 297 | `c0f815d89177128ef43559fe1ad2cbdcf33ce78240a9d3d0de784c78bd2e482e` |
| 34 | `src/natur-freizeit.md` | 40 | 361 | `44f6d9b4fe735d7ccd7910c1c3e1bcd04b60a00de7e015aa656498016d0a9b48` |
| 35 | `src/naturschutzgebiete.md` | 103 | 813 | `d79295c3ce16f18b9a4f3ff0b6d0a27970e2bd55daca7a0ffa92cd45c89c9b3e` |
| 36 | `src/neue-artikel-erstellen.md` | 166 | 1268 | `10ee01877944509e42cf192930b8d313ec5c953f56950dfead161c2675ebd349` |
| 37 | `src/openwiki/architecture.md` | 170 | 934 | `41086e8c232502b85fe565be3171ec2333838d9b4c637bb319fefa0fd581926f` |
| 38 | `src/openwiki/overview.md` | 108 | 662 | `cc449bbae08417cbb5add94eeca73ea5c17b3bb07f73b6999c0ecff80e5053f4` |
| 39 | `src/openwiki/source-map.md` | 111 | 945 | `09d9006934250fafd30dfb7d7d304b07297328d95b7978f9aa4506b065d1d943` |
| 40 | `src/ortsname-ahrensburg.md` | 114 | 993 | `1105c5b914196b54352c009d511a9c8342b00295531e2106df928d68b8fb3799` |
| 41 | `src/persoenlichkeiten.md` | 137 | 1041 | `9cfc8914ed7f858259c297f152bae2a58f1f9b8ad47397945364fa74a6b7ee75` |
| 42 | `src/regelmaessige-feste-veranstaltungen.md` | 18 | 242 | `1daf3994d2a5bfdb0199ca792b87821d9635a0886e596a0a9437862d58bc3367` |
| 43 | `src/restaurant.md` | 52 | 657 | `74489ac064051f945ec521304c7829bf95fc73220203ba6134ddffadf356d8dd` |
| 44 | `src/schloss-ahrensburg.md` | 33 | 188 | `5f75cd31352c0d95002a45c1e5a6ba80e64cf54dfa8e8415e096061b4e006f92` |
| 45 | `src/schlosskirche-ahrensburg.md` | 50 | 461 | `5fced57f3aa67ab998b081238964a31eb071ff270e65bd34e601f092a4e90345` |
| 46 | `src/sehenswuerdigkeiten-kultur.md` | 34 | 331 | `74e08b506fa79384be001fcbc702069da445052c369d369d723b4638ac8ef2cb` |
| 47 | `src/sehenswuerdigkeiten.md` | 70 | 574 | `ab1da2b86a3590b62920148ecbf50fe919f1cc8e552335c3847e3b5fe8b6a249` |
| 48 | `src/seniorentreff.md` | 69 | 492 | `1ba92b6238d5fc10a09fcb31c6567088b7721d2a3977364ece0bee5bc8655625` |
| 49 | `src/software-fuer-ein-grosses-wissensprojekt.md` | 199 | 1608 | `6b7494eeae67578e588a2c11f56eb5b00b50797b81809672546670fedb17be41` |
| 50 | `src/spielplaetze.md` | 68 | 552 | `35192cd410a7f1d30077dce9daa74fe8cae0be2f706fffbefb8906311f7e9f73` |
| 51 | `src/stadtverwaltung.md` | 45 | 277 | `554e3d649ebddb515689963c6bd69198601bf7d65bca686168a28a82e64f19bb` |
| 52 | `src/stadtwappen.md` | 87 | 557 | `18fe94e0fa64ea168bb2cb64482cf37d4f867252335f30110e2e39398f8685de` |
| 53 | `src/stadtwerdung-1949.md` | 56 | 539 | `00e0b9d953cae9ce12d8ff34eaf58e477bb1690afed9a4f2449bb6f23e97031f` |
| 54 | `src/uebernachtungsmoeglichkeiten-in-ahrensburg.md` | 21 | 166 | `b3c0cdf16e947f3eb82312068052d59d7fcddea1c8be4538edf9c3b8f82079f7` |
| 55 | `src/urheberrecht-pruefroutine-und-skills.md` | 180 | 1568 | `03b248c2416ce025274789f0ba9e31e9a8860a253b510f4e2b8fa83c4b324136` |
| 56 | `src/urheberrecht-und-duplicate-content.md` | 126 | 1660 | `4a37f3573fa22dd2fdccd34d3585a8915b855de99f7e4310f62c28cb65df4c70` |
| 57 | `src/vereinsleben.md` | 21 | 282 | `ac13e70db1526ae555857c1d686f11cf96152126ea2ba68bb37af48ca1ba7fc4` |
| 58 | `src/verkehrsanbindung.md` | 58 | 509 | `e0997018c46905e1dfb9e49f7b9f3de3a1d8a51dff2ea6c40f9414f20a792056` |
| 59 | `src/wander-und-radwege.md` | 31 | 347 | `4ed079a3639506ff1d593a1fe5557c95e85a9f1a498329beb1c8dbcdb279d7fd` |
| 60 | `src/webframeworks-im-vergleich.md` | 305 | 2286 | `51c7ce60f0457d75ffcd618a8e708e812ad023aa21deee2d37727503fb4e27b3` |
| 61 | `src/wichtige-unternehmen-arbeitgeber.md` | 21 | 297 | `6df17013b594eb895e813d0dc8ce85292c4e91a83fcae427c0e60ed5bdbae147` |
| 62 | `src/wikis-im-vergleich.md` | 183 | 1396 | `4c479412e86a777e456f4205a3eb2b948d5bbe808b1ec197884ded8b0967e1b9` |
| 63 | `src/wissen-speichern.md` | 303 | 2113 | `1fa1e1348d01985f7e974d378dc4219cec8a329ce7482d3e843c1b0327e00e20` |
| 64 | `src/wissenssystem-selbst-bauen.md` | 344 | 2514 | `94c8f150d716fc3c53c3ad2ad9115fdd7a8bd4d7284c21f2f8e02fff49a63f77` |
| 65 | `src/wissenssysteme-im-vergleich.md` | 241 | 1811 | `b2c287f2f85e45fd8b36cb942098a963feae5db257e5a747c5742d5ffe1baaeb` |
| 66 | `src/wochenmarkt.md` | 46 | 382 | `99d9de5c302fa743684969ca2fb2e5edf2d37c968c7ffa70a6b705a759845a85` |

---

## 2. Quellen- und Rechtematrix (Alle 66 Seiten)

Jede Seite wurde anhand folgender Kategorien eingestuft:
- **abgeglichen:** Vertiefter Abgleich gegen Primärquelle, Gesetzestext, Lizenzbestimmungen oder nachgewiesene redaktionelle Eigenformulierung.
- **teilweise abgeglichen:** Relevante Fakten- und Linkabgleiche erfolgt; Restprüfung von Allgemeinwissen ohne Einzelbeleg.
- **begründet ausgenommen:** Maschinell generierter Index, Inhaltsverzeichnis oder gesetzlicher Betreiber-Pflichttext.

| Datei | Status | Identifizierte Vorlagen / Quellen | Nutzungsgrundlage | Herkunftsprüfung & Befund (Stand nach Ausbau) |
|---|---|---|---|---|
| `SUMMARY.md` | **begründet ausgenommen** | mdBook-Inhaltsverzeichnis | Gemeinfreie Struktur (§ 2 UrhG) | Kein Textwerk, reine Dateiliste (inkl. neuem Prüfkapitel) |
| `ahrensburg-nachrichten-website.md` | **abgeglichen** | Eigene Portalarchitektur | Eigene Schöpfung (§ 2 UrhG) | Keine Fremdvorlage, methodische Eigenentwicklung |
| `ahrensburg-ns-zeit.md` | **abgeglichen** | Wikipedia: *Ahrensburg* (Abschnitt Geschichte), *Liste der Stolpersteine in Ahrensburg* | CC BY-SA 4.0 | Vollständige Attribution, Link auf Artikel und Lizenz, Bearbeitungshinweis, Share-Alike |
| `ahrensburger-tunneltal.md` | **abgeglichen** | Wikipedia: *Ahrensburger Kultur*, *Stellmoor–Ahrensburger Tunneltal*, *Alfred Rust*; LANU-Faltblatt | CC BY-SA 4.0; Sachinformationen / Gemeingut | Entzerrte geologische Entstehung; Wikipedia-Attribution lückenlos vorhanden |
| `alltag-leben-in-ahrensburg.md` | **abgeglichen** | Kommunale Strukturdaten, Lebensbereiche | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (430 Wörter):** Eigenständige Überblicksdarstellung mit Querverweisen |
| `buergermeister-und-stadtvertretung.md` | **abgeglichen** | Gemeindeordnung SH, amtliche Wahlergebnisse | Gemeinfreie Fakten / amtl. Daten (§ 5 UrhG) | Sachliche Darstellung der Kommunalorgane |
| `cms-im-vergleich.md` | **abgeglichen** | Offizielle Webseiten & Doku von WordPress, TYPO3, Strapi, Ghost, Drupal | Eigene Fachdarstellung / Zitate (§ 51 UrhG) | Technischer Faktenvergleich, keine Fließtextübernahmen |
| `cms-millionen-artikel.md` | **abgeglichen** | Architekturanalysen, MediaWiki/OpenCms/TYPO3 Specs | Eigene Fachdarstellung (§ 2 UrhG) | Systematische Eigenanalyse von Enterprise-Architekturen |
| `co-wiki.md` | **abgeglichen** | Repository-Konzept `ahrensburg-buch` | Eigene Originalschöpfung | Dokumentiert die Kernidee dieses Wikis |
| `datenschutz.md` | **begründet ausgenommen** | DSGVO-Musterangaben | Gesetzlicher Pflichttext | Rechtliche Pflichterfüllung nach Art. 13 DSGVO |
| `demografie.md` | **abgeglichen** | Wikipedia: *Ahrensburg* (Einwohnerentwicklung), amtliche Statistik SH | CC BY-SA 4.0; amtl. Statistik (§ 5 UrhG) | Historische Zahlenfolge aus Wikipedia mit ordnungsgemäßer Attribution |
| `die-stadtteile-im-portraet.md` | **abgeglichen** | Geografische und städtebauliche Fakten | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (620 Wörter):** Eigenständige Quartiersporträts & Vergleichstabelle |
| `doku-generatoren-im-vergleich.md` | **abgeglichen** | mdBook, MkDocs, Docusaurus, Sphinx Specs | Eigene Fachdarstellung (§ 2 UrhG) | Eigenständige Benchmark- und Feature-Analyse |
| `einkaufen-in-ahrensburg.md` | **abgeglichen** | Öffentliche Standort-, Branchen- und Parkdaten | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (499 Wörter):** Innenstadt, Nessler, CCA, Fachmärkte; keine Datenbankübernahme |
| `familie-bildung.md` | **teilweise abgeglichen** | Schul- und Kita-Verzeichnisse der Stadt | Gemeinfreie Fakten (§ 2 UrhG) | Reine Namens- und Adressnennungen |
| `familie-rantzau.md` | **abgeglichen** | Wikipedia: *Rantzau (Adelsgeschlecht)*, *Daniel Rantzau*, *Peter Rantzau*, *Schloss Ahrensburg* | CC BY-SA 4.0 | Vollständige Attribution und korrekter Lizenzblock |
| `familie-schimmelmann.md` | **abgeglichen** | Wikipedia: *Schimmelmann*, *Heinrich Carl*, *Ernst Heinrich*; Tobias von Pein Rechenschaftsbericht 2020 | CC BY-SA 4.0; Sachzitat / Beleg (§ 51 UrhG) | Bereinigt um ungesichertes Zitat und fremdes Werturteil; Attribution lückenlos |
| `fauna-und-flora.md` | **teilweise abgeglichen** | Naturkundliche Schutzgebietsberichte | Gemeinfreie Fakten (§ 2 UrhG) | Deskriptive Artenliste der Region |
| `gastronomie-fuehrer.md` | **abgeglichen** | Regionale Kulinarik & Quartierslagen | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (381 Wörter):** Eigenständige Darstellung der Gastro-Lagen und Saisonküche |
| `geografie.md` | **abgeglichen** | Geodaten SH, amtliche topographische Beschreibungen | Gemeinfreie Sachdaten (§ 2 UrhG) | Reine Messdaten, Koordinaten, Flächengrößen |
| `geschichte-allgemeines.md` | **abgeglichen** | Historische Eckdaten der Stadtgeschichte | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (467 Wörter):** Fünf-Epochen-Überblick in eigenständiger Formulierung |
| `geschichte-der-stadt-ahrensburg.md` | **abgeglichen** | Historische Jahreszahlen & Meilensteine | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (469 Wörter):** Chronologische Zeitleiste und Themenpfade |
| `gesundheit.md` | **teilweise abgeglichen** | Öffentliche Notdienst- und Krankenhausdaten | Gemeinfreie Fakten (§ 2 UrhG) | Öffentliche Verzeichnisangaben |
| `gewaesser-und-seen.md` | **abgeglichen** | Gewässerverzeichnisse Landesamt SH | Gemeinfreie Naturdaten (§ 2 UrhG) | Eigenständige Beschreibung von Teichen, Flüssen |
| `gewerbegebiete.md` | **teilweise abgeglichen** | Städtische Wirtschaftsförderungsangaben | Gemeinfreie Fakten (§ 2 UrhG) | Lage- und Flächenangaben |
| `gottesbuden.md` | **abgeglichen** | Wikipedia: *Gottesbuden Ahrensburg*, *Schlosskirche Ahrensburg* | CC BY-SA 4.0 | Ordnungsgemäße Attribution mit Artikellinks und Lizenzverweis |
| `hauptseite.md` | **abgeglichen** | Eigene Projektbeschreibung | Eigene Schöpfung (§ 2 UrhG) | Lizenzaussage präzisiert; keine Fremdübernahme |
| `impressum.md` | **begründet ausgenommen** | Gesetzliche Anbieterkennzeichnung (§ 5 DDG) | Gesetzlicher Pflichttext | Individuelle Betreiberangaben |
| `infrastruktur-wirtschaft.md` | **abgeglichen** | Standortfaktoren, Verkehrs- und Versorgungsdaten | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (367 Wörter):** Fünf Standort-Säulen, Stadtwerke, Feuerwehr, Unternehmen |
| `kirchen-und-religioese-gemeinschaften.md` | **teilweise abgeglichen** | Verzeichnis lokaler Gemeinden | Gemeinfreie Fakten (§ 2 UrhG) | Adress- und Kontaktangaben |
| `llm-wiki.md` | **abgeglichen** | Karpathy LLM-Wiki-Konzept, Lizenzbestimmungen | Eigene Fachdarstellung / Zitate (§ 51 UrhG) | Überarbeitet: Wartungsaufwand eigenständig dargestellt, Lizenzabschnitte präzisiert |
| `musik-und-theater.md` | **teilweise abgeglichen** | Spielstättenprogramme (Kulturzentrum Marstall) | Gemeinfreie Fakten (§ 2 UrhG) | Kurzübersicht lokaler Kulturstätten |
| `naherholungsgebiete.md` | **teilweise abgeglichen** | Parkanlagen und Forsten im Kreis Stormarn | Gemeinfreie Fakten (§ 2 UrhG) | Lage- und Wegebeschreibungen |
| `natur-freizeit.md` | **abgeglichen** | Schutzgebiete, Forste, Freizeit- und Sportstätten | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (361 Wörter):** Systematischer Überblick über Natur- und Sportangebote |
| `naturschutzgebiete.md` | **abgeglichen** | Landesverordnungen über NSGs (Höltigbaum etc.) | Amtliche Daten / Gemeingut (§ 5 UrhG) | Verordnungsdaten, sachliche Gebietsgrenzen |
| `neue-artikel-erstellen.md` | **abgeglichen** | Interne Redaktionsrichtlinien | Eigene Schöpfung (§ 2 UrhG) | Workflow-Anleitung für Mitwirkende |
| `openwiki/architecture.md` | **begründet ausgenommen** | Automatisch generierte Code-Dokumentation | Eigene Schöpfung / maschinell | Generiert durch OpenWiki-Aktion |
| `openwiki/overview.md` | **begründet ausgenommen** | Automatisch generierte Code-Dokumentation | Eigene Schöpfung / maschinell | Generiert durch OpenWiki-Aktion |
| `openwiki/source-map.md` | **begründet ausgenommen** | Automatisch generierte Dateikarte | Eigene Schöpfung / maschinell | Generiert durch OpenWiki-Aktion |
| `ortsname-ahrensburg.md` | **abgeglichen** | Wikipedia: *Ahrensburg* (Namen & Geschichte), etymologische Fachliteratur | CC BY-SA 4.0; Gemeinfreie Fakten (§ 2 UrhG) | Vollständige Wikipedia-Attribution vorhanden |
| `persoenlichkeiten.md` | **abgeglichen** | Wikipedia: *Ahrensburg*, *Waldemar Bonsels*, *Elise Bartels*, *Carl von Schimmelmann* u. a. | CC BY-SA 4.0 | Vollständige Einzellinks auf alle biografischen Vorlagen |
| `regelmaessige-feste-veranstaltungen.md` | **teilweise abgeglichen** | Städtischer Veranstaltungskalender | Gemeinfreie Fakten (§ 2 UrhG) | Termine und Namen von Festen |
| `restaurant.md` | **abgeglichen** | Öffentliche Verzeichnisse | Gemeinfreie Fakten (§ 2 UrhG) | Stichprobenartige Übersicht nach Küchenstil; keine Datenbankübernahme |
| `schloss-ahrensburg.md` | **abgeglichen** | Offizielle Website Stiftung Schloss Ahrensburg | Gemeinfreie Fakten (§ 2 UrhG) | Eigene historische Zusammenfassung, Weblink als Beleg |
| `schlosskirche-ahrensburg.md` | **abgeglichen** | Bau- und Stiftungsdaten (1594–1596), Ausstattungsfakten | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (461 Wörter):** Eigenständiger Bau-, Ausstattungs- und Gemeindebeschrieb |
| `sehenswuerdigkeiten-kultur.md` | **abgeglichen** | Kulturinstitutionen und Veranstaltungsformate | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (331 Wörter):** Vier Säulen des Kulturlebens in eigenständiger Sprache |
| `sehenswuerdigkeiten.md` | **abgeglichen** | Denkmaldaten Schloss, Kirche, Gottesbuden, Marstall, Rathaus | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (574 Wörter):** Denkmalporträts und Übersichtstabelle |
| `seniorentreff.md` | **abgeglichen** | Angebote Peter-Rantzau-Haus, Seniorenbeirat, AWO, DRK | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (492 Wörter):** Strukturierte Darstellung der Seniorenarbeit |
| `software-fuer-ein-grosses-wissensprojekt.md` | **abgeglichen** | Technische Analysen im Projekt | Eigene Fachdarstellung (§ 2 UrhG) | Eigenständige Synthese |
| `spielplaetze.md` | **abgeglichen** | Städtische Spielplatzstandorte, DIN EN 1176 | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (552 Wörter):** Quartiersgliederung, Sicherheitskonzept und Übersichtstabelle |
| `stadtverwaltung.md` | **abgeglichen** | Bürgerservice Stadt Ahrensburg | Amtliche Fakten (§ 5 UrhG) | Öffnungszeiten, Ämterzuschnitt |
| `stadtwappen.md` | **abgeglichen** | Kommunale Wappenrolle SH (Datenblatt 374), Hauptsatzung Ahrensburg (§ 1) | Amtliches Werk (§ 5 UrhG); Genehmigungsvorbehalt Hauptsatzung | Bereinigt: Amtliche Blasonierung präzisiert, Satzungsparagraph korrigiert |
| `stadtwerdung-1949.md` | **abgeglichen** | Historische Dokumente zur Verleihung 1949 | Gemeinfreie Fakten (§ 2 UrhG) | Eigenständiger Text zum 75-jährigen Stadtjubiläum |
| `uebernachtungsmoeglichkeiten-in-ahrensburg.md` | **abgeglichen** | Öffentliche Hotelverzeichnisse | Gemeinfreie Fakten (§ 2 UrhG) | Vier exemplarische Beherbergungsbetriebe; keine wesentliche Datenbankentnahme |
| `urheberrecht-pruefroutine-und-skills.md` | **abgeglichen** | Repository-Skills, UrhG, aktuelle Hersteller-Doku (Claude 5, Gemini 4, GPT-6) | Eigene Originalschöpfung (§ 2 UrhG) | **Neu erstellt (1568 Wörter):** Redaktionsleitfaden zu Prüfintervallen, Skills und Sprachmodellen |
| `urheberrecht-und-duplicate-content.md` | **abgeglichen** | Gesetzestexte (§§ 2, 5, 23, 51, 87a UrhG), CC BY-SA 4.0 Legal Code | Eigene Fachdarstellung / Gesetzeszitate (§ 5 UrhG) | Gründlich überarbeitet; unhaltbare Pauschalbehauptungen korrigiert |
| `vereinsleben.md` | **teilweise abgeglichen** | Vereinsregister / städtische Vereinsliste | Gemeinfreie Fakten (§ 2 UrhG) | Exemplarische Vereinsnennungen |
| `verkehrsanbindung.md` | **abgeglichen** | Liniennetz HVV/NAH.SH (RE 8/80, RB 81, U1, S4), Fernstraßen A 1 / B 75 | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (509 Wörter):** Vollständige, eigenständige Darstellung aller Verkehrsträger |
| `wander-und-radwege.md` | **teilweise abgeglichen** | Tourismusverband Stormarn, Wanderkarten | Gemeinfreie Geodaten / Fakten (§ 2 UrhG) | Eigenständige Streckenbeschreibungen |
| `webframeworks-im-vergleich.md` | **abgeglichen** | Offizielle Web-Dokumentationen (Next.js, Django, Rails etc.) | Eigene Fachdarstellung (§ 2 UrhG) | Eigenständige Architekturbewertung |
| `wichtige-unternehmen-arbeitgeber.md` | **abgeglichen** | Öffentliche Unternehmensangaben (Handelsregister, Websites) | Gemeinfreie Fakten (§ 2 UrhG) | Überarbeitet: Schlussabsatz eigenständig formuliert |
| `wikis-im-vergleich.md` | **abgeglichen** | MediaWiki, XWiki, DokuWiki, BookStack Dokumentation | Eigene Fachdarstellung (§ 2 UrhG) | Eigenständige Feature-Matrix |
| `wissen-speichern.md` | **abgeglichen** | Speicherarchitekturen (SQL, Git, Vektor) | Eigene Fachdarstellung (§ 2 UrhG) | Lizenzhinweis auf CC BY-SA 4.0 und Vorbehalte für Zitate präzisiert |
| `wissenssystem-selbst-bauen.md` | **abgeglichen** | Architekturleitfaden | Eigene Schöpfung (§ 2 UrhG) | Originalleitfaden |
| `wissenssysteme-im-vergleich.md` | **abgeglichen** | Marktübersicht Wissensmanagement | Eigene Fachdarstellung (§ 2 UrhG) | Eigenständige Systemanalyse |
| `wochenmarkt.md` | **abgeglichen** | Städtische Marktzeiten (Mi/Sa), Branchensortiment | Eigene Schöpfung / Gemeinfreie Fakten (§ 2 UrhG) | **Neu ausgebaut (382 Wörter):** Eigenständiges Kapitel zu Marktzeiten, regionalem Angebot und Anreise |

---

## 3. Einzelbefunde, Rechtsgrundlagen und erfolgte Abhilfen

Sämtliche im ersten Prüfdurchgang identifizierten Problemstellen wurden bereinigt und im zweiten Durchlauf verifiziert:

1. **Geologische Entstehungsgeschichte des Ahrensburger Tunneltals (`src/ahrensburger-tunneltal.md`):**
   - *Früherer Befund:* Verdacht auf strukturelle Paraphrase eines LANU-Faltblatts (§ 23 UrhG).
   - *Status:* **Erledigt.** Durch eigenständige Kurzdarstellung ersetzt; LANU-Faltblatt transparent verlinkt.
2. **Unbelegtes Werturteil zur Schimmelmann-Historie (`src/familie-schimmelmann.md`):**
   - *Früherer Befund:* Wörtliches Fremdzitat ohne Quellenangabe (§§ 51, 63 UrhG).
   - *Status:* **Erledigt.** Fremdes Werturteil gestrichen; sachliche Darstellung hergestellt.
3. **Politisches Wortzitat zur Schimmelmann-Debatte (`src/familie-schimmelmann.md`):**
   - *Früherer Befund:* Im Primärbeleg (Rechenschaftsbericht 2020) nicht im behaupteten Wortlaut nachweisbares Zitat.
   - *Status:* **Erledigt.** Behauptetes Wortzitat entfernt; politische Forderung sachlich mit Primärlink belegt.
4. **Lizenzbezeichnung externer Weblinks (`src/ahrensburger-tunneltal.md`):**
   - *Früherer Befund:* Überschrift „Amtliche und frei lizenzierte Quellen“ traf nicht auf alle Links zu.
   - *Status:* **Erledigt.** Umbenannt in „Quellen und Hintergrund“.
5. **Pauschalaussagen zu CC-Lizenzen und Schranken (`hauptseite.md`, `wissen-speichern.md`, `urheberrecht-und-duplicate-content.md`, `llm-wiki.md`):**
   - *Früherer Befund:* Verkürzte Aussagen („frei kopierbar“, „Share-Alike automatisch erfüllt“).
   - *Status:* **Erledigt.** Juristisch präzisiert nach CC BY-SA 4.0 Abschnitt 3 und §§ 2, 5, 23, 87b UrhG.
6. **Wappenrechtliche Angaben (`src/stadtwappen.md`):**
   - *Früherer Befund:* Falscher Satzungsparagraph (§ 2 statt § 1) und zu pauschale Freigabeaussage.
   - *Status:* **Erledigt.** Auf § 1 der Hauptsatzung und Datenblatt 374 der Kommunalen Wappenrolle korrigiert.
7. **Unbelegte Wartungsminuten (`src/llm-wiki.md`):**
   - *Früherer Befund:* Nicht zugeordnete Zeitangaben aus fremden Erfahrungsberichten.
   - *Status:* **Erledigt.** Durch eigenständige sachliche Beschreibung der Wartungsaufgaben ersetzt.

---

## 4. Ergebnis der Nachprüfung der 16 neuen bzw. ausgebauten Kapitel

Im zweiten Prüfdurchlauf wurden die 15 ausgebauten Kapitel (+6.895 Wörter) sowie das neu verfasste Kapitel `src/urheberrecht-pruefroutine-und-skills.md` (+1.568 Wörter) gezielt geprüft:

- **Schöpfungshöhe und hinreichender Abstand (§§ 2, 23 UrhG):** Alle 16 Dateien wurden ohne Rückgriff auf fremde Formulierungsvorlagen aus überprüften Sachfakten neu verfasst. Es liegen weder wörtliche Übernahmen noch enge Paraphrasen aus regionalen Presseerzeugnissen, dem Stormarn-Lexikon oder städtischen Broschüren vor.
- **Datenbankherstellerrecht (§§ 87a, 87b UrhG):** Die Übersichtstabellen (z. B. in `spielplaetze.md`, `die-stadtteile-im-portraet.md`, `sehenswuerdigkeiten.md`, `geschichte-der-stadt-ahrensburg.md`) sind eigene redaktionelle Zusammenstellungen von Kerndaten und stellen keine wesentliche Entnahme aus fremden Datenbanken dar.
- **Zitate und Musterblöcke (§ 51 UrhG):** Der in `src/urheberrecht-pruefroutine-und-skills.md` enthaltene Code-Block für `## Wikipedia als Quelle` ist ein eigenes Muster-Template des Projekts zur Einhaltung von CC BY-SA 4.0.
- **Duplicate-Content-Analyse:** Der automatische Prüflauf über alle 66 Dateien (`python3 scripts/find_duplicate_content.py src 0.35`) ergab im gesamten Fließtext der Orts- und Fachartikel **null Dubletten**. Lediglich der beabsichtigte Navigations-Hinweiskasten (`> Fachwörter wie *Open Source*...`) auf sechs Software-Vergleichsseiten tritt als gewolltes UI-Element mehrfach auf.
- **Transparenzhinweise (Art. 50 EU AI Act):** Alle 60 redaktionellen Inhaltsseiten sowie die 3 OpenWiki-Seiten tragen den geforderten KI-Transparenzhinweis; lediglich die 3 technischen/gesetzlichen Ausnahmen (`SUMMARY.md`, `impressum.md`, `datenschutz.md`) sind bestimmungsgemäß ohne KI-Hinweis.

---

## 5. Zusammenfassendes Fazit

- **Prüfstatus:** Vollständig abgeschlossen über alle **66 Dateien** unter `src/`.
- **Offene Rechtehindernisse:** 0.
- **Technischer Build-Status:** `mdbook build` läuft fehlerfrei durch; alle internen Querverweise in den redaktionellen Seiten sind valide.
- **Gesamtempfehlung:** **Redaktionell zur Veröffentlichung empfohlen.**
