# Status: mahabharata

Updated 2026-10-17 on branch docs/2026-10-17/version-1. Base source: S1 (BORI Critical Edition, Tokunaga / Smith, Sanskrit Documents ITRANS).

- Sanskrit `text/`: 17 of 18 parvans complete, parvan 3 (Aranyaka) cut off in chapter 241 (ISSUES I1). 1,937 chapters, 154,281 lines in 1,923 files (parvans 16 to 18 are one file each).
- `toc.md`: built from the files, chapter titles from the source; the map has NOT been confirmed by the owner. English names and purposes are empty.
- Hindi / English / word split (sandhi): not made yet. Run `/verify-vedic-book-reference`.
- Checks run: `check_extraction.py` (exit 0), structure check, word checker (see `VERIFY.md`, `checks/`). AI proofreading: not run.

## Next
1. Obtain `mbh03.itx` again (complete) and re-run `tools/itx_to_text.py`.
2. AI proofreading pass over `checks/typos.tsv`, `stray.tsv`, `metre.tsv` plus a sample.
3. Layers in chunks (`layers-work/`), starting with a short parvan.
