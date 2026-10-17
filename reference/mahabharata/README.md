# Mahabharata (Vyasa): raw extracted source bank

Stage 1 (extraction) of a pipeline; stage 2 (verification, layers, quiz feed) is `/verify-vedic-book-reference`. This folder holds the raw text, not a finished edition. Nothing here has been proofread by a person.

Edition: Critical Edition (BORI, Pune), electronic text by M. Tokunaga and J. D. Smith. Private use only (licence note in `sources.md`); keep this repository private.

Read, in order: FORMAT.md (file and line format), toc.md (structure), STATUS.md (what is done), sources.md (where text came from), ISSUES.md (known doubts), VERIFY.md (checks run).

| Folder | What |
|---|---|
| `raw/` | The 18 downloaded ITRANS files, unchanged, with SHA256SUMS |
| `devanagari/` | Same files converted to Devanagari, line for line |
| `text/` | The extract-format files (`ID | text`), one file per chapter (parvans 16 to 18: one file per parvan) |
| `titles.json`, `parse_report.json` | Chapter titles; every parser decision and oddity |
| `checks/` | Structure and word-checker results |
| `tools/` | `itx_to_devanagari.py`, `itx_to_text.py`, `make_toc.py`, `check_extraction.py` |

Rules for anyone editing here: text lines come only from the raw files; do not rename files or change IDs; record every doubt in ISSUES.md; run `python3 tools/check_extraction.py .` before every commit; push new branches only, the owner merges.
How to continue: STATUS.md "Next".
