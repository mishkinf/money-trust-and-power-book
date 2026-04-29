# Page-Number Cleanup Queue

**Date:** 2026-04-29
**Purpose:** Track citation/page-number cleanup without reopening substantive revision.

## Rule

Do not invent page numbers. If the edition is not in hand or a digital scan does not expose stable pagination, keep the citation at chapter/article level and mark the page lookup for later.

## Already Has Usable Page Anchors

These are good enough for the current working apparatus, subject to final edition consistency:

| Location | Source anchor |
|---|---|
| Consolidated Notes, Chapter 1 | von Glahn, *Fountain of Fortune*, p. 49; Peng, p. 393; Yang, p. 32. |
| Consolidated Notes, Chapter 9 | Keynes, *Collected Writings*, Vol. IX, pp. 207-230 and p. 223. |
| Consolidated Notes, Chapter 11 | Volcker, *Keeping At It*, pp. 71-74. |
| Chapter 10 sources | Steil, *Battle of Bretton Woods*, pp. 233-276; newspaper quotation at p. 189. |
| Chapter 11 sources | Schenk, Wilson, Callaghan, Hennessy, IMF, Dell, Gavin, Solomon, Gowa, Volcker/Gyohten, Steil, Eichengreen entries mostly include page ranges. |
| Chapter 12 sources | Hagedorn/farm-crisis, Rust Belt, Eurozone, supply-chain, fiscal-stimulus, and several modern-data sources include page ranges or stable URLs. Hayek/Ammous approximate page references were removed pending final edition verification. |

## Needs Page Cleanup Before Publication-Facing Notes

| Priority | Source family | What to verify |
|---|---|---|
| High | Overstone / Norman / Currency School institutional-capture material | Page references in Overstone correspondence, Eltis, Fetter, History of Parliament, Bank Act committee records, and Gladstone/Wood/Russell correspondence. |
| High | Attwood / Birmingham School | Page references in Briggs, Miller, Moss, and primary Attwood pamphlets for the "proto-Keynesian" caution, Newhall Hill, Chartist petition, and monetary-contraction claims. |
| High | Backwell / goldsmith banking | Page references in Quinn dissertation, NatWest archive material, D.M. Mitchell, Pepys entries, Strype, and Stop of Exchequer sources. |
| High | Bank of England founding mechanics | Page references in Clapham, Dickson, Roseveare, Pressnell, Bell, Mehrling, and relevant statutory/parliamentary materials. |
| Medium | Newton / gold-standard adoption | Page references in Redish, Velde/Webber, Flandreau, Eichengreen, Newton Mint material, and country-adoption sources. |
| Medium | Bank Restriction / resumption / farmer distress | Page references in O'Brien/Palma, Clark, Thornton, Ricardo, Cobbett, Hilton, Gazette insolvency notices, Hansard, and farmer-distress dossiers. |
| Medium | Bretton Woods / bancor | Page references in Steil, Skidelsky, Helleiner, Horsefield, Keynes *Collected Writings* Vol. XXV, and Bretton Woods proceedings. |
| Medium | 1971 / Triffin / dollar hegemony | Page references in Triffin, Eichengreen, Solomon, Gavin, Gowa, Garber, Volcker/Gyohten, Garten, Safire, and Silber. |
| Medium | Chapter 12 modern profile material | Confirm stable source locations for Kono, McKenzie, Lehman employees, Terri Smith/FTX, Hagedorn, Ty Stehlik, and modern inflation/decomposition studies. |
| Low | Supplementary materials | Bring timeline, glossary, key figures, and further reading into the same citation style only after the main manuscript notes are stable. |

## Approximate Page Flags To Clean

Search targets:

- `~p.`
- `~pp.`
- `approximately p.`
- `around p.`
- `Chapter [number]` where a page number would be materially better.
- Any quotation without page number in a book-length source.

Known current example:

- Chapter 12 Hayek/Ammous approximate page references were removed in the first page-cleanup pass; verify against final editions before restoring page numbers.
- Paterson "money out of nothing" attribution: first OCR search of public Internet Archive scans of Bannister's three volumes did not locate the exact phrase. Keep the source note's contested-attribution language unless a stable printed page is later found.

## Internal-Dossier Conversion

First conversion pass complete: chapter source files no longer contain public-facing `Local research dossier` entries. Working research files remain in the repository for internal audit, but the reader-facing source layer now points to underlying source families.

## Current Status

No missing page number currently blocks the manuscript's argument. This is normal publishing cleanup, not a must-read-status issue.
