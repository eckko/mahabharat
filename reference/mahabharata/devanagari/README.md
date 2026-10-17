Devanagari plain-text copies of `../raw/mbh01.itx` to `mbh18.itx`, made by `../tools/itx_to_devanagari.py` (ITRANS 5.3 to Devanagari with `indic_transliteration`). Nothing is edited, dropped or corrected, and line N here is line N of the raw file, so the two can be compared line by line.

- Header comments (`%`), TeX commands (`\medskip`, `\hrule`, `##`) and the English footer are copied unchanged. Only text lines are converted.
- `.h` (explicit halant, as in `pravrajanam.h`) is dropped because the converter already puts the halant on a word-final consonant.
- Source marks that carry over as they are: `;` inside some verses (the editors' half-verse mark), a few `-`, `=`, `( )` and one `\-` (TeX line-break hyphen) at the end of a long line in a prose passage.
- Checks run: same line count as raw for all 18 files; 156,661 lines converted; no Latin letters left on converted lines; Devanagari to ITRANS to Devanagari round trip is stable on every converted line. These checks show consistency, not correctness of the original typing.
