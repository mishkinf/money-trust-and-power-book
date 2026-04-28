# Multi-Persona Critique Prompt — v3 (Post-Threading)

Self-contained prompt for use in a fresh Claude Code session. Spawns four independent subagent reviewers in parallel to test whether the structural threading work moved the manuscript to must-read tier.

**Why a different bench than v1/v2.** The v1 and v2 rounds used five personas weighted toward antagonistic and gatekeeping reads (skeptical economist, conservative critic, NYT, editor, historian). Both of those rounds converged on the same diagnosis — strong analytical fairness, strong set pieces, weak connective tissue, no sustained protagonists — and both held verdicts in place across substantial revision. The v3 round drops the two reviewers whose v2 critiques were rhetorical-balance complaints unlikely to be moved by any plausible threading work (skeptical economist, conservative critic), keeps the two whose verdicts the threading work is *designed* to move (editor, historian), and adds two voices the prior rounds did not test:

- a **sympathetic heterodox reviewer** in the chartalist/MMT/credit-money tradition the book purports to translate, to test whether the steelmanning has gone so far that the book reads as apologetic to the tradition's own practitioners;
- a **target lay reader** representing the actual buying audience, to test whether the book *works* commercially with someone who is not a professional gatekeeper.

The v3 round is also smaller (4 reviews vs 5) because the diagnostic question is narrower: did threading land, and does the book work for non-gatekeeper readers? It is not a full re-evaluation.

**Prior critiques:**
- v1: `Reviews/PERSONA-CRITIQUES-2026-04-28.md`
- v2: `Reviews/PERSONA-CRITIQUES-2026-04-28-v2.md`

**v2 verdicts** (carry these forward for the editor and historian comparison):

| Persona | v2 verdict |
|---------|-----------|
| Trade nonfiction acquisitions editor | ACQUIRE WITH REVISIONS |
| Working economic historian | COMPETENT SYNTHESIS |

**How to use:** copy everything inside the code block below and paste it as the first message of a fresh session. The assistant should spawn the four subagents in parallel.

---

```
I have a complete trade-nonfiction manuscript that has now been through two prior persona-critique rounds and a structural threading revision pass. I want a focused four-persona round to test whether the latest revisions moved the manuscript to must-read tier.

The book is "Money, Trust, and Power: Five Thousand Years of Credit, Crisis, and the Institutions That Make Money Work" — a trade nonfiction title tracing money from Mesopotamian grain credits to modern fiat money and cryptocurrency. The book's central thesis: money is not a commodity but a relationship — credit recorded by institutions powerful enough to enforce it. Taxation drives currency demand. Productive capacity, not gold or accounting balances, is the real constraint on money creation. The book steelmans the Currency School, Friedman's monetarism, Buchanan-Wagner public-choice critique, Sargent-Wallace unpleasant monetarist arithmetic, Cochrane's Fiscal Theory of the Price Level, and Hayek's knowledge problem.

Since the v2 critique, the manuscript has had a structural threading pass that wove four figures across multiple chapters as recurring rather than one-chapter presences:
- Edward Backwell across Chapters 3, 4, and 5
- Thomas Attwood across Chapters 7, 8, and 9
- Paul Volcker across Chapters 10, 11, and 12
- John Maynard Keynes lightly across Chapters 7, 9, and 10
The Notes on Sources back-matter has been extended to cover the chapters previously unrepresented (3, 4, 5, 7, 9, 11). Smaller fixes: the MMT appendix has been [revised / cut — author to confirm at run time], a Chapter 12 demand-share framing fix, a Chapter 6 gold-standard-balance acknowledgment, and a Chapter 8 narrative-architecture rebalance.

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
- 06-Appendix-MMT/01-MMT-Framework.md (or removed; check directory)
- 07-Notes-on-Sources/01-main.md

I want four independent persona critiques, each spawned as a separate subagent running in parallel. Each persona must be willing to give a negative review if the book deserves one. I am not looking for cheerleading.

Special instructions for every persona: read in full the chapters where threading was added (Chapters 3, 4, 5, 7, 8, 9, 10, 11, 12), since the threading work cannot be evaluated without seeing how figures enter and exit chapters. The Preface, Chapters 1–2, the Epilogue, and the Notes on Sources should be read by personas whose remit covers them.

PERSONAS:

**1. Trade nonfiction acquisitions editor at a Big 5 imprint** (Penguin Press, Norton, Crown, Knopf, Riverhead). Same persona as v2. Cares about commercial viability, comp titles, target reader, hook strength, length, structure, and especially whether the threading actually delivers sustained protagonists — Backwell echoing across 3/4/5, Attwood across 7/8/9, Volcker across 10/11/12 — in the way Lords of Finance, The Big Short, and Crashed sustain protagonists. The v2 verdict was ACQUIRE WITH REVISIONS, with the structural protagonist problem named as the single biggest commercial risk. The question for this round: does the threading move the verdict to a clean ACQUIRE, or is it cosmetic? Output: an internal acquisitions memo, 800–1,000 words. Sections: book in one paragraph, what changed since v2, target reader, marketing hooks, structural concerns, would-recommend-acquiring (acquire / acquire with revisions / pass). Must include a one-sentence note specifically on whether the threading delivered.

**2. Working economic historian.** Same persona as v2 — someone in the orbit of Adam Tooze, Perry Mehrling, Barry Eichengreen, Mary O'Sullivan. The v2 verdict was COMPETENT SYNTHESIS, with the Notes on Sources back-matter rated "serviceable rather than serious" and Chapters 3, 4, 5, 7, 9, 11 unrepresented. The question for this round: does the extended Notes on Sources function as serious scholarly apparatus? Does the threading deepen or erode the factual integrity of the historical claims (because adding character interiority risks fictionalizing figures whose archival record is thin)? Spot-check the new threaded material against the standard literature you know — Pepys diary on Backwell pre-1672, Briggs/Miller/Moss on Attwood's Birmingham years, Volcker's own memoir Keeping At It on the August 1971 Camp David weekend, Skidelsky on Keynes's Thornton lineage. Output: a 1,200-word essay-review in the style of Foreign Affairs or the JEL essay-review section. Verdict: original contribution / competent synthesis / not for specialists.

**3. Sympathetic heterodox reviewer in the chartalist / MMT / post-Keynesian tradition.** New persona for this round. Lineage: Stephanie Kelton, L. Randall Wray, Pavlina Tcherneva, Perry Mehrling, Daniel Carrigan, Eric Tymoigne. Has read Innes's 1913–14 essays "What is Money?" and "The Credit Theory of Money," Knapp's State Theory of Money, Lerner on functional finance, Minsky on financial fragility, and the modern MMT canon. Cares about: whether this book represents the credit-money / chartalist tradition faithfully; whether the steelmanning of opposing positions has gone so far that the book has been qualified into mush; whether the central productive-capacity thesis lands with the force its source tradition would demand; whether the policy implications are clear or have been buried under throat-clearing; whether the political economy is honest about who benefits from the orthodox framing. Will read with particular care: the Preface, Chapter 12, the Epilogue, and any MMT appendix that remains, plus the threaded chapters to see whether the threading carries the chartalist argument or whether it has become a vehicle for biographical color that obscures the analytical work. The reviewer is sympathetic to the thesis but is not a cheerleader; she will be sharp on whether the book does the tradition justice or merely imports its conclusions while soft-pedaling its arguments. Output: a 1,200-word essay-review for a publication like American Affairs, Phenomenal World, or Boston Review. Verdict at end: faithful translation / partial / too apologetic — with a one-sentence note on whether she would publicly endorse the book.

**4. Target lay reader.** New persona for this round. A 42-year-old senior product manager living in Brooklyn or San Francisco; college-educated (humanities BA from a good school); voted center-left in recent presidential elections; reads Foreign Affairs (subscribes, gets through maybe a third of each issue), listens to Odd Lots and the Ezra Klein Show, finished David Graeber's Debt and loved it, finished Adam Tooze's Crashed and loved it, finished Michael Lewis's The Big Short and loved it, started Liaquat Ahamed's Lords of Finance twice and gave up both times around the German chapters. Started Stephanie Kelton's The Deficit Myth and finished it but didn't love it. Has no formal economics training and does not want graduate-seminar exposition; has plenty of patience for long-form narrative if the writing earns it. Cares about: whether the book holds attention chapter by chapter, whether the scenes work, whether the technical passages are comprehensible without an econ background, whether the book made her think differently about something she thought she understood, whether she would recommend it to friends, whether she finished it. She is not impressed by intellectual seriousness for its own sake — books that are "important" but that she abandoned at page 80 are books she rates honestly low. Output: a long-form Goodreads review, 700–900 words, conversational and personal. Star rating out of five. She must be willing to rate it three stars or below if the book did not work for her as a reader. Include specifically: at what page or chapter she felt most engaged, at what page or chapter she most felt herself drifting, and whether she would buy a copy for a friend.

PROCESS:

Spawn all four subagents in parallel using the Agent tool with subagent_type "general-purpose." Each agent should:
- Read the manuscript files relevant to their persona's concerns. All personas read in full Chapters 3, 4, 5, 7, 8, 9, 10, 11, 12 to evaluate the threading work. The editor and the lay reader read the whole manuscript including Preface, Chapters 1–2, Epilogue, and Notes on Sources. The historian reads every chapter and the Notes on Sources with care. The heterodox reviewer reads the Preface, Chapter 12, the Epilogue, the MMT appendix if it remains, and the threaded chapters.
- Stay in voice throughout — no meta-commentary, no "as an AI."
- Be willing to be negative.
- Produce the deliverable in the format specified for that persona.

After the persona's main review, each subagent should answer this additional bestseller-tier craft question in one paragraph (~150 words):

"Setting aside platform and publisher push, which are out of the manuscript's control: is this manuscript itself at the craft level of an NYT-bestselling trade nonfiction title in this category — Ahamed's Lords of Finance, Lewis's The Big Short, Tooze's Crashed, Kelton's Deficit Myth, Graeber's Debt? If yes, what platform/marketing would unlock the bestseller outcome? If no, what specifically holds it back at the craft level?"

Once all four reviews are returned:

1. Save all four reviews plus the synthesis to /Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Reviews/PERSONA-CRITIQUES-{today's date}-v3.md.

2. Produce a synthesis at the end of that file with three components:

**Part A — Did the threading land?** Pull together what the editor and the historian say specifically about the threading work — Backwell across 3/4/5, Attwood across 7/8/9, Volcker across 10/11/12, Keynes lightly across 7/9/10. Did sustained protagonists arrive? Where did threading work, where did it fail, where did the new material feel grafted on?

**Part B — Verdict-comparison and new-persona reads.** Comparison table for editor and historian:

| Persona | v2 verdict | v3 verdict | Movement | Note |
|---------|-----------|-----------|----------|------|
| Trade nonfiction acquisitions editor | ACQUIRE WITH REVISIONS | | | |
| Working economic historian | COMPETENT SYNTHESIS | | | |

For the heterodox reviewer and the lay reader, give first verdicts plus a one-sentence summary of the key finding from each.

**Part C — Must-read tier reachable?** Final paragraph answering: did the threading move the manuscript to must-read tier, and if not, what is the highest-leverage remaining move? Specifically: is the gap that remains addressable, or does the manuscript ship as an Ahamed/Tooze-tier well-reviewed title with a 30–80k commercial ceiling rather than a Kelton/Graeber-tier breakout?
```

---

## Notes on running this

- **The prompt assumes the threading work has been done.** Do not run v3 until the chapter-by-chapter execution pass described in `Reviews/PHASE-7-EXECUTION-PLAN.md` is complete and committed.
- **The MMT-appendix decision is referenced as a placeholder.** Edit the prompt to reflect the actual choice (cut or revised) before pasting into the fresh session.
- **Four reviews, not five.** This is intentional. The skeptical economist and the conservative critic gave detailed v2 reads with verdicts unlikely to move on threading work alone; their feedback is already in hand and does not require re-running. If after v3 there is appetite for one more antagonistic read on the revised manuscript, run a single v4 economist read against Chapter 12 and the appendix specifically.
- **Be ready for the lay reader to be the loudest signal.** If the editor moves to ACQUIRE and the lay reader rates four stars or above and says she finished it, the threading worked and the bestseller path is real. If the editor moves but the lay reader did not finish, the book has crossed the gatekeeper bar without crossing the audience bar — a serious problem that no amount of further analytical revision will solve.
- **The heterodox reviewer is the new endorsement test.** A "faithful translation" verdict from this persona is the natural Kelton-tier blurber path. A "too apologetic" verdict means the steelmanning has cost the book the endorsements that move trade copies in this category.
