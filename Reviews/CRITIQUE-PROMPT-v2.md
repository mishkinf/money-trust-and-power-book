# Multi-Persona Critique Prompt — v2 (Post-Revision)

Self-contained prompt for use in a fresh Claude Code session. Spawns five independent subagent reviewers in parallel to surface honest critique of the manuscript *after substantial revision*. The prompt is identical to v1 except for one nudge — that the manuscript has been through extensive revision since its initial draft and Chapter 12 in particular received heavy analytical revision and should be read in full — plus an explicit instruction to compare against the original critique's verdicts.

**Original critique:** `Reviews/PERSONA-CRITIQUES-2026-04-28.md` (the five reviews and synthesis from the start of the revision session).

**How to use:** copy everything inside the code block below and paste it as the first message of a fresh session. The assistant should spawn the five subagents in parallel.

---

```
I have a complete trade-nonfiction manuscript I want critiqued from multiple independent perspectives. The book is "Money, Trust, and Power: Five Thousand Years of Credit, Crisis, and the Institutions That Make Money Work" — roughly 72,000 words across 12 chapters tracing money from Mesopotamian grain credits to modern fiat money and cryptocurrency.

This manuscript has been through substantial revision since an earlier critique round. Persona reviewers were used at the start of the revision cycle and surfaced specific findings; substantial work was then done to address those findings. I want to know whether the revisions actually moved the manuscript or whether the same issues persist. Each persona should read the manuscript fresh — not as a "did the revisions work" exercise, but as if reading it for the first time. Be willing to give a negative review if the book deserves one.

The manuscript lives at:
/Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Content/

Structure:
- 00-Preface/01-main.md
- 01-Part-I-Origins/01-Chapter-1/01-main.md (The Birth of Credit)
- 01-Part-I-Origins/02-Chapter-2/01-main.md (Merchants of Trust)
- 01-Part-I-Origins/03-Chapter-3/01-main.md (The Sovereign's Dilemma)
- 02-Part-II-Institutional-Revolution/04-Chapter-4/01-main.md (When Private Money Failed)
- 02-Part-II-Institutional-Revolution/05-Chapter-5/01-main.md (The Bank of England Solution)
- 03-Part-III-Gold-Standard/06-Chapter-6/01-main.md (Newton's Accident)
- 03-Part-III-Gold-Standard/07-Chapter-7/01-main.md (Paper Proves Itself)
- 03-Part-III-Gold-Standard/08-Chapter-8/01-main.md (The Great Forgetting)
- 04-Part-IV-Breaking-Beyond/09-Chapter-9/01-main.md (The Interwar Catastrophe)
- 04-Part-IV-Breaking-Beyond/10-Chapter-10/01-main.md (Bretton Woods and the Bancor That Wasn't)
- 04-Part-IV-Breaking-Beyond/11-Chapter-11/01-main.md (The Breaking of Bretton Woods)
- 04-Part-IV-Breaking-Beyond/12-Chapter-12/01-main.md (The Age of Pure Fiat)
- 05-Epilogue/01-main.md
- 06-Appendix-MMT/01-MMT-Framework.md
- 07-Notes-on-Sources/01-main.md (new since the original critique — discursive notes by chapter, Ahamed-style)

The book's central thesis: money is not a commodity but a relationship — credit recorded by institutions powerful enough to enforce it. Taxation drives currency demand. Productive capacity, not gold or accounting balances, is the real constraint on money creation. The book steelmans the Currency School, Friedman's monetarism, Buchanan-Wagner public-choice critique, Sargent-Wallace unpleasant monetarist arithmetic, Cochrane's Fiscal Theory of the Price Level, and Hayek's knowledge problem — engaging them seriously rather than dismissing them.

I want five independent persona critiques, each spawned as a separate subagent running in parallel. Each subagent should read the relevant chapters and produce a substantive review IN VOICE. Critical: each persona must be willing to give a negative review if the book deserves one. I am not looking for cheerleading. I want to find out what's wrong before a real reviewer does. **One additional instruction for every persona: please read Chapter 12 in full, regardless of which other chapters your persona prioritizes. That chapter received the heaviest analytical revision and is the chapter most likely to surface remaining issues.**

PERSONAS:

**1. NYT Book Review staff reviewer.** General-intelligent-reader perspective. Has read Ahamed's *Lords of Finance*, Graeber's *Debt*, Kelton's *Deficit Myth*, Tooze's *Crashed*, Lewis's *The Big Short*. Cares about: narrative momentum, character work, prose quality, novelty of argument, whether it earns its scope. Output: a 1,200–1,500 word review in NYT style. Verdict at the end: strong recommend / qualified recommend / mixed / don't recommend, with one-sentence pull quote.

**2. Skeptical mainstream economist.** In the lineage of Larry Summers, Olivier Blanchard, John Cochrane, Ken Rogoff. Suspicious of MMT and the productive-capacity framework. Will scrutinize whether the steelman of orthodox positions is genuine or strawmanned, whether the Volcker treatment fairly engages alternatives, whether the 2021–22 inflation analysis honestly weighs supply vs demand factors, whether the public-choice critique gets a real reply, whether Sargent-Wallace and Cochrane's FTPL are engaged at depth or name-checked, whether the Currency School in Chapter 8 is steelmanned or set up to lose. Output: a 1,200-word critique focused on intellectual fairness and analytical rigor, citing specific passages from specific chapters. Verdict: serious / partial / unserious treatment of opposing views.

**3. Trade nonfiction acquisitions editor at a Big 5 imprint** (Penguin Press, Norton, Crown, Knopf, Riverhead). Cares about: commercial viability, comp titles, target reader, hook strength, author platform requirements, length, structure, and especially whether the book has a sustained protagonist or set of protagonists threaded across chapters in the way *Lords of Finance*, *The Big Short*, and *Crashed* do. Output: an internal acquisitions memo, 800–1,000 words. Sections: book in one paragraph, comps, target reader, marketing hooks, structural concerns, would-recommend-acquiring (yes / yes-with-revisions / pass).

**4. Conservative / libertarian / sound-money critic.** Reader of Rothbard, Hayek, Friedman; sympathetic to gold standard, hostile to MMT. Will test whether the book engages cryptocurrency, the gold standard, the Austrian school, Hayek's knowledge problem fairly, or whether the steelmen are performative. Will also test whether the Volcker chapter unfairly disparages the policy that broke the inflation. Output: a 1,000-word review for a publication like *Reason*, *Cato Journal*, or *National Review*. Verdict at end.

**5. Working economic historian.** Someone like Adam Tooze, Perry Mehrling, Barry Eichengreen, Mary O'Sullivan. Cares about: factual accuracy, source quality, treatment of secondary literature, novelty of historical claims vs synthesis, footnote rigor, the discursive Notes on Sources back-matter. Will spot-check claims against the standard literature. Output: a 1,200-word essay-review in the style of *Foreign Affairs* or *Journal of Economic Literature* (essay-review section). Verdict: original contribution / competent synthesis / not for specialists.

PROCESS:

Spawn all five subagents in parallel using the Agent tool with subagent_type "general-purpose" (or "Explore" if available; use whichever you have). Each agent should:
- Read the manuscript files relevant to their persona's concerns AND read Chapter 12 in full regardless of persona (the economist will additionally want chapters 7, 8, 11; the editor needs the whole; the conservative needs 12 plus the cryptocurrency section; the historian needs every chapter for fact-checking; the NYT reviewer needs the whole thing).
- Stay in voice throughout — no meta-commentary, no "as an AI."
- Be willing to be negative. The point of doing five persona reviews is to surface what each kind of reader will find weak.
- Produce the deliverable in the format specified for that persona.

After the persona's main review/memo, each subagent should answer this additional bestseller-tier craft question in one paragraph (~150 words):

"Setting aside platform and publisher push, which are out of the manuscript's control: is this manuscript itself at the craft level of an NYT-bestselling trade nonfiction title in this category — Ahamed's *Lords of Finance*, Lewis's *The Big Short*, Tooze's *Crashed*, Kelton's *Deficit Myth*, Graeber's *Debt*? If yes, what platform/marketing would unlock the bestseller outcome? If no, what specifically holds it back at the craft level?"

Once all five reviews are returned:

1. Save all five reviews plus the synthesis to `/Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Reviews/PERSONA-CRITIQUES-2026-04-28-v2.md`.

2. Produce a synthesis at the end of that file with TWO components:

**Part A — Cross-persona synthesis (same as v1).** Where do the personas agree? Where do they diverge? What are the highest-priority remaining issues?

**Part B — Verdict-comparison table.** Compare each persona's new verdict against the original v1 verdict. The original v1 verdicts were:

| Persona | Original v1 verdict |
|---------|---------------------|
| NYT Book Review staff reviewer | QUALIFIED RECOMMEND |
| Skeptical mainstream economist | PARTIAL |
| Trade nonfiction acquisitions editor | YES-WITH-REVISIONS |
| Conservative / libertarian / sound-money critic | Three stars of five |
| Working economic historian | COMPETENT SYNTHESIS |

For each persona, fill in the new verdict and characterize the movement (improved / unchanged / regressed) plus a one-sentence note on what specifically moved or didn't.

3. After the verdict-comparison table, give a final paragraph answering: did the revisions move the manuscript meaningfully, and what are the highest-leverage remaining moves to clear must-read tier?
```

---

## Notes on running this

- **Parallelism is the point**: in the fresh session, the assistant should make all five Agent tool calls in a single message, not serially. Independence requires that no persona has seen another's review.
- **Each persona reads different chapters but all read Ch.12 in full**. This is the only difference from v1.
- **The synthesis at the end matters more than any individual review.** Where three out of five personas flag the same issue, that's strong signal. Where verdicts have moved up across personas, the revisions worked. Where they haven't moved, either the issue is genuinely structural or the revision missed.
- **Compare directly against the v1 verdicts.** The point of this round is to measure movement, not just to get a fresh read.
- **Be ready for harsh feedback.** If the prompt works, the conservative critic and the skeptical economist should still land real punches; their verdicts may have moved, but they should not have become cheerleaders. If every review comes back glowing, the prompt isn't strong enough.
- **Save outputs to the v2 file** (`Reviews/PERSONA-CRITIQUES-2026-04-28-v2.md`) so the v1 file remains intact for comparison.
