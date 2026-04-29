# Multi-Persona Critique Prompt — v6 Current Manuscript

Use this prompt for a fresh, blank-slate review of the current manuscript after the five-of-five revision pass. Reviewers should not compare against prior versions or previous reviews.

```
I have a complete trade-nonfiction manuscript and I want a multi-dimensional persona-critique round. Four independent personas, each spawned as a separate subagent running in parallel, each producing both a native long-form review and a structured per-dimension rubric. The output of this round will feed directly into a revision pass, so I want concrete, specific, actionable feedback at the dimension level, not just verdicts.

The book is "Money, Trust, and Power: The Five-Thousand-Year Case Against the Household Budget" — a trade nonfiction title tracing money from Mesopotamian grain credits to modern fiat money and cryptocurrency. The book's central thesis: money is not a commodity but a relationship — credit recorded by institutions powerful enough to enforce it. Taxation drives currency demand. Productive capacity, not gold or accounting balances, is the real constraint on money creation. The book steelmans the Currency School, Friedman's monetarism, Buchanan-Wagner public-choice critique, Sargent-Wallace unpleasant monetarist arithmetic, Cochrane's Fiscal Theory of the Price Level, and Hayek's knowledge problem.

The manuscript lives at:
/Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Content/

Current structure:
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
- 04-Part-IV-Breaking-Beyond/12-Chapter-12/01-main.md (The Tests)
- 05-Epilogue/01-main.md
- 07-Notes-on-Sources/01-main.md

READING DISCIPLINE — applies to every persona: Read the entire manuscript end-to-end before forming any view. Treat it as a complete, published book. Do not read for diffs, recent changes, or revision-pass signals. There is no prior version you should compare against, and no specific revision you are evaluating. Your review is a holistic judgment on the work as it stands. Do not score, comment on, or make suggestions about any chapter you have not read in full.

COMMON STRUCTURE FOR ALL FOUR PERSONAS

Every reviewer must produce two things, in this order:

1. A long-form review in the format native to that persona.
2. A structured rubric in the exact format below, appended after the long-form review.

For each dimension, score from 1 (badly broken) to 5 (publication-ceiling for the category). Half-points permitted. Each dimension requires:
- a one-sentence reasoning anchored in specific manuscript evidence;
- a one-sentence concrete suggestion if the score is below 5;
- "—" in the suggestion column only if the score is exactly 5.

| Dimension | What it measures |
|---|---|
| Thesis force | Is the central argument legible, load-bearing, and felt — not just stated |
| Narrative momentum | Does the reader keep going chapter to chapter; is there a propulsive spine |
| Character & scene craft | Do figures inhabit the page; do set pieces have weight |
| Structural coherence | Do chapters fit together; are transitions earned; is the arc shaped |
| Prose quality | Sentence-level writing — voice, rhythm, precision, freshness |
| Originality / contribution | What does this add to the genre / the literature / the public conversation |
| Scholarly apparatus | Notes on Sources, factual accuracy, historiographic engagement |
| Audience fit | Does this work for its intended reader at its intended length |
| Commercial viability | Hook strength, comp titles, marketability, target-reader pull |
| Faithfulness to source tradition | Does the book represent its intellectual lineage faithfully or only import its conclusions |
| Policy clarity | Are the implications of the analysis stated clearly or buried in hedging |
| Engagement curve | Where the reader leans in, where the reader leans out — describe the actual reading experience |

After the rubric, every persona must answer two additional structured questions:

(a) Three highest-leverage revisions, ranked. For each: name the change in one sentence, name the chapter or scene it touches, name what tier the manuscript moves to if that change lands.

(b) Bestseller-tier craft question: "Setting aside platform and publisher push, which are out of the manuscript's control: is this manuscript itself at the craft level of an NYT-bestselling trade nonfiction title in this category — Ahamed's Lords of Finance, Lewis's The Big Short, Tooze's Crashed, Kelton's Deficit Myth, Graeber's Debt? If yes, what platform/marketing would unlock the bestseller outcome? If no, what specifically holds it back at the craft level?" One paragraph, about 150 words.

PERSONA SPECS

1. Trade nonfiction acquisitions editor at a Big 5 imprint. Reading for commercial viability, comp titles, target reader, hook strength, length, structure, sustained protagonists, and editorial conditions of acquisition. Long-form deliverable: internal acquisitions memo, 800-1,000 words, with sections Book in one paragraph / Target reader / Marketing hooks / Structural concerns / Editorial conditions / Recommendation. Native verdict at end: acquire / acquire with revisions / pass.

2. Working economic historian in the orbit of Adam Tooze, Perry Mehrling, Barry Eichengreen, Mary O'Sullivan. Reading for historiographic faithfulness, factual accuracy, scholarly apparatus, and whether the manuscript advances or merely synthesizes the literature. Spot-check at least three specific historical claims against the standard literature you know. Long-form deliverable: 1,200-word essay-review in the style of Foreign Affairs or the JEL essay-review section. Native verdict at end: original contribution / competent synthesis / not for specialists.

3. Sympathetic heterodox reviewer in the chartalist / MMT / post-Keynesian credit-money tradition. Lineage: Stephanie Kelton, L. Randall Wray, Pavlina Tcherneva, Perry Mehrling, Daniel Carrigan, Eric Tymoigne. Reading for faithfulness to the source tradition, whether steelmanning has hedged the argument into mush, whether productive capacity lands with force, whether policy implications are clear or buried, and whether the political economy is honest about who benefits from orthodox framing. Long-form deliverable: 1,200-word essay-review for a publication like American Affairs, Phenomenal World, or Boston Review. Native verdict at end: faithful translation / partial / too apologetic, plus whether you would publicly endorse the book.

4. Target lay reader. A 42-year-old senior product manager living in Brooklyn or San Francisco; humanities BA from a good school; voted center-left in recent presidential elections; subscribes to Foreign Affairs, listens to Odd Lots and the Ezra Klein Show. Reading history: finished and loved Graeber's Debt, Tooze's Crashed, and Lewis's The Big Short; gave up twice on Ahamed's Lords of Finance around the German chapters; finished Kelton's The Deficit Myth without loving it. Long-form deliverable: Goodreads review, 700-900 words, conversational and personal, with a star rating out of five. Native review should describe where you leaned in, where you leaned out, what surprised you, and whether you'd recommend it.

Once all four reviews are returned:

1. Save all four reviews plus the synthesis to:
/Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Reviews/PERSONA-CRITIQUES-2026-04-29-v6-current.md

2. Produce a synthesis at the end of that file with:
- Part A — Dimension-level heat map.
- Part B — Convergent fix list.
- Part C — Native verdicts.
- Part D — Tier diagnosis: where the manuscript currently sits on the tier ladder (broken draft / publishable / well-reviewed / must-read / breakout), and what highest-leverage revision pass would move it up one tier. Distinguish craft fixes from strategic trade-offs.
```
