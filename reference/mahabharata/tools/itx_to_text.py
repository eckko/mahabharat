#!/usr/bin/env python3
"""Mahabharata (BORI CE, Sanskrit Documents ITRANS) -> FORMAT.md text files.

    python3 itx_to_text.py RAW_DIR BOOK_DIR

Reads RAW_DIR/mbh01.itx ... mbh18.itx and writes into BOOK_DIR:
  text/chPPP.CCC.md  or  text/pPPP.md   ("ID | Devanagari" lines)
  titles.json        chapter titles as printed (Devanagari), per part and chapter
  parse_report.json  counts and every oddity (repeats, skips, orphan lines)

Nothing is corrected. Rules (see FORMAT.md):
  * indented non-empty lines are headings (titles, then the chapter number)
  * a line that ends "| N |" (prose numbered) is a verse too, marker "|"
  * a line that ends "|| N||" closes a verse numbered N; a verse's lines are
    the lines since the previous closing line; the marker becomes "||"
  * a verse of more than 26 lines is stored as prose lines P1.. (logged in parse_report.json)
  * the same number twice in a row means one verse with more lines
  * "xyz uvAcha||" (a line closed by || without a number) is prose Pk
  * a trailing "\\-" (TeX hyphen) joins the next line
  * parts under 1000 lines go in one pPPP.md file, others one file per chapter
"""
import json, re, sys, unicodedata
from pathlib import Path
from indic_transliteration import sanscript as S

NUM_END = re.compile(r"\|\|\s*(\d+)\s*\|\|\s*$")
PLAIN_END = re.compile(r"\|\|\s*$")
SINGLE_END = re.compile(r"(?<!\|)\|\s*(\d+)\s*\|\s*$")   # prose verse: "... | 001 |"
CHNUM = re.compile(r"^\s+(\d+)\s*$")
CMD = re.compile(r"^\s*(\\medskip|\\hrule|\\engtitle|\\itxtitle|##)")
FOOTER = ("Mahabharata Critical Edition", "Encoding:", "Electronic text",
          "Pune, India", "http://bombay", "for further details")

def deva(t):
    t = t.replace(".h", "")
    return unicodedata.normalize("NFC", S.transliterate(t, S.ITRANS, S.DEVANAGARI)).strip()

def letters(n):
    return [chr(97 + i) for i in range(n)] if n <= 26 else [f"a{chr(97+i)}" for i in range(n)]

def parse(path, report, part):
    lines = Path(path).read_text(encoding="utf8").split("\n")
    # join TeX hyphen continuations
    joined = []
    for l in lines:
        if joined and joined[-1].endswith("\\-"):
            joined[-1] = joined[-1][:-2] + l.strip()
            report["joined_tex_hyphen"].append(f"{path.name}: {joined[-1][:60]}")
        else:
            joined.append(l)
    chapters, cur, titles, group = [], None, [], []
    def close_chapter():
        nonlocal cur, group
        if cur is None: return
        if group:   # lines without a closing marker
            report["orphan_lines"].append(f"{path.name} ch{cur['num']}: {group}")
            cur["items"].append({"kind": "orphan", "lines": group[:]})
            group = []
        chapters.append(cur); cur = None
    for raw in joined:
        s = raw.rstrip()
        if not s.strip() or s.lstrip().startswith("%") or CMD.match(s) or s.strip().startswith(FOOTER):
            continue
        m = CHNUM.match(s)
        if m:
            close_chapter()
            cur = {"num": int(m.group(1)), "titles": titles, "items": []}
            titles = []
            continue
        if s[0] in " \t":                 # indented heading text
            titles.append(s.strip()); continue
        titles = []
        if cur is None:
            report["before_first_chapter"].append(f"{path.name}: {s[:60]}"); continue
        m = NUM_END.search(s)
        m1 = None if m else SINGLE_END.search(s)
        if m or m1:
            m = m or m1
            v = int(m.group(1)); text = (NUM_END if NUM_END.search(s) else SINGLE_END).sub("||" if NUM_END.search(s) else "|", s)
            group.append(text)
            items = cur["items"]
            if items and items[-1]["kind"] == "verse" and items[-1]["v"] == v:
                items[-1]["lines"].extend(group); report["repeated_number"] += 1
            else:
                if items and items[-1]["kind"] == "verse":
                    pv = items[-1]["v"]
                    if v != pv + 1:
                        report["number_jumps"].append(f"{path.name} ch{cur['num']}: {pv} -> {v}")
                items.append({"kind": "verse", "v": v, "lines": group[:]})
            group = []
        elif PLAIN_END.search(s) and not group:
            cur["items"].append({"kind": "prose", "lines": [s]})
        else:
            group.append(s)
    close_chapter()
    return chapters

def main(raw_dir, book_dir):
    raw_dir, book_dir = Path(raw_dir), Path(book_dir)
    out = book_dir / "text"; out.mkdir(parents=True, exist_ok=True)
    report = {"joined_tex_hyphen": [], "before_first_chapter": [], "orphan_lines": [],
              "number_jumps": [], "repeated_number": 0, "parts": {}}
    titles_json = {}
    for src in sorted(raw_dir.glob("mbh??.itx")):
        part = int(src.stem[3:])
        chapters = parse(src, report, part)
        rows_by_ch, nverses = {}, 0
        for ch in chapters:
            rows, p = [], 0
            for it in ch["items"]:
                if it["kind"] == "verse" and len(it["lines"]) > 26:
                    # more lines than letters a-z: store as prose lines, log the verse number
                    report.setdefault("long_verses", []).append(
                        f"{part:03d}.{ch['num']:03d}.{it['v']}: {len(it['lines'])} lines stored as prose P-lines")
                    for t in it["lines"]:
                        p += 1
                        rows.append((f"{part:03d}.{ch['num']:03d}.P{p}", deva(t)))
                elif it["kind"] == "verse":
                    nverses += 1
                    lt = letters(len(it["lines"])) if len(it["lines"]) > 1 else [""]
                    for L, t in zip(lt, it["lines"]):
                        rows.append((f"{part:03d}.{ch['num']:03d}.{it['v']}{L}", deva(t)))
                else:
                    for t in it["lines"]:
                        p += 1
                        rows.append((f"{part:03d}.{ch['num']:03d}.P{p}", deva(t)))
            rows_by_ch[ch["num"]] = rows
            titles_json.setdefault(f"{part:03d}", {})[f"{ch['num']:03d}"] = [deva(t) for t in ch["titles"]]
        total = sum(len(r) for r in rows_by_ch.values())
        if total < 1000:
            rows = [r for c in sorted(rows_by_ch) for r in rows_by_ch[c]]
            (out / f"p{part:03d}.md").write_text("".join(f"{i} | {t}\n" for i, t in rows), encoding="utf8")
            layout = "part file"
        else:
            for c, rows in rows_by_ch.items():
                (out / f"ch{part:03d}.{c:03d}.md").write_text("".join(f"{i} | {t}\n" for i, t in rows), encoding="utf8")
            layout = "chapter files"
        report["parts"][f"{part:03d}"] = {"chapters": len(chapters), "verses": nverses, "lines": total, "layout": layout}
    (book_dir / "titles.json").write_text(json.dumps(titles_json, ensure_ascii=False, indent=1), encoding="utf8")
    (book_dir / "parse_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf8")
    for k, v in report["parts"].items(): print(k, v)
    print({k: (len(v) if isinstance(v, list) else v) for k, v in report.items() if k != "parts"})

main(sys.argv[1], sys.argv[2])
