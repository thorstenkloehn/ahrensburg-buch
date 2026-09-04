# Neue Artikel aus Rohfassungen erstellen

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*

In einem [Co-Wiki](co-wiki.md) schreiben Mensch und künstliche Intelligenz (KI) Hand in Hand. Doch wie entsteht aus einer ersten Idee, ein paar hingeworfenen Stichpunkten oder einer Notiz eigentlich ein fertiger, geprüfter Artikel im Buch?

Der Schlüssel dazu ist die **Rohfassung** und die anschließende **Redaktionspipeline**. Diese Seite erklärt den gesamten Weg Schritt für Schritt – so einfach, dass ihn auch Einsteiger und jüngere Leser sofort verstehen.

---

## 1. Was ist eine Rohfassung? (Der rohe Tonklumpen)

Stell dir vor, du möchtest eine schöne Schale oder eine Tierfigur aus Ton töpfern. Am Anfang hast du nur einen feuchten, unförmigen **Tonklumpen**. Er ist noch nicht hübsch und man kann noch nicht daraus essen – aber er enthält bereits das gesamte Material, das du brauchst.

Genau das ist eine **Rohfassung**:
- Sie ist ein **vorläufiger Arbeitsentwurf**, kein fertiges Endprodukt.
- Sie sammelt Ideen, Notizen, Web-Links, Buchseiten und Gedanken an einem Ort.
- Sie lebt in einem speziellen Arbeitsordner namens `raw/` und ist **niemals direkt im Buch sichtbar**.

Erst wenn der Bildhauer (die KI) den Tonklumpen in Form gebracht hat und der Meister (der Mensch) prüft, ob alles stabil und richtig ist, wird daraus ein fertiges Werkstück für das Buch unter `src/`.

---

## 2. Der Bauplan einer Rohfassung (Die Vorlage)

Damit die KI und der Mensch reibungslos zusammenarbeiten können, gibt es für Rohfassungen eine feste Vorlage (`raw/_vorlage.md`). Jeder Abschnitt erfüllt einen wichtigen Zweck:

```markdown
# Rohfassung: Thema

> Status: **Rohfassung** — noch nicht für `src/` freigegeben.
> Zuständig (Mensch): <Name>
> Zielseite: `src/<slug>.md`

## Worum geht es?
<Ein, zwei Sätze: was soll der Artikel erklären, für wen?>

## Material / Notizen
- <Stichpunkt>
- <Stichpunkt>

## Quellen
- <URL oder Buch/Seite> — <was steht dort drin?>

## Offene Fragen
- <Was muss noch geklärt oder geprüft werden?>

## Rohtext
<Hier frei drauflosschreiben — Struktur egal, Hauptsache die Fakten stehen drin.>
```

### Warum ist jeder Baustein unverzichtbar?

1. **Status & Zuständigkeit:** Jeder weiß sofort: Dieser Text ist eine Baustelle. Und es steht fest, welcher Mensch am Ende die Verantwortung trägt.
2. **Zielseite (`src/<slug>.md`):** Legt von Anfang an fest, wie die Datei später heißen soll und wo sie im Buch hingehört.
3. **Worum geht es?:** Gibt der KI den Fokus vor (z. B. „Erklärung für Einsteiger“ oder „Historischer Überblick für Schüler“).
4. **Material & Notizen:** Die wichtigsten Stichpunkte und Kernaussagen auf einen Blick.
5. **Quellen (Belege):** Ohne echte Quellen darf kein Artikel entstehen! Hier stehen Links, Bücher oder Dokumente, aus denen das Wissen stammt.
6. **Offene Fragen:** Markiert Unklarheiten (z. B. „Stimmt diese Jahreszahl wirklich?“). So weiß die KI, worüber sie nicht spekulieren darf.
7. **Rohtext:** Hier darf unordentlich drauflosgeschrieben oder Material hineinkopiert werden.

---

## 3. Die Redaktionspipeline: Schritt für Schritt zum fertigen Artikel

Liegt eine Rohfassung im Ordner `raw/`, schickt der Mensch sie mit einem klaren Arbeitsauftrag (Prompt) in die **Redaktionspipeline** des Roboter-Teams:

> **Typische Prompts / Befehle:**
> - `Starte die Redaktionspipeline für <Thema>`
> - `Rohfassung <Thema> durch die Pipeline schicken`

Nun arbeiten die spezialisierten Subagenten Hand in Hand:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Briefing & Info-Mappe (Forscher sammelt Fakten & Quellen)│
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Bauplan & Gliederung (Architekt baut Überschriften-Gerüst)│
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Textentwurf (Schreiberling verfasst den Fließtext)       │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. Kritikschleife (Lektor & Faktenchecker prüfen streng)    │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. Verlinkung (Verlinker setzt Querverweise im Wiki)        │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. Finale Freigabe durch den Menschen (Human-in-the-Loop)   │
└─────────────────────────────────────────────────────────────┘
```

1. **Der Forscher (*Research Agent*):** Liest die Rohfassung, prüft die angegebenen Quellen und baut eine strukturierte Info-Mappe auf.
2. **Der Architekt (*Outline Agent*):** Entwirft die Gliederung (welche Überschriften gibt es und worum geht es in welchem Absatz?).
3. **Der Schreiberling (*Writer Agent*):** Verwandelt den Bauplan in verständlichen, lebendigen deutschen Fließtext.
4. **Die Kritikschleife (Lektor & Faktenchecker):**
   - Der **Lektor** feilt am Schreibstil, beseitigt Schachtelsätze und sorgt für guten Lesefluss.
   - Der **Faktenchecker** gleicht jeden einzelnen Satz mit den Quellen ab. Gibt es Unstimmigkeiten, muss der Schreiberling nachbessern (bis zu 2–3 Runden).
5. **Der Verlinker (*Linker Agent*):** Ergänzt Querverweise zu anderen Seiten im Wiki (z. B. zu verwandten Geschichts- oder Naturthemen).
6. **Menschliche Freigabe:** Der Mensch prüft das Gesamtergebnis. Erst mit seiner Freigabe wandert der Text nach `src/<slug>.md` und in das Inhaltsverzeichnis `src/SUMMARY.md`.

---

## 4. Warum dieser Aufwand? Risiken & Qualitätsprüfung

Man könnte sich fragen: *Warum lassen wir die KI nicht einfach mit einem kurzen Satz einen ganzen Artikel schreiben?*

Die Antwort liegt in der Funktionsweise moderner Sprachmodelle (LLMs):

### Das Problem der „Halluzinationen“
Ein Sprachmodell denkt nicht wie ein Mensch. Es rechnet mathematisch aus, welches Wort statistisch am besten auf das vorherige folgt (*Next-Token-Prediction*). Wenn dem Modell ein echtes Faktum fehlt, denkt es nicht nach und sagt nicht „Ich weiß es nicht“, sondern erfindet mitunter täuschend echt klingende Jahreszahlen, historische Ereignisse oder Personen.

### Strikte Belegpflicht & Nachprüfbarkeit
In einem verlässlichen Nachschlagewerk darf kein erfundenes Wissen stehen. Deshalb gilt im Co-Wiki eine **strikte Belegpflicht**: Jede Kernaussage in der Rohfassung muss auf echten Primärquellen beruhen. Der Faktenchecker-Agent und der Mensch prüfen unnachgiebig, ob die Quellen die Behauptungen auch wirklich stützen.

### Der Mensch als Chef (Human-in-the-Loop)
Die KI ist eine unheimlich schnelle Schreibmaschine und ein kluger Sortierhelfer – aber sie trägt keine Verantwortung. Nur ein Mensch kann mit gesundem Menschenverstand beurteilen, ob ein Text fair, wahrheitsgetreu und angemessen formuliert ist. Deshalb veröffentlicht die KI niemals selbstständig eine Seite.

---

## 5. Die Gefahr des Modell-Kollapses (Model Collapse)

Ein weiterer, noch tieferer Grund für echte menschliche Recherche ist der sogenannte **Modell-Kollaps**:

Wenn immer mehr Texte im Internet ausschließlich von KI generiert werden, passiert etwas Gefährliches: Zukünftige KI-Modelle werden mit Texten trainiert, die vorherige KIs geschrieben haben. Man nennt das auch **„Modell-Inzucht“**.

- **Informationsverlust:** Seltene Fakten, lokale Besonderheiten und feine sprachliche Nuancen gehen verloren.
- **Fehlerverstärkung:** Kleine Ungenauigkeiten schaukeln sich von Generation zu Generation weiter auf.
- **Verflachung:** Alle Texte klingen irgendwann gleich förmlich und inhaltsleer.

> **Der unersetzliche Wert des Menschen:**  
> Nur echte Menschen, die selbst vor Ort recherchieren, Archive durchstöbern, Zeitzeugen befragen oder Bücher lesen, bringen **neues, unverfälschtes Weltwissen** in den Datenpool. Ohne menschliche Originalarbeit verkümmert das Wissen im digitalen Raum.

---

## 6. Lebenszyklus & Aufräumen: Vom Entwurf ins Buch

Wie sieht der Lebenslauf einer Rohfassung in diesem Projekt konkret aus?

1. **Lokal vorschreiben:** Ein Mensch legt `raw/<thema>.md` an (basierend auf `raw/_vorlage.md`). Da `raw/` in `.gitignore` eingetragen ist, bleibt der Entwurf privat auf dem Rechner.
2. **Pipeline starten:** Mensch gibt den Auftrag an die Redaktionspipeline.
3. **Freigabe & Veröffentlichung:** Sobald der Artikel fertig und geprüft ist, wird er unter `src/<slug>.md` gespeichert und in [SUMMARY.md](SUMMARY.md) eingetragen.
4. **Transparenzhinweis:** Jede Seite in `src/` erhält oben und unten den vorgeschriebenen Transparenzhinweis gemäß Art. 50 EU AI Act.
5. **Rohfassung löschen:** Da alle wertvollen Inhalte, Quellen und Fakten nun sauber strukturiert im versionierten Wiki (`src/`) gesichert sind, wird die temporäre Datei in `raw/` gelöscht. So bleibt der Arbeitsbereich stets aufgeräumt.

---

## Verwandte Seiten

- [Co-Wiki: Mensch & KI](co-wiki.md) – Das grundlegende Kooperationsmodell dieses Wikis.
- [Urheberrecht und Duplicate Content](urheberrecht-und-duplicate-content.md) – Wie das Wiki Urheberrechte prüft (zentrale Aufgabe des Faktencheckers in der Pipeline).
- [Wissen speichern](wissen-speichern.md) – Was einen guten Wissensartikel ausmacht und wie große Wissensmengen abgelegt, durchsucht und weitergegeben werden.
- [Software für ein großes Wissensprojekt](software-fuer-ein-grosses-wissensprojekt.md) – Wie das Wiki technisch aufgebaut ist.
- [Doku-Generatoren im Vergleich](doku-generatoren-im-vergleich.md) – Warum mdBook für dieses Wissensprojekt genutzt wird.
- [Überblick](openwiki/overview.md) – Technische Übersicht über das Repository.

---

*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*
