#!/usr/bin/env python3
"""Convert BORI ITRANS (.itx) parvan files to Devanagari plain text.

Line for line: output line N is input line N. Header comments (%), TeX
commands (\\...) and the English footer are copied unchanged; every other
line is transliterated. Nothing is added, dropped or corrected.
Usage: itx_to_devanagari.py RAW_DIR OUT_DIR
"""
import re, sys, unicodedata
from pathlib import Path
from indic_transliteration import sanscript as S

KEEP = re.compile(r"^(%|\\|##|Mahabharata Critical Edition|Encoding:|Electronic text|Pune, India|http|for further details)")

def convert_line(line):
    if KEEP.match(line.strip()) or not line.strip():
        return line, False
    text = line.replace(".h", "")          # word-final halant is implied
    out = S.transliterate(text, S.ITRANS, S.DEVANAGARI)
    return unicodedata.normalize("NFC", out), True

def main(raw, out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    for src in sorted(Path(raw).glob("mbh??.itx")):
        lines = src.read_text(encoding="utf8").split("\n")
        res, bad, conv = [], [], 0
        for n, line in enumerate(lines, 1):
            new, did = convert_line(line)
            res.append(new)
            if did:
                conv += 1
                if re.search(r"[A-Za-z]", new):
                    bad.append((n, line, new))
        (out / (src.stem + ".txt")).write_text("\n".join(res), encoding="utf8")
        print(f"{src.name}: {len(lines)} lines, {conv} converted, {len(bad)} with Latin letters left")
        for n, a, b in bad[:3]:
            print("   line", n, "|", a, "|", b)

main(sys.argv[1], sys.argv[2])
