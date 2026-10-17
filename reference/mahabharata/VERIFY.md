# Verification log: mahabharata

## 2026-10-17 (branch docs/2026-10-17/version-1)
- Inventory: `raw/` (18 ITRANS files, S1), `devanagari/` (script conversion of the raw files, line for line), `text/` (extract format), tools, checks. No other kinds of files.
- Base text: Devanagari from the BORI ITRANS files, converted by `tools/itx_to_devanagari.py` and parsed by `tools/itx_to_text.py`.
- Completeness: `checks/structure.md`. Flag: part 003 truncated in chapter 241. All other parvans end with the source footer and have contiguous chapter numbers.
- Word checker: `checks/word_check.md`. Second edition: not available in this folder (the Kumbhakonam edition is a different recension and is not stored here), skipped.
- AI proofreading: not run yet.
- Layers pilot, parvan 18 (5 chapters, 205 units): draft agent per chapter, check_chunk.py clean (0 errors), independent review agent per chapter (8 to 11 units flagged per chapter, mostly small additions in translations; two real grammar errors fixed: 18.1 hatā, 18.3 upasevantu), 86 review patches applied, 1 patch re-applied by hand (changes_1.json). check_extraction.py: exit 0 with the layers aligned. EPUB `feed/mahabharata-p018.epub` read back by extract_book.py: 410 of 410 line numbers.
- Text flags raised by the drafts (suspected typos in the source, text unchanged): 18.1 cintayatumarhasi (cintayitum?), 18.2 sā (sa?) and yāsmyāmi (yāsyāmi), see the chunk files.
- Other parvans: not started.
