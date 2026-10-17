# Sources: Mahabharata (Vyasa)

Requested primary edition: BORI Critical Edition (Sukthankar et al., Pune). Checked 2026-10-17.

Shell reach: GitHub (git, raw.githubusercontent.com) and PyPI work. GRETIL, SARIT site, sanskritdocuments.org, bombay.indology.info, sanskritlibrary.org, archive.org and sa.wikisource.org all return 403 from the shell. WebSearch/WebFetch can read pages but only as summaries, so they cannot supply bulk text.

| id | Source | Edition | Script | Licence | Completeness | Reach | Notes |
|---|---|---|---|---|---|---|---|
| S1 | Sanskrit Documents mirror, https://sanskritdocuments.org/mirrors/mahabharata/mahabharata-bori.html | BORI Critical Edition, typed by Muneo Tokunaga, revised by John D. Smith | per-parvan Devanagari HTML/PDF, ITRANS `mbh01.itx` ... `mbh18.itx` | not stated | 18 parvans (appendix and star passages only from Smith's site, registration needed) | blocked from shell | Best match for the request. Needs the user to download the 18 files |
| S2 | bombay.indology.info (John Smith's project page) | same text, "made available with BORI's agreement" | per its reader | not stated | includes separate supplementary passages | blocked | Online reader and supplementary passages; no bulk download link seen |
| S3 | Internet Archive item `mahabharat-bori-critical-edition-sanskrit-only` | "BORI-CE version", 18 volumes mbh-01 ... mbh-18 | Devanagari PDFs and OCR text (Tesseract, san) | not stated | 18 volumes | blocked | Uploader "educationpurposeonly". OCR text layer, so proofreading heavy. Fallback only |
| S4 | https://github.com/stotrasamhita/Mahabharatam (copy of SARIT TEI-XML `mahabharata-devanagari.xml`) | NOT BORI: Kumbhakonam edition (Krishnacharya and Vyasacharya, 1906-1910), southern recension | Devanagari | repo CC0, source text CC BY-SA (SARIT) | all 18 parvans | reachable | A different edition with a different structure and length |
| S5 | https://github.com/cogni-prith/mahabharata | English translation of BORI CE, no Sanskrit | n/a | unclear, repo may be private | n/a | n/a | Not usable as Sanskrit source |

No GitHub repo with the BORI Critical Edition Sanskrit text was found. GitHub-wide search is not available in this session.

## Captured raw files (2026-10-17): all 18 parvans of S1

Supplied by the owner (downloaded from the Sanskrit Documents mirror), saved unchanged in `raw/`; checksums in `raw/SHA256SUMS` (`sha256sum -c SHA256SUMS`). Every file's own header names itself `mbhNN.itx`, ITRANS 5.3, latest update September 16, 2013, pure ASCII (no Devanagari yet).

| File | Parvan | Lines | Bytes |
|---|---|---|---|
| mbh01 | 1 Adiparva | 25,459 | 828,169 |
| mbh02 | 2 Sabhaparva | 8,385 | 273,279 |
| mbh03 | 3 Aranyakaparva (Vana) | 29,370 | 961,313 |
| mbh04 | 4 Virataparva | 6,613 | 213,038 |
| mbh05 | 5 Udyogaparva | 21,081 | 705,158 |
| mbh06 | 6 Bhishmaparva | 18,251 | 612,092 |
| mbh07 | 7 | 27,063 | 908,645 |
| mbh08 | 8 | 13,031 | 460,405 |
| mbh09 | 9 | 11,304 | 377,637 |
| mbh10 | 10 | 2,647 | 87,927 |
| mbh11 | 11 | 2,575 | 82,687 |
| mbh12 | 12 | 44,529 | 1,470,048 |
| mbh13 | 13 Anushasanaparva | 22,782 | 745,655 |
| mbh14 | 14 Ashvamedhikaparva | 9,777 | 314,614 |
| mbh15 | 15 Ashramavasikaparva | 3,781 | 121,731 |
| mbh16 | 16 Mausalaparva | 965 | 32,936 |
| mbh17 | 17 Mahaprasthanikaparva | 421 | 13,934 |
| mbh18 | 18 Svargarohanaparva | 697 | 23,238 |

Observations for the next stage (nothing has been changed):
- Some shorter parvans (16 to 18) end with a footer: "Mahabharata Critical Edition Only for Personal Studies ... Electronic text (C) Bhandarkar Oriental Research Institute, Pune, India, 1999". It is not verse text and must be dropped by the parser.
- Chapter headings are an adhyaya title line followed by its number; speaker lines end `uvAcha||`; verses end `|| N||`. Some verse numbers repeat or are skipped within a chapter (for example mbh16 chapter 2 jumps from 11 to 13, and chapter 3 has verse 4 twice). Keep them and log them in ISSUES.md.
- These files are the main text only. The appendix and star passages are not included (only on Smith's site, registration needed). No Harivamsa file is in this set.

Licence note from the file header: "prepared by volunteers and is to be used for personal study and research"; not to be reposted for promotion of any website or individual or for commercial purpose without permission. The owner confirmed on 2026-10-17 that `eckko/mahabharat` is private. Do not make the repository public with `raw/` inside without permission.
