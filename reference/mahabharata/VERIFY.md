# Verification log: mahabharata

## 2026-10-17 (branch docs/2026-10-17/version-1)
- Inventory: `raw/` (18 ITRANS files, S1), `devanagari/` (script conversion of the raw files, line for line), `text/` (extract format), tools, checks. No other kinds of files.
- Base text: Devanagari from the BORI ITRANS files, converted by `tools/itx_to_devanagari.py` and parsed by `tools/itx_to_text.py`.
- Completeness: `checks/structure.md`. Flag: part 003 truncated in chapter 241. All other parvans end with the source footer and have contiguous chapter numbers.
- Word checker: `checks/word_check.md`. Second edition: not available in this folder (the Kumbhakonam edition is a different recension and is not stored here), skipped.
- AI proofreading: not run yet.
- Layers (-sandhi, -hindi, -english) and the quiz feed: not made yet.
