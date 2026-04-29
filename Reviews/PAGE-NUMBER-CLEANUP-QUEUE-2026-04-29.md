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

## Current Source-Anchor Pass

**2026-04-29, Chapter 10:** Tightened the Bretton Woods quote apparatus in `Content/04-Part-IV-Breaking-Beyond/10-Chapter-10/sources.md`.

Now anchored:

- Robbins/Vinson "We know we will be beaten..." — Steil (2013), p. 224.
- Keynes/White October 1943 "Talmud" / "Your Highness" exchange — Steil (2013), p. 165.
- White procedural-control quote to Morgenthau — Steil (2013), p. 212.
- Keynes July 19 heart attack as context for British weakness — Steil (2013), p. 224, with Skidelsky edition page still to add if used directly.
- Keynes December 1944 "clean and consecutive copy" / "dotted line" letter — Steil (2013), p. 251.
- New York *World-Telegram* "kid who owns the ball" quotation — Steil (2013), p. 189.

Still needs edition/page access:

- Robbins diary "glorious confusion," "virtues as technicians," and "not good organisers" in the Macmillan printed edition / LSE Robbins file.
- Theunis "you are on your knees" quote in Robbins diary / Steil.
- Bareau Savannah quotes and Keynes's "tyrant" line in Skidelsky/Steil.
- Keynes "absolute hell" loan-negotiations quote in Skidelsky.
- Official Proceedings page or document anchor for the Shroff/Bernstein/Robertson "gold convertible exchange" exchange if we want primary-proceedings citation rather than Steil's reconstruction.

**2026-04-29, Chapter 8:** Tightened the Attwood / Currency School / deposit-creation quote apparatus in `Content/03-Part-III-Gold-Standard/08-Chapter-8/sources.md` and softened unanchored exact-quote language in the live text.

Now anchored:

- BPU motto "PEACE, LAW, ORDER, LOYALTY and UNION" — Wakefield (1885), title-page epigraph.
- George Grote tribute to Attwood's law-bound organizing — Wakefield (1885), Introduction, p. v.
- Briggs proto-Keynesian caution — Briggs (1948), article range 190-216, note 73.
- Miller's "popular radicals" frame — Miller (2012), pp. 354-377.
- Charles Wood / Overstone "person to whom we are really indebted for the Act of 1844" — O'Brien (1971), vol. 1, p. 381; Eltis (2001), p. 10.
- Newdegate "sheer loss without the shadow of an equivalent" — Hansard, Commons, 13 June 1844, cols. 829-830.
- Goulburn "had consequently met with the concurrence" — Hansard, Commons, 13 June 1844, col. 809.
- Hawes warning about small bills and acceptances — Hansard, Commons, 13 June 1844, col. 831.

Still needs edition/page access:

- Attwood "strong as a giant" / "weak as an infant" formulation in Wakefield or another primary Attwood source.
- Disraeli "provincial banker labouring under a financial monomania" in Money (1920) / Checkland.
- Goodhart "fare-thee-well" quotation in the final edition of *Money, Information and Uncertainty*, ch. 5.
- Samuel Gurney's October 25, 1847 testimony page and/or question number in Parliamentary Papers 1847-48 (395) VIII, Pt. I.
- Mill, Bagehot, and Keynes exact page anchors if we later restore direct quotations about credit/deposit creation; the live text now paraphrases the less-secure Mill/Bagehot phrasings.

**2026-04-29, Chapters 3-5:** Tightened Backwell / goldsmith banking and Bank of England founding mechanics in the source apparatus.

Now anchored:

- Strype's Lombard Street description — Strype (1720), *Survey of the Cities of London and Westminster*.
- Backwell shop scene, crusados, perfumed comfits — Pepys diary, June 17, 1662.
- Backwell "good master, the King" line — Pepys diary, July 23, 1666.
- Backwell "vain glory" line — Pepys diary, November 15, 1667.
- Backwell "little town" property line — Pepys diary, April 12, 1669.
- January 1672 Treasury sequence — *Calendar of Treasury Books*, vol. 3 (1669-1672), January 1672 entries.
- Langhorne "trade of bankers is totally destroyed" line — Hatton Correspondence, Camden Society, vol. 1 (1878), p. 101.
- Stop of Exchequer litigation and settlement history — Horsefield (1982), pp. 511-528.
- Backwell ledger/customer base and £295,994 claim — Hilton Price (1890), pp. 191-230; NatWest Group Heritage Hub; Archives Hub Backwell records.
- Bank of England founding bargain — Tonnage Act 1694, 5 & 6 William and Mary c. 20; Broz and Grossman (2004), pp. 48-72.

Still needs edition/page access:

- Exact printed-page or section anchor for Strype's Lombard Street passage if using a specific edition rather than online text.
- Exact Latham/Matthews volume/page references for the Pepys entries, though diary dates are stable enough for working notes.
- Exact NatWest/Archives Hub stable object page for the 1671-72 Backwell ledger if a publisher wants archive-level citation.
- Clapham, Dickson, Roseveare, and Horsefield page anchors for sealed bills, running cash notes, early Bank balance-sheet mechanics, and tally-to-Bank continuity in Chapters 4-5.

**2026-04-29, Chapter 7:** Tightened Bank Restriction, resumption, and farmer-distress source anchors.

Now anchored:

- Bank Restriction framework — O'Brien and Palma (2020), pp. 390-426; Bank Restriction Act, 37 Geo. III, c. 45.
- Bank note circulation benchmarks — Clapham, Vol. 2; O'Brien and Palma (2020), pp. 390-426, with the £2.3 million small-note caution retained.
- Wheat-price benchmarks and wartime/postwar decline — Clark (2003) price series.
- Suffolk "one unusual scene of distress" — Hansard, Commons, 18 February 1822.
- Matthias Attwood abandonment warning — Hansard, Commons, 7 May 1822.
- Essex "not possessed of a shilling" testimony — Hansard, Series 2, Vol. 7, 13 May 1822, cols. 654-655.
- Farmer insolvency examples — Elwick (1843), *London Gazette* issues 1821-1826, and the named Gazette notices already listed in Chapter 7 sources.

Still needs edition/page access:

- Clapham Vol. 2 exact pages for 1797 and 1814 note-circulation figures.
- Clark table/page or dataset row anchors for each wheat-price benchmark used in the live text.
- Ricardo Vol. 10 exact page for the December 1821 Paris letter.
- 1821 Select Committee page/question anchors for William Hanning and George Webb Hall.
- Cobbett *Rural Rides* edition/page anchors if any direct scenic quotation is restored.

## Internal-Dossier Conversion

First conversion pass complete: chapter source files no longer contain public-facing `Local research dossier` entries. Working research files remain in the repository for internal audit, but the reader-facing source layer now points to underlying source families.

## Current-Data Refresh Pass

Incorporated the 2026 data refresh into the live manuscript and submission materials where it strengthens the argument rather than overloading the book with volatile statistics.

Now updated:

- Chapter 12 Fed balance-sheet sequence through April 2026 quantitative tightening.
- Chapter 12 inflation/capacity section with March 2026 CPI, February 2026 PCE, and March 2026 capacity-utilization anchors.
- Chapter 12 Japan employment-ice-age update with the April 2026 support-program sources.
- Chapter 12 crypto/FTX section with 2026 stablecoin scale language and FTX Recovery Trust distribution framing.
- Proposal, query prep, and jacket-copy materials so the "why now" case reflects the nearly two decades since 2008, the 2026 inflation last mile, and FTX's court-administered recovery.

## Source-Safe Paraphrase Pass

Converted several exact quotations or overly specific numerical phrasings into source-safe paraphrase where the point did not require direct quotation and the available apparatus did not yet include final edition page anchors.

Now softened:

- Chapter 8 Attwood "strong as a giant / weak as an infant" formulation now paraphrases the legalist-radical point while retaining the anchored BPU motto.
- Chapter 8 Goodhart "fare-thee-well" deposit-creation quote now paraphrases Goodhart's argument pending exact final-edition page verification.
- Chapter 10 Keynes "absolute hell" loan-negotiation wording now paraphrases the punishing character of the negotiations.
- Chapter 12 housing-price appreciation phrase now avoids an unanchored exact 2019 percentage.
- Chapter 1 and glossary *jiaozi* entries now distinguish nominal strings/cash value from literal note/coin counts.
- Epilogue now includes a concise Job Guarantee / employment-buffer-stock paragraph with supporting source note, addressing the policy-clarity concern without restoring the old extended policy appendix.

Search checks now show no remaining main-manuscript hits for the old approximate-page or fragile-quote flags: `~p.`, `~pp.`, `approximately p.`, `around p.`, `strong as a giant`, `weak as an infant`, `fare-thee-well`, `absolute hell`, `99.91`, or the flagged stale chronology phrasings.

## Blank-Context Review Round

Fresh v9 review packet saved at `Reviews/PERSONA-CRITIQUES-2026-04-29-v9-blank-context-current.md`.

Result: strong but not clean 5/5. The manuscript now reads as well-reviewed / near-must-read. All four fresh reviewers identified Chapter 12 density as the main remaining craft issue; three or more also named repeated explanatory restatement, source traceability for high-risk claims, and a more concrete but restrained policy payoff.

Immediate fixes completed from that round:

- Corrected the Chapter 1 *jiaozi* unit issue flagged by the historian.
- Added the concise Epilogue Job Guarantee / employment-buffer-stock paragraph requested by the heterodox reviewer.
- Continued source-safe paraphrase cleanup for unpaginated exact quotations.
- Completed a conservative Chapter 12 streamline: Chapter 12 narrative now counts at 7,921 words, and the full narrative manuscript counts at 62,816 words.

Remaining high-confidence craft pass:

- Re-review Chapter 12 after the streamline; split only if fresh readers still experience it as a crowded second book.
- Cut repeated explanatory/thematic restatement in Chapters 2, 4, 5, 8, 12, and chapter endings.
- Add or preserve precise source anchors for high-risk reconstructed scenes, numerical claims, and direct quotations.

Submission-day refresh targets:

- Replace February 2026 PCE with March 2026 PCE once the April 30, 2026 BEA release is available.
- Recheck CPI, Fed H.4.1/WALCL, capacity utilization, stablecoin market size, and FTX recovery distribution status immediately before sending materials.
- Add IMF COFER reserve-share or Fed target-rate figures only if the final proposal or manuscript text starts relying on those specific claims.

## Current Status

No missing page number currently blocks the manuscript's argument. This is normal publishing cleanup, not a must-read-status issue.
