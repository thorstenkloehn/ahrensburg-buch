---
name: dsgvo-und-persoenlichkeitsrecht
description: Überprüfe alle Inhalte dieses Stadt-Wikis unter src/ auf Datenschutz- (DSGVO) und Persönlichkeitsrechts-Risiken – personenbezogene Daten Lebender, private Kontaktdaten, Äußerungsrecht über lokale Betriebe/Vereine sowie rechtliche Pflichtangaben in Impressum und Datenschutzerklärung. Kompatibel mit Codex, Antigravity (agy) und Claude Code.
---

# DSGVO- & Persönlichkeitsrechts-Prüfung (Lokales Stadt-Wiki-Audit)

Diese Skill leitet Coding- und Redaktions-Agenten (Codex, Antigravity/agy, Claude Code) an, alle Seiten des Ahrensburg-Wikis (`src/**/*.md`) auf datenschutzrechtliche Risiken (DSGVO / BDSG) sowie Verletzungen des allgemeinen Persönlichkeitsrechts (APR, Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG) und des Unternehmenspersönlichkeitsrechts zu überprüfen.

> **Wichtiger Hinweis:** Diese Skill dient der redaktionellen Risikominimierung und Qualitätssicherung; sie ersetzt keine Rechtsberatung durch eine Rechtsanwältin oder einen Rechtsanwalt.

---

## 1. Warum ist diese Prüfung in einem Stadt-Wiki wichtig?

Anders als rein historische oder technische Lexika beschreibt ein lokales Stadt-Wiki reale, gegenwärtig in Ahrensburg lebende Menschen, aktive Vereine, Ärztinnen/Ärzte, Gastronomiebetriebe, Einzelhändler und lokale Unternehmen. Dabei gelten strenge Grenzen:

1. **Personenbezogene Daten lebender Personen (Art. 4 Nr. 1, Art. 6 Abs. 1 lit. f DSGVO):**
   - **Zulässig (in der Regel):** Nennung von Personen des öffentlichen Lebens, Amtsträgern in Ausübung ihres Amtes (z. B. Bürgermeister, Bürgervorsteher, historische Persönlichkeiten) oder geschäftsführenden Organen größerer Institutionen im sachlichen Kontext.
   - **Kritisch / Unzulässig ohne Einwilligung:** Private Wohnadressen, private Telefonnummern, private E-Mail-Adressen, Namen von nicht-öffentlichen Privatpersonen (z. B. Nachbarn, einfache Vereinsmitglieder, Minderjährige/Schülerinnen und Schüler).
2. **Lokale Gewerbebetriebe, Gastronomie, Praxen & Dienstleister (`src/einkaufen-in-ahrensburg.md`, `src/gastronomie-fuehrer.md`, `src/gesundheit.md` etc.):**
   - **Unternehmenspersönlichkeitsrecht & Kreditgefährdung (§ 823, § 824 BGB):** Keine unbelegten negativen Tatsachenbehauptungen, keine herabsetzenden Werturteile und keine geschäftsschädigenden Gerüchte.
   - **Wettbewerbsrecht / Schleichwerbung:** Sachlich-neutrale Darstellung; keine werblichen Superlative (*„das beste Restaurant der Stadt"*, *„führender Anbieter"*) für einzelne lokale Betriebe.
3. **Verstorbene Personen (Postmortales Persönlichkeitsrecht):**
   - Auch nach dem Tod (z. B. in `src/persoenlichkeiten.md` oder `src/ahrensburg-ns-zeit.md`) darf das Lebensbild nicht durch grobe Entstellungen oder unbelegte ehrverletzende Behauptungen verfälscht werden. Historisch gesicherte und quellenmäßig belegte Tatsachen sind hingegen durch die Wissenschafts- und Informationsfreiheit gedeckt.
4. **Pflichtseiten & Tracking-Freiheit (`src/datenschutz.md`, `src/impressum.md`):**
   - Stimmen die Angaben in `src/datenschutz.md` mit der tatsächlichen technischen Auslieferung (GitHub Pages, eingebundene externe Skripte/Schriften/Mermaid-Assets) überein?

---

## 2. Automatisierter Vorab-Scan (Token-schonend)

Der Agent führt zunächst gezielte Suchabfragen über `src/` aus, um relevante Fundstellen zu lokalisieren:

```bash
# 1. E-Mail-Adressen und Telefonnummern in src/ finden
git grep -inE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" src/
git grep -inE "(\+49|04102|Tel\.|Telefon)" src/

# 2. Straßenadressen mit Hausnummern prüfen (Privatadresse vs. öffentliche Einrichtung?)
git grep -inE "(straße|str\.|weg|allee|platz|damm|kamp|ring|chaussee)\s+[0-9]+" src/

# 3. Werbliche Superlative oder kritische Wertungen bei lokalen Betrieben finden
git grep -inE "(beste[rsn]?|führend|beliebteste|einzigartig|leider|mangelhaft|umstritten|skandal)" src/

# 4. Externe Ressourcen/CDNs in book.toml oder src/ prüfen (DSGVO-Relevanz für datenschutz.md)
git grep -inE "https?://" book.toml src/datenschutz.md src/impressum.md
```

---

## 3. Bewertungsmatrix

| Risikostufe | Kriterium | Empfohlene Maßnahme |
|---|---|---|
| 🔴 **HOCH** | Private Kontaktdaten (Adresse/Tel./Mail) lebender Privatpersonen; Nennung Minderjähriger; unbelegte ehrverletzende/geschäftsschädigende Aussagen; fehlende Drittanbieter-Nennung in `datenschutz.md`. | **Sofort entfernen** bzw. `datenschutz.md` ergänzen. |
| 🟡 **MITTEL** | Nennung von Einzelpersonen ohne klare öffentliche Funktion (z. B. einzelne Mitarbeitende, Ehrenamtliche ohne Vorstandsamt); stark werbliche Sprache für einzelne lokale Geschäfte/Lokale. | Auf Institution/Amt verallgemeinern (z. B. *„die Vereinsleitung"* statt Klarnamen) und werbliche Adjektive neutralisieren. |
| 🟢 **NIEDRIG** | Öffentliche Funktionsadressen (Rathaus, Schloss, Museen), historische Persönlichkeiten, neutral gehaltene Branchenübersichten. | Zulässig – keine Änderung nötig. |

---

## 4. Berichtsformat

```markdown
# Prüfbericht: DSGVO & Persönlichkeitsrecht

**Geprüfter Umfang:** `src/*.md` + `book.toml`
**Befunde:** 🔴 HOCH: [X] | 🟡 MITTEL: [Y] | 🟢 NIEDRIG / HINWEIS: [Z]

| Risikostufe | Fundstelle (`Datei:Zeile`) | Betroffene Person / Institution | Rechtlicher Aspekt (DSGVO / APR / UWG) | Konkrete Handlungsempfehlung |
|---|---|---|---|---|
| 🔴 / 🟡 / 🟢 | `src/datei.md:Zeile` | [Name / Betrieb / Ressource] | [z. B. Personenbezogenes Datum ohne Erforderlichkeit] | [z. B. Namen durch Funktionsbezeichnung ersetzen] |
```
