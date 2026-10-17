# Issues: Mahabharata (BORI CE, S1)

## I1. mbh03.itx (Aranyakaparva / Vana) is cut off mid-chapter 241 (open)
Found 2026-10-17 by the completeness check (chapter and verse numbering per file).
- The file ends after chapter 241's first words ("janamejaya uvAcha|| vasamAn") with no BORI footer. All 17 other files end with the footer and have contiguous chapter numbers.
- The raw file in `raw/` is byte-identical to what was attached, so the cut happened before it reached this repo (most likely when the file was downloaded or attached).
- The Critical Edition's Aranyakaparva is, as far as I recall, 299 adhyayas, so about 58 chapters (242 to 299) are missing. This number is from memory and must be confirmed against the source.
- Fix: download `mbh03.itx` again from the Sanskrit Documents mirror, check it ends with the footer, and attach it. `raw/mbh03.itx` and `devanagari/mbh03.txt` are then regenerated.

## I2. Chapters with irregular verse numbering (open, expected)
Verse numbers repeat, skip or restart inside some chapters (mbh01: 5 chapters, mbh02: 1, mbh03: 4, mbh04: 3, mbh05: 2, mbh06: 1, mbh08: 4, mbh09: 1, mbh12: 2, mbh13: 13, mbh14: 1, mbh16: 1). Kept as typed. Chapter-level list to be produced by the checker.

## Completeness check result (chapter numbering)
| Parvan | Chapters found | Contiguous 1..N |
|---|---|---|
| 1 Adi | 225 | yes |
| 2 Sabha | 72 | yes |
| 3 Aranyaka | 241 (file truncated) | yes up to 241 |
| 4 Virata | 67 | yes |
| 5 Udyoga | 197 | yes |
| 6 Bhishma | 117 | yes |
| 7 Drona | 173 | yes |
| 8 Karna | 69 | yes |
| 9 Shalya | 64 | yes |
| 10 Sauptika | 18 | yes |
| 11 Stri | 27 | yes |
| 12 Shanti | 353 | yes |
| 13 Anushasana | 154 | yes |
| 14 Ashvamedhika | 96 | yes |
| 15 Ashramavasika | 47 | yes |
| 16 Mausala | 9 | yes |
| 17 Mahaprasthanika | 3 | yes |
| 18 Svargarohana | 5 | yes |

Total 1,937 chapters and 75,880 verse markers in the 18 files. The chapter counts of the 17 complete files match what I recall for the Critical Edition; this has not yet been checked against a source.

## I3. Parser decisions and source oddities found while building text/ (info, 2026-10-17)
Made by `tools/itx_to_text.py`; see `parse_report.json` for the full lists.
- Verse numbers: 20 jumps inside chapters (listed in `parse_report.json`, key `number_jumps`; the structure check lists them too). Kept as typed.
- Repeated verse number on consecutive line groups: 4293 times; stored as extra lines (a, b, c ...) of the same verse.
- Lines `... | 001 |` (single bar, mbh01 prose passages): 241 lines, stored as numbered prose verses; the marker is kept as a single danda.
- Chapter-final lines without a closing marker (stored as prose lines `P`): mbh03.itx ch192: ['utta~NkamevamuktvA tu viShNurantaradhIyata |']; mbh03.itx ch241: ['vasamAn']; mbh09.itx ch38: ['tatrAjagAma balavAnbalabhadraH pratApavAn |'].
- 012.325.4: one numbered verse of 41 lines (a list of 160+ names). Stored as prose lines `012.325.P1..` because the ID format allows one line letter (a-z): `012.325.4: 41 lines stored as prose P-lines`.
- One TeX hyphen join: mbh12.itx: mAlyAbharaNavastrAbhya~NgagandhopabhoganRRittagIt.
- Headings (chapter titles) were not put into `text/`: they are in `titles.json` (Devanagari, per chapter) and in `toc.md`. They are not verses.

## I4. Word checker results (info, script only, nothing corrected)
`checks/word_check.md`, `stray.tsv`, `typos.tsv`, `metre.tsv`. Stray: 6 lines, e.g. 001.003.1a and 001.003.60a hold a leftover backslash (`\ब्ग्`, `\एग्`: raw TeX commands in the source), and `=` inside the name list 012.325. Typo candidates are many and mostly innocent (sandhi forms, case endings); tier 1 (difference inside the word) is the useful list. AI proofreading pass: not run yet.

