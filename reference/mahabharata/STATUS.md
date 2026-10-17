# Status: mahabharata

Updated 2026-10-17 on branch docs/2026-10-17/version-1. Base source: S1 (BORI Critical Edition, Tokunaga / Smith, Sanskrit Documents ITRANS).

- Sanskrit `text/`: 17 of 18 parvans complete, parvan 3 (Aranyaka) cut off in chapter 241 (ISSUES I1). 1,937 chapters, 154,281 lines in 1,923 files (parvans 16 to 18 are one file each).
- `toc.md`: built from the files, chapter titles from the source; the map has NOT been confirmed by the owner. English names and purposes are empty.
- Hindi / English / word split (sandhi): pilot done for parvan 18 only (205 units, 5 chunks): `text/p018-sandhi.md`, `-hindi.md`, `-english.md`, drafted by model, independently reviewed by a second model, patches applied (`layers-work/p018/*/changes_1.json`). NOT yet read by a person. Other parvans: not started (whole book is about 2,324 chunks, roughly 26 million draft tokens plus the same for review).
- Quiz feed: `feed/mahabharata-p018.epub` (+ `.map.json`, `feed/p018/part00N.txt`) for `/quiz-advanced-cdn`, part 18 only.
- Checks run: `check_extraction.py` (exit 0), structure check, word checker (see `VERIFY.md`, `checks/`). AI proofreading: not run.

## Next
1. Obtain `mbh03.itx` again (complete) and re-run `tools/itx_to_text.py`.
2. AI proofreading pass over `checks/typos.tsv`, `stray.tsv`, `metre.tsv` plus a sample.
3. Owner reads the pilot layers; then choose the next parvans (`plan_work.py --parts N`).
