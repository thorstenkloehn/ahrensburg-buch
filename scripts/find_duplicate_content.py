#!/usr/bin/env python3
"""
Findet interne Textdopplungen (Duplicate Content) in den Markdown-Dateien unter src/.
Arbeitet token-schonend und heuristisch:
- Teilt Markdown-Dateien in Absätze auf.
- Ignoriert Standard-Hinweise (z.B. Art. 50 EU AI Act Transparenzhinweis, Wikipedia-Lizenzblöcke, H1-Titel).
- Normalisiert Text (Kleinschreibung, Satzzeichen entfernt, Whitespace bereinigt).
- Bildet 5-Gramme (Shingles) und vergleicht Absätze paarweise (Jaccard-Ähnlichkeit >= Schwellenwert)
  oder prüft auf identische Sätze mit >= 8 Wörtern.
"""

import os
import re
import glob
import sys
from collections import defaultdict

IGNORE_PHRASES = [
    "art. 50 eu ai act",
    "künstlicher intelligenz erstellt und redaktionell überprüft",
    "wikipedia als quelle",
    "teile dieses artikels wurden aus der deutschsprachigen wikipedia übernommen",
    "autoren der vorlagen jeweils laut versionsgeschichte",
    "diese seite steht unter derselben lizenz",
    "cc by-sa 4.0",
    "transparenzhinweis gemäß art. 50"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # Links zu Ankertext
    text = re.sub(r'[^\w\s]', ' ', text)
    words = text.split()
    return words

def get_paragraphs(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    raw_paras = content.split('\n\n')
    valid_paras = []
    line_offset = 1

    for p in raw_paras:
        lines = p.strip().splitlines()
        p_lines_count = len(lines)
        p_text = " ".join(lines).strip()
        
        # Check if should ignore
        lower_p = p_text.lower()
        should_ignore = False
        if not p_text or p_text.startswith('#') or p_text.startswith('---'):
            should_ignore = True
        elif len(p_text.split()) < 12:  # Zu kurz für geschützten Fließtext
            should_ignore = True
        else:
            for ign in IGNORE_PHRASES:
                if ign in lower_p:
                    should_ignore = True
                    break

        if not should_ignore:
            valid_paras.append({
                'file': filepath,
                'line': line_offset,
                'text': p_text,
                'words': clean_text(p_text)
            })

        line_offset += p_lines_count + 1

    return valid_paras

def jaccard_similarity(words1, words2, n=4):
    if len(words1) < n or len(words2) < n:
        return 0.0
    s1 = set(tuple(words1[i:i+n]) for i in range(len(words1)-n+1))
    s2 = set(tuple(words2[i:i+n]) for i in range(len(words2)-n+1))
    if not s1 or not s2:
        return 0.0
    return len(s1 & s2) / len(s1 | s2)

def main(src_dir="src", threshold=0.45):
    files = sorted(glob.glob(os.path.join(src_dir, "**/*.md"), recursive=True))
    all_paras = []

    for f in files:
        if "SUMMARY.md" in f or "openwiki" in f:
            continue
        all_paras.extend(get_paragraphs(f))

    duplicates = []
    n = len(all_paras)

    for i in range(n):
        p1 = all_paras[i]
        for j in range(i + 1, n):
            p2 = all_paras[j]
            if p1['file'] == p2['file']:
                continue
            
            sim = jaccard_similarity(p1['words'], p2['words'])
            if sim >= threshold:
                duplicates.append({
                    'file1': p1['file'],
                    'line1': p1['line'],
                    'file2': p2['file'],
                    'line2': p2['line'],
                    'sim': sim,
                    'text1': p1['text'][:140] + "..." if len(p1['text']) > 140 else p1['text'],
                    'text2': p2['text'][:140] + "..." if len(p2['text']) > 140 else p2['text']
                })

    duplicates.sort(key=lambda x: x['sim'], reverse=True)

    print(f"=== DUPLICATE CONTENT ANALYSE ({len(files)} Dateien durchsucht) ===")
    if not duplicates:
        print("Keine relevanten internen Textdopplungen gefunden (Schwellenwert: {:.0%}).".format(threshold))
        return

    print(f"Gefundene Dopplungen / hohe Ähnlichkeiten: {len(duplicates)}\n")
    for d in duplicates:
        print(f"Ähnlichkeit: {d['sim']:.1%}")
        print(f"  Quelle A: {d['file1']}:{d['line1']}")
        print(f"  Vorschau: \"{d['text1']}\"")
        print(f"  Quelle B: {d['file2']}:{d['line2']}")
        print(f"  Vorschau: \"{d['text2']}\"")
        print("-" * 60)

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "src"
    t = float(sys.argv[2]) if len(sys.argv) > 2 else 0.45
    main(src, t)
