---
name: deploy-und-sync
description: Führe den vollständigen Pre-/Post-Deploy- und Synchronisations-Workflow dieses Repositories aus – .claude/.agents-Mirror-Sync, OpenWiki-Drift-Check, mdbook build, CNAME-only-Diff-Check gegen origin/gh-pages sowie Live-Verifikation. Kompatibel mit Codex, Antigravity (agy) und Claude Code.
---

# Deploy & Sync (Release- und Verifikations-Workflow)

Diese Skill bündelt das gesamte operative Runbook aus [`docs/deploy-verification.md`](../../../docs/deploy-verification.md) und [`docs/agent-notes.md`](../../../docs/agent-notes.md) in einer standardisierten Prüf- und Release-Routine für Coding-Agenten (Codex, Antigravity/agy, Claude Code).

---

## 1. Wann wird diese Skill aufgerufen?

- **Vor einem Commit / Push (`Pre-Commit / Pre-Deploy`):** Sicherstellen, dass `.agents/` synchron ist, `src/openwiki/` keinen Drift aufweist, alle Wiki-Konventionen eingehalten werden und `mdbook build` fehlerfrei durchläuft.
- **Beim Veröffentlichen (`Deploy`):** Nach ausdrücklicher menschlicher Freigabe (`Human-in-the-Loop`) den Build nach `gh-pages` publizieren.
- **Nach einem Deploy (`Post-Deploy-Verifikation`):** Mittels CNAME-only-Diff-Check und HTTP-Statusprüfung verifizieren, dass `https://wissen-ahrensburg.de` exakt dem aktuellen `main`-Stand entspricht.

---

## 2. Schritt-für-Schritt-Workflow

### Schritt 1: `.claude/` → `.agents/` Mirror synchronisieren & prüfen

`.claude/` ist die **Single Source of Truth** für Agenten (`agents/`) und Skills (`skills/`). `.agents/` ist die byte-identische Kopie für Agent-Runner (die Root-`AGENTS.md` wird **nicht** nach `.agents/` kopiert).

```bash
mkdir -p .agents
rsync -a --delete .claude/agents/ .agents/agents/
rsync -a --delete .claude/skills/ .agents/skills/

# Verifikation (muss komplett leer bleiben = PASS)
diff -rq .claude/agents .agents/agents
diff -rq .claude/skills .agents/skills
```

### Schritt 2: OpenWiki-Kopien auf Drift prüfen (`openwiki/` ↔ `src/openwiki/`)

Die Dateien unter `src/openwiki/*.md` sind manuelle Kopien der generierten `openwiki/*.md`-Seiten (mit EU-AI-Act-Transparenzhinweis statt YAML-Frontmatter und angepassten relativen Links).

```bash
for f in overview.md architecture.md source-map.md; do
  echo "=== $f ==="
  diff -u "openwiki/$f" "src/openwiki/$f" | head -n 30
done
```

- **Erwarteter Unterschied:** Nur der Frontmatter↔Transparenzhinweis-Tausch am Anfang, ggf. Pfadanpassungen und der Transparenzhinweis am Ende.
- **Bei inhaltlichem Drift:** Änderungen aus `openwiki/<f>` unter Beibehaltung des oberen/unteren Transparenzhinweises nach `src/openwiki/<f>` übernehmen.

### Schritt 3: Konventions-Linter & `mdbook build`

Vor jedem Release müssen der technische Linter und der Buch-Build fehlerfrei durchlaufen:

```bash
python3 scripts/check_wiki_conventions.py src
export PATH="$HOME/.cargo/bin:$PATH"
mdbook build
```

Falls `gh-pages` noch nicht lokal unter `node_modules/.bin/gh-pages` installiert ist:
```bash
npm install
```

### Schritt 4: Deploy ausführen (NUR nach menschlicher Freigabe!)

> **WICHTIG:** Ein Agent führt `npm run ver` oder `git push` nur aus, wenn der Mensch dies für den aktuellen Stand freigegeben hat.

```bash
export PATH="$HOME/.cargo/bin:$PATH"
mdbook build
npm run ver
```

*Hinweis:* `npm run ver` gibt immer `Published` aus. Ein neuer Commit auf `gh-pages` entsteht nur, wenn sich Dateien unter `book/` (also `src/` oder `book.toml`) tatsächlich geändert haben. Reine Meta-Commits (`docs/`, `.claude/`, `.agents/`, `README.md`, `AGENTS.md`, `CLAUDE.md`) verändern `book/` nicht.

### Schritt 5: CNAME-only-Diff-Check (`book/` vs. `origin/gh-pages`)

Prüft deterministisch, ob der veröffentlichte `gh-pages`-Branch 1:1 dem lokalen frischen Build entspricht:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
git fetch origin -q && rm -rf book && mdbook build
tmp=$(mktemp -d)
git archive origin/gh-pages | tar -x -C "$tmp"
diff -rq book "$tmp" | grep -vE '\.git|/CNAME|\.nojekyll' || true
rm -rf "$tmp"
```

- **PASS:** Keine Ausgabe (oder ausschließlich `Nur in <tmp>: CNAME.`).
- **STALE:** Jede andere Abweichung zeigt an, dass `gh-pages` noch nicht auf dem Stand von `src/` ist.

### Schritt 6: Live-Verifikation (HTTP 200 & Stichprobe)

Nach einem Inhalts-Deploy die geänderten Seiten live prüfen:

```bash
curl -sI https://wissen-ahrensburg.de/ | head -n 10
```

---

## 3. Berichtsformat

Der Agent fasst den Durchlauf kompakt zusammen:

```markdown
# Statusbericht: Deploy & Sync

| Prüfpunkt | Status | Details |
|---|---|---|
| **1. `.agents/`-Mirror-Sync** | PASS / FIXED | `diff -rq` zwischen `.claude/` und `.agents/` leer |
| **2. OpenWiki-Sync (`src/openwiki/`)** | PASS / SYNCED | `overview`, `architecture`, `source-map` abgeglichen |
| **3. Konventions-Linter (`src/`)** | PASS / WARN | Ergebnis von `scripts/check_wiki_conventions.py` |
| **4. `mdbook build`** | PASS / FAIL | Build nach `book/` |
| **5. CNAME-only-Diff (`gh-pages`)** | PASS / STALE | Vergleich `book/` gegen `origin/gh-pages` |
| **6. Live-Check** | PASS / SKIPPED | HTTP-Status & Commit-Hash (`main` / `gh-pages`) |
```
