#!/usr/bin/env python3
"""
Automatisierter Konventions- und Link-Linter für das Ahrensburg-Wiki (src/).
Prüft:
1.SUMMARY.md-Abgleich: Verwaiste src/*.md-Dateien oder tote Einträge in SUMMARY.md
2.EU-AI-Act-Transparenzhinweis am Anfang und Ende jeder Inhaltsseite (Ausnahme: datenschutz.md)
3.Interne Markdown-Links (Existenz der Zieldatei und ggf. Überschriften-Anker)
4.Stormarn-Lexikon-Links auf den Pflichtzusatz '© Kreisarchiv Stormarn'
5.Wikipedia-Quellenblöcke auf vollständige CC-BY-SA-4.0-Nennung
"""

import os
import re
import sys
from pathlib import Path

TRANSPARENCY_NOTICE = (
    "*Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher Intelligenz "
    "erstellt und redaktionell überprüft (Transparenzhinweis gemäß Art. 50 EU AI Act).*"
)
EXEMPT_TRANSPARENCY = {"SUMMARY.md", "datenschutz.md", "impressum.md"}


def slugify_heading(heading_text: str) -> str:
    """Näherung an mdBook-Anker-Generierung für deutsche Überschriften."""
    text = heading_text.strip().lower()
    # Entferne Markdown-Formatierung / Links in Überschriften
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text)
    # Ersetze alles außer Buchstaben (inkl. Umlaute/ß), Ziffern, Bindestrich und Leerzeichen
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def collect_headings(md_path: Path) -> set[str]:
    anchors = set()
    try:
        content = md_path.read_text(encoding="utf-8")
    except Exception:
        return anchors
    in_code_block = False
    for line in content.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        m = re.match(r"^#{1,6}\s+(.+)$", line.strip())
        if m:
            anchors.add(slugify_heading(m.group(1)))
    return anchors


def main() -> int:
    src_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("src")
    if not src_dir.is_dir():
        print(f"Fehler: Verzeichnis '{src_dir}' nicht gefunden.", file=sys.stderr)
        return 2

    summary_path = src_dir / "SUMMARY.md"
    issues: list[tuple[str, str, str, str]] = []  # (Schweregrad, Datei, Kategorie, Nachricht)

    # 1. Alle .md Dateien unter src/ erfassen
    all_md_files: set[Path] = set()
    for p in src_dir.rglob("*.md"):
        rel = p.relative_to(src_dir)
        all_md_files.add(rel)

    # 2. SUMMARY.md auswerten
    summary_Targets: set[Path] = set()
    if summary_path.is_file():
        summary_text = summary_path.read_text(encoding="utf-8")
        for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", summary_text):
            target = m.group(2).split("#")[0].strip()
            if target and not target.startswith(("http://", "https://", "mailto:")):
                target_path = Path(target)
                summary_Targets.add(target_path)
                if not (src_dir / target_path).is_file():
                    issues.append(
                        ("HOCH", "src/SUMMARY.md", "Toter SUMMARY-Link", f"Ziel existiert nicht: '{target}'")
                    )
    else:
        issues.append(("HOCH", "src/SUMMARY.md", "Fehlende Datei", "src/SUMMARY.md wurde nicht gefunden."))

    for rel_md in sorted(all_md_files):
        if rel_md.name == "SUMMARY.md":
            continue
        if rel_md not in summary_Targets:
            issues.append(
                ("HOCH", f"src/{rel_md}", "Verwaiste Seite", "Datei ist nicht in src/SUMMARY.md verlinkt.")
            )

    # 3. Vorab Überschriften-Anker aller Dateien sammeln
    file_anchors: dict[Path, set[str]] = {
        rel_md: collect_headings(src_dir / rel_md) for rel_md in all_md_files
    }

    # 4. Einzelprüfung jeder Inhaltsdatei
    link_pattern = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")

    for rel_md in sorted(all_md_files):
        if rel_md.name == "SUMMARY.md":
            continue
        full_path = src_dir / rel_md
        display_path = f"src/{rel_md}"
        text = full_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        non_empty = [ln.strip() for ln in lines if ln.strip()]

        # 4a. Transparenzhinweis-Prüfung
        if rel_md.name not in EXEMPT_TRANSPARENCY:
            has_top = any(TRANSPARENCY_NOTICE in ln for ln in non_empty[:5])
            has_bottom = any(TRANSPARENCY_NOTICE in ln for ln in non_empty[-3:])
            if not has_top:
                issues.append(
                    ("MITTEL", display_path, "Transparenzhinweis (oben)", "Pflichthinweis am Seitenanfang fehlt oder weicht ab.")
                )
            if not has_bottom:
                issues.append(
                    ("MITTEL", display_path, "Transparenzhinweis (unten)", "Pflichthinweis am Seitenende fehlt oder weicht ab.")
                )

        # 4b. Zeilenweise Prüfung (außerhalb von Codeblöcken)
        in_code_block = False
        for idx, line in enumerate(lines, start=1):
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            # Stormarn-Lexikon-Regel
            if "stormarnlexikon.de" in line.lower() or "stormarn-lexikon.de" in line.lower():
                context_window = "\n".join(lines[max(0, idx - 2): min(len(lines), idx + 2)])
                if "kreisarchiv stormarn" not in context_window.lower() and "alle rechte vorbehalten" not in context_window.lower():
                    issues.append(
                        ("MITTEL", f"{display_path}:{idx}", "Stormarn-Lexikon-Zusatz", "Link auf stormarnlexikon.de ohne '© Kreisarchiv Stormarn, alle Rechte vorbehalten'.")
                    )

            # Links und Bilder prüfen
            for m in link_pattern.finditer(line):
                is_image, label, raw_target = m.group(1), m.group(2), m.group(3).strip()
                target_url = raw_target.split()[0]  # optionalen Markdown-Titel abtrennen

                if is_image == "!":
                    issues.append(
                        ("MITTEL", f"{display_path}:{idx}", "Eingebettetes Bild", f"Bild-Einbettung '!['{label}']({target_url})' gefunden – Bildrechte & Lizenz gesondert prüfen.")
                    )
                    continue

                if target_url.startswith(("http://", "https://", "mailto:", "tel:")):
                    continue

                # Interner Link
                if target_url.startswith("#"):
                    anchor = target_url[1:]
                    if anchor and anchor not in file_anchors.get(rel_md, set()):
                        issues.append(
                            ("NIEDRIG", f"{display_path}:{idx}", "Interner Anker", f"Anker '#{anchor}' in derselben Datei nicht gefunden.")
                        )
                else:
                    parts = target_url.split("#", 1)
                    rel_target_str = parts[0]
                    anchor = parts[1] if len(parts) > 1 else ""
                    resolved = (full_path.parent / rel_target_str).resolve()
                    try:
                        resolved_rel = resolved.relative_to(src_dir.resolve())
                    except ValueError:
                        issues.append(
                            ("HOCH", f"{display_path}:{idx}", "Link außerhalb src/", f"Interner Link verweist aus src/ heraus: '{raw_target}'")
                        )
                        continue

                    if not resolved.is_file():
                        issues.append(
                            ("HOCH", f"{display_path}:{idx}", "Toter interner Link", f"Linkziel '{raw_target}' existiert nicht.")
                        )
                    elif anchor and anchor not in file_anchors.get(resolved_rel, set()):
                        issues.append(
                            ("NIEDRIG", f"{display_path}:{idx}", "Fehlender Ziel-Anker", f"Anker '#{anchor}' in Zieldatei 'src/{resolved_rel}' nicht gefunden.")
                        )

        # 4c. Wikipedia-Quellenblock prüfen
        if "## Wikipedia als Quelle" in text:
            wp_section = text.split("## Wikipedia als Quelle", 1)[1]
            if "CC BY-SA 4.0" not in wp_section:
                issues.append(
                    ("MITTEL", display_path, "Wikipedia-Attribution", "Abschnitt '## Wikipedia als Quelle' nennt 'CC BY-SA 4.0' nicht.")
                )
            if "de.wikipedia.org/wiki/" not in wp_section:
                issues.append(
                    ("MITTEL", display_path, "Wikipedia-Attribution", "Abschnitt '## Wikipedia als Quelle' enthält keinen direkten Artikel-Link auf de.wikipedia.org.")
                )

    # Ausgabe
    counts = {"HOCH": 0, "MITTEL": 0, "NIEDRIG": 0}
    for sev, _, _, _ in issues:
        counts[sev] = counts.get(sev, 0) + 1

    print(f"Geprüfte Markdown-Dateien unter {src_dir}/: {len(all_md_files)}")
    print(f"Befunde gesamt: {len(issues)} (HOCH: {counts['HOCH']} | MITTEL: {counts['MITTEL']} | NIEDRIG: {counts['NIEDRIG']})")
    if issues:
        print("\n| Schweregrad | Fundstelle | Kategorie | Details |")
        print("|---|---|---|---|")
        for sev, loc, cat, msg in issues:
            print(f"| {sev} | `{loc}` | {cat} | {msg} |")
    else:
        print("\nPASS: Alle geprüften Wiki-Konventionen und internen Links sind fehlerfrei.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
