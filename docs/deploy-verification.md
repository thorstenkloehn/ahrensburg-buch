---
type: Runbook
title: Deploy & Verifikation
description: Deploy-Ablauf für die mdBook-Seite und der CNAME-only-Diff-Check, mit dem geprüft wird, ob die Live-Seite dem aktuellen main entspricht.
tags:
  - deploy
  - verification
  - gh-pages
  - runbook
audience: Betreiber / coding agents
---

# Deploy & Verifikation

Ablauf zum Veröffentlichen der Ahrensburg-Wissensdatenbank
(`npm run ver` → Branch `gh-pages` → <https://wissen-ahrensburg.de>) und zur Kontrolle,
dass die Live-Seite wirklich dem aktuellen Stand entspricht. `docs/` liegt außerhalb von
`src/` und ist nicht Teil des mdBook.

## Deploy-Ablauf

```
npm install     # gh-pages-Binary ist eine gitignorierte devDependency, auf frischem Checkout nicht da
mdbook build    # rendert src/ nach book/ (gitignored)
npm run ver     # gh-pages -d book --nojekyll --cname wissen-ahrensburg.de
```

Der Deploy ist manuell — es gibt keinen CI-Workflow in diesem Repo.

## Wichtig: „Published" heißt nicht „geändert"

`npm run ver` gibt **immer** `Published` aus, auch wenn sich nichts geändert hat. Das
`gh-pages`-Tool legt nur dann einen neuen `gh-pages`-Commit an, wenn sich der `book/`-Output
tatsächlich unterscheidet.

Commits, die **nur Meta-Dokumente** anfassen (`CLAUDE.md`, `AGENTS.md`, `README.md`,
`docs/**`, `.claude/**`, `raw/**`) oder die generierten `openwiki/`-Originale, ändern `book/`
nicht. Folge:

- `gh-pages` bleibt auf demselben Commit stehen.
- Der GitHub-Pages-Header `last-modified` bewegt sich nicht.

Das ist **korrektes Verhalten**, kein fehlgeschlagener Deploy. `last-modified` wandert erst,
wenn sich eine Seite unter `src/` ändert.

## Der CNAME-only-Diff-Check

Prüft, ob die veröffentlichte Seite byte-identisch mit einem frischen Build des aktuellen
`main` ist:

```
git fetch origin -q && rm -rf book && mdbook build
tmp=$(mktemp -d); git archive origin/gh-pages | tar -x -C "$tmp"
diff -rq book "$tmp" | grep -vE '\.git|/CNAME|\.nojekyll'
rm -rf "$tmp"
```

### Ergebnis deuten

- **PASS** — die gefilterte Ausgabe ist ausschließlich `Nur in <tmp>: CNAME.`
  Die deployte Seite entspricht 1:1 dem Build vom aktuellen `main`.
- **STALE** — irgendeine andere Datei taucht auf (`Dateien … sind verschieden` oder
  `Nur in book:` / `Nur in <tmp>:` für einen Nicht-CNAME-Pfad). Dann `mdbook build` +
  `npm run ver` erneut ausführen und neu prüfen.

### Erwartete Nicht-Inhalts-Unterschiede (vom Filter abgedeckt)

| Datei | Warum unterschiedlich |
|-------|-----------------------|
| `CNAME` | Nur im deployten Baum. `npm run ver` fügt sie über `--cname` ein; sie liegt nicht in `book/`. |
| `.gitignore` | Vom `gh-pages`-Tool angelegt; matcht das `\.git`-Muster. |
| `.nojekyll` | In beiden Bäumen vorhanden, aber unterschiedliche Bytes (`gh-pages --nojekyll` schreibt eine eigene Variante statt der von `mdbook`). Inhaltlich bedeutungslos. |

## Handgepflegte Kopien, die zusammen aktualisiert werden müssen

Manche Inhalte liegen bewusst mehrfach im Repo und werden **nicht** aus einer Quelle generiert.
Wer eine davon ändert, muss die anderen nachziehen:

| Thema | Stellen |
|-------|---------|
| **Co-Wiki** (Rollen, Arbeitsmodelle, Ablauf, Technik, fortgeschrittene Muster) | `CLAUDE.md` (Abschnitt „Zusammenarbeit Mensch & KI (Co-Wiki)") und `AGENTS.md` (Abschnitt „Die drei Betriebsmuster") — beide nur Kurzfassung mit Verweis auf die Skill; `.claude/skills/co-wiki/` (`SKILL.md` + `references/`, Volltext), `.claude/agents/` (`redaktion-*`), `src/co-wiki.md` (öffentliche Seite, live unter `/co-wiki.html`). Details und Umfang je Stelle: [`agent-notes.md`](agent-notes.md) §3. |
| **OpenWiki-Seiten** | `openwiki/*.md` (generiert) → `src/openwiki/*.md` (manuelle Kopien für `SUMMARY.md`). Drift-Check: `diff src/openwiki/<f> openwiki/<f>` — erwartet ist nur der Frontmatter↔Transparenzhinweis-Tausch oben und der Hinweis am Ende. |
| **`.agents/`-Mirror** | `.claude/agents/` + `.claude/skills/` → `.agents/` (byte-identische Kopie für Runner, die `.agents/` erwarten; **im Repo eingecheckt**, Root-`AGENTS.md` wird nicht gespiegelt). `.claude/` ist die Quelle. Sync + Drift-Check: [`agent-notes.md`](agent-notes.md) §6. |

## Weitere nützliche Kommandos

- `gh api repos/{owner}/{repo}/pages/builds/latest` — Status des letzten GitHub-Pages-Builds
  (`status`, `commit`, `updated_at`).
- `git log -1 -- src/` — letzter echter Inhalts-Commit. Meta-Doc-Commits danach beeinflussen
  den Build nicht.
- `curl -sI https://wissen-ahrensburg.de | grep -i last-modified` — Zeitstempel der
  aktuell ausgelieferten CDN-Kopie.

## Related pages

- [`agent-notes.md`](agent-notes.md) — gesammeltes Betriebswissen (Deploy, OpenWiki-Kopien, Co-Wiki-Kopien).
- [`../CLAUDE.md`](../CLAUDE.md) — Build-/Deploy-Kommandos und Inhaltskonventionen.
- [`../AGENTS.md`](../AGENTS.md) — Umgang mit dem generierten `openwiki/`-Evidenzindex.
- [`verification/README.md`](verification/README.md) — Render-Verifikationsscreenshots.
