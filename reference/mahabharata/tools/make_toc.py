#!/usr/bin/env python3
"""Write toc.md for the Mahabharata folder from text/ and titles.json.  usage: make_toc.py BOOK_DIR"""
import json, re, sys
from pathlib import Path
from collections import OrderedDict
book = Path(sys.argv[1])
PARTS = ["Adiparva", "Sabhaparva", "Aranyakaparva (Vanaparva)", "Viratparva", "Udyogaparva", "Bhishmaparva",
         "Dronaparva", "Karnaparva", "Shalyaparva", "Sauptikaparva", "Striparva", "Shantiparva",
         "Anushasanaparva", "Ashvamedhikaparva", "Ashramavasikaparva", "Mausalaparva",
         "Mahaprasthanikaparva", "Svargarohanaparva"]
SKT = ["आदिपर्व", "सभापर्व", "आरण्यकपर्व", "विराटपर्व", "उद्योगपर्व", "भीष्मपर्व", "द्रोणपर्व", "कर्णपर्व",
       "शल्यपर्व", "सौप्तिकपर्व", "स्त्रीपर्व", "शान्तिपर्व", "अनुशासनपर्व", "आश्वमेधिकपर्व",
       "आश्रमवासिकपर्व", "मौसलपर्व", "महाप्रस्थानिकपर्व", "स्वर्गारोहणपर्व"]
partial = {("003", "241")}      # file ends mid-chapter (ISSUES I1)
titles = json.load(open(book / "titles.json", encoding="utf8"))
chap = OrderedDict()
for f in sorted((book / "text").glob("*.md")):
    if "-" in f.stem: continue
    for line in f.read_text(encoding="utf8").splitlines():
        i = line.split(" | ")[0]
        p, c, v = i.split(".")
        chap.setdefault((p, c), (f.name, set()))
        chap[(p, c)][1].add(re.sub(r"[a-z]+$", "", v))
tv = sum(len(x[1]) for x in chap.values())
out = ["# Mahabharata (महाभारत)", "",
 "- Author / compiler: Vyasa (Krishna Dvaipayana), tradition: itihasa; Vaishampayana to Janamejaya, as told by Ugrashravas Sauti (text itself)",
 "- Subject and purpose of the book: the story of the Kuru family and the Bharata war with teaching on dharma, politics and liberation (summary, not from this file's own words)",
 "- Base edition: Critical Edition, V. S. Sukthankar and others, BORI Pune 1933-1966; electronic text by M. Tokunaga, J. D. Smith (source S1 in sources.md)",
 "- Mapping: part = parvan (1 to 18), chapter = adhyaya of the critical edition, verse = the edition's verse number (lines of one verse get a, b, c)",
 f"- Totals: 18 parts, {len(chap)} chapters, {tv} verses extracted (the critical edition has about 1995 chapters and 73,000 verses; parvan 3 is incomplete, see ISSUES.md I1)",
 ""]
by = OrderedDict()
for (p, c), v in chap.items(): by.setdefault(p, []).append((c, v))
for p, rows in by.items():
    n = int(p)
    out += [f"## Part {p}: {SKT[n-1]} ({PARTS[n-1]})", "",
            "Purpose: parvan of the Mahabharata (source: tradition)", "",
            "| Part | Chapter | Sanskrit name | English name | Purpose | Verses (extracted) | Verses (traditional) | File | Status |",
            "|---|---|---|---|---|---|---|---|---|"]
    for c, (fn, vs) in rows:
        t = " ".join(titles.get(p, {}).get(c, [])) or "-"
        t = t.replace("|", "/")
        st = "partial" if (p, c) in partial else "extracted"
        out.append(f"| {p} | {c} | {t} | | | {len(vs)} | | text/{fn} | {st} |")
    out.append("")
(book / "toc.md").write_text("\n".join(out), encoding="utf8")
print(len(chap), "chapters", tv, "verses")
