# Verifikationsartefakte

Screenshots, die belegen, dass bestimmte Ausgaben auf der Live-Seite korrekt gerendert werden.
Nicht Teil des mdBook (`docs/` liegt außerhalb von `src/`).

## Mermaid-Diagramm in `openwiki/architecture.md`

- **Datum:** 2026-08-31
- **URL:** <https://wissen-ahrensburg.de/openwiki/architecture.html>
- **Methode:** Headless Chrome (`google-chrome --headless`), Warten auf `pre.mermaid svg`,
  Screenshot des `pre.mermaid`-Elements.
- **Ergebnis:** `mdbook-mermaid` (0.14.0) + `mermaid.min.js` rendern den `flowchart LR`-Block
  clientseitig als SVG. `<pre class="mermaid">` wird zu `<pre class="mermaid" data-processed>`
  mit `<svg class="flowchart">`.

| Datei | Inhalt |
|-------|--------|
| `mermaid-architecture.png` | Ausschnitt: das gerenderte Diagramm |
| `architecture-page-full.png` | Kontext: oberer Teil der Seite im mdBook-Layout |

## Co-Wiki-Seite (`src/co-wiki.md`)

- **Datum:** 2026-08-31
- **URL:** <https://wissen-ahrensburg.de/co-wiki.html>
- **Methode:** Headless Chrome (`google-chrome --headless --window-size=1280,3900
  --screenshot --virtual-time-budget=8000`).
- **Ergebnis:** Die Seite ist live. Transparenzhinweis steht oben und unten, alle Abschnitte
  (Der Chef / Der fleißige Assistent / Die Bibliothek / Arbeitsmodelle / Der typische Ablauf /
  Wie funktioniert das technisch? / Das Roboter-Team / Das Buch, das sich selbst aktualisiert)
  rendern korrekt, die relativen Links zu `openwiki/overview.md` / `architecture.md` sind auf
  `.html` umgeschrieben. In der Seitenleiste erscheint der Abschnitt „Wie dieses Wiki entsteht"
  mit dem markierten Eintrag „11. Co-Wiki: Mensch & KI".
- **Aktualisiert:** 2026-08-31 — Screenshot nach Ergänzung der Abschnitte „Das Roboter-Team
  (Multi-Agenten-Redaktion)" und „Das Buch, das sich selbst aktualisiert" neu aufgenommen
  (Fensterhöhe auf 3900 px erhöht).
- **Aktualisiert:** 2026-09-02 — neu aufgenommen (`--window-size=1280,3900`,
  `--virtual-time-budget=8000`). Anlass: neuer Link im Absatz „Der Ablauf" des Roboter-Team-
  Abschnitts auf die Seite „Neue Artikel aus Rohfassungen erstellen" (rendert korrekt als
  `.html`-Link) und die um 10 neue Einträge gewachsene Seitenleiste (u. a. „Neue Artikel"
  oben, „Der Ortsname", „Ahrensburg in der NS-Zeit", „Stadtwerdung 1949", „Persönlichkeiten",
  „Demografie", „Gewässer und Seen", „Naturschutzgebiete", „Fauna und Flora", „Bürgermeister
  und Stadtverordnetenversammlung"). Abschnittsstruktur der Seite selbst unverändert;
  Transparenzhinweis weiterhin oben und unten.
- **Aktualisiert:** 2026-09-02 — erneut aufgenommen. Anlass: der neue Einzellink „LLM Wiki"
  steht jetzt ganz oben in der Seitenleiste (unter „Startseite" / „Neue Artikel"). Die
  Co-Wiki-Seite selbst ist unverändert — alle acht Inhalts-Abschnitte rendern, Transparenz-
  hinweis oben und unten, Eintrag „11. Co-Wiki: Mensch & KI" in der Leiste markiert.
- **Aktualisiert:** 2026-09-03 — erneut aufgenommen. Anlass: die „…im Vergleich"-Familie ist
  komplett in den oberen Prefix-Block der Seitenleiste zusammengeführt (Wissenssysteme ·
  Wiki-Programme · CMS · Wie CMS mit Millionen Artikeln umgehen · Doku-Generatoren ·
  Webframeworks · Ein Wissenssystem selbst bauen), zwei davon neu aus der Redaktionspipeline.
  „Wie dieses Wiki entsteht" enthält jetzt nur noch „11. Co-Wiki: Mensch & KI" (markiert) und
  „12. Software für ein großes Wissensprojekt". Co-Wiki-Seite selbst unverändert — alle acht
  Inhalts-Abschnitte rendern, Transparenzhinweis oben und unten, relative Links auf `.html`.
- **Aktualisiert:** 2026-09-03 — erneut aufgenommen. Anlass: neue Seite „Wissen speichern"
  (aus der Redaktionspipeline) steht jetzt als vierter Eintrag im oberen Prefix-Block der
  Seitenleiste, direkt nach „LLM Wiki" und vor „Wissenssysteme im Vergleich". Methode:
  `mdbook serve` (lokal, Port 3000) + Headless Chrome (`--window-size=1280,4200
  --virtual-time-budget=8000 --screenshot`). Co-Wiki-Seite selbst unverändert — alle acht
  Inhalts-Abschnitte rendern, Transparenzhinweis oben und unten.
- **Aktualisiert:** 2026-09-03 — erneut aufgenommen. Anlass: **zwei** Änderungen. (1) Die
  Co-Wiki-Seite selbst hat jetzt am Ende einen Abschnitt „Verwandte Seiten" (vier Links, u. a.
  auf die neue Seite „Urheberrecht und Duplicate Content"). (2) Ebendiese neue Seite steht als
  fünfter Eintrag im oberen Prefix-Block der Seitenleiste, direkt nach „Wissen speichern".
  Methode: Headless Chrome gegen die Live-URL (`--window-size=1280,4600
  --virtual-time-budget=8000 --screenshot`). Die acht Inhalts-Abschnitte unverändert,
  Transparenzhinweis oben und unten, relative Links auf `.html`.

| Datei | Inhalt |
|-------|--------|
| `co-wiki-page-full.png` | Ganze Seite im mdBook-Layout inkl. Seitenleiste |
