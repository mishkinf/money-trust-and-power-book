# Multi-Persona Critique Prompt — v5 (Multi-Dimensional Scoring)

Self-contained prompt for use in a fresh Claude Code session. Spawns four independent persona reviewers in parallel and asks each for a multi-dimensional read with per-dimension scores, reasoning, and concrete suggestions — rather than a single-line verdict.

**Why v5 differs from v4.** The format and rubric are unchanged from v4 — the v4 design (multi-dimensional scoring, per-dimension reasoning + concrete suggestion, three highest-leverage revisions, bestseller-tier craft question, holistic blank-slate read) proved its value and is preserved. v5 is run against a manuscript state that has incorporated the convergent fix list from v4 and additional revision work; the round's job is to test whether those changes landed, but reviewers are not told what changed and read holistically. The synthesis at the end of the round will surface any movement on dimensions that v4 flagged.

**v5 reading discipline.** Reviewers read the entire manuscript end-to-end as a complete published book. No diff-thinking. No references to prior versions. No instructions about what to look for. Reviewers form their own judgments based on the manuscript as it stands. The round tests Path A *by not telling reviewers about Path A*.

**Prior critiques and findings:**
- v1: `Reviews/PERSONA-CRITIQUES-2026-04-28.md`
- v2: `Reviews/PERSONA-CRITIQUES-2026-04-28-v2.md`
- v3: `Reviews/PERSONA-CRITIQUES-2026-04-28-v3.md`
- v4: `Reviews/PERSONA-CRITIQUES-2026-04-28-v4.md`

**How to use:** copy everything inside the code block below and paste it as the first message of a fresh session. The assistant should spawn the four subagents in parallel.

---

```
I have a complete trade-nonfiction manuscript and I want a multi-dimensional persona-critique round. Four independent personas, each spawned as a separate subagent running in parallel, each producing both a native long-form review and a structured per-dimension rubric. The output of this round will feed directly into a revision pass — so I want concrete, specific, actionable feedback at the dimension level, not just verdicts.

The book is "Money, Trust, and Power: The Five-Thousand-Year Case Against the Household Budget" — a trade nonfiction title tracing money from Mesopotamian grain credits to modern fiat money and cryptocurrency. The book's central thesis: money is not a commodity but a relationship — credit recorded by institutions powerful enough to enforce it. Taxation drives currency demand. Productive capacity, not gold or accounting balances, is the real constraint on money creation. The book steelmans the Currency School, Friedman's monetarism, Buchanan-Wagner public-choice critique, Sargent-Wallace unpleasant monetarist arithmetic, Cochrane's Fiscal Theory of the Price Level, and Hayek's knowledge problem.

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
- 04-Part-IV-Breaking-Beyond/12-Chapter-12/01-main.md (Chapter 12A: The Validation)
- 04-Part-IV-Breaking-Beyond/13-Chapter-12B/01-main.md (Chapter 12B: The Tests)
- 05-Epilogue/01-main.md
- 07-Notes-on-Sources/01-main.md

**READING DISCIPLINE — applies to every persona:** Read the entire manuscript end-to-end before forming any view. Treat it as a complete, published book. Do not read for diffs, recent changes, or revision-pass signals — there is no prior version you should be comparing against, and no specific revision you are evaluating. Your review is a holistic judgment on the work as it stands. Do not score, comment on, or make suggestions about any chapter you have not read in full. The file list above is the complete book; read it from the Preface through the Notes on Sources.

I want four independent persona critiques, each spawned as a separate subagent running in parallel via the Agent tool with subagent_type "general-purpose."

============================
COMMON STRUCTURE FOR ALL FOUR PERSONAS
============================

Every reviewer must produce TWO things, in this order:

1. A long-form review in the format native to that persona (memo / essay-review / Goodreads-style review). Length specified per persona below.

2. A STRUCTURED RUBRIC, in the following exact format, appended after the long-form review. Use a markdown table.

For each dimension, score from 1 (badly broken) to 5 (publication-ceiling for the category). Half-points permitted. Each dimension requires:
- a one-sentence reasoning anchored in specific manuscript evidence (cite a chapter, scene, or page);
- a one-sentence concrete suggestion if the score is below 5 (the suggestion should be specific enough that the author could act on it without further interpretation — e.g., "cut the Overstone/Norman/Political Economy Club catalogue in Chapter 8 by ~20 pages and tell that material through Attwood's perspective" rather than "tighten Chapter 8");
- "—" in the suggestion column only if the score is exactly 5.

DIMENSIONS (every persona scores all that apply to their remit; mark "n/a" with a one-sentence reason if a dimension is genuinely outside the persona's expertise):

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

(a) **Three highest-leverage revisions, ranked.** For each: name the change in one sentence, name the chapter or scene it touches, name what tier the manuscript moves to if that change lands.

(b) **Bestseller-tier craft question:** "Setting aside platform and publisher push, which are out of the manuscript's control: is this manuscript itself at the craft level of an NYT-bestselling trade nonfiction title in this category — Ahamed's Lords of Finance, Lewis's The Big Short, Tooze's Crashed, Kelton's Deficit Myth, Graeber's Debt? If yes, what platform/marketing would unlock the bestseller outcome? If no, what specifically holds it back at the craft level?" One paragraph, ~150 words.

Reviewers should rate honestly. Do not cheerlead, but also do not pre-load critical posture. If the book is a 5 on a dimension, score it 5 and explain why.

============================
PERSONA SPECS
============================

**1. Trade nonfiction acquisitions editor at a Big 5 imprint** (Penguin Press, Norton, Crown, Knopf, Riverhead). Reading for commercial viability, comp titles, target reader, hook strength, length, structure, sustained protagonists, and editorial conditions of acquisition. Read the entire manuscript including Preface, Epilogue, and Notes on Sources. Long-form deliverable: an internal acquisitions memo, 800–1,000 words, with sections (Book in one paragraph / Target reader / Marketing hooks / Structural concerns / Editorial conditions / Recommendation). Native verdict at end: acquire / acquire with revisions / pass. Score all dimensions in the rubric; commercial viability is your home dimension.

**2. Working economic historian** in the orbit of Adam Tooze, Perry Mehrling, Barry Eichengreen, Mary O'Sullivan. Reading for historiographic faithfulness, factual accuracy, scholarly apparatus, and whether the manuscript advances or merely synthesizes the literature. Read the entire manuscript with care, especially the Notes on Sources. Spot-check at least three of the manuscript's specific historical claims against the standard literature you know — for example: Pepys diary on Backwell pre-1672; Briggs/Miller/Moss on Attwood's Birmingham years; Volcker's memoir Keeping At It on the August 1971 Camp David weekend; Skidelsky on Keynes's Thornton lineage; Steil vs. Helleiner on Bretton Woods; Hudson vs. Van De Mieroop on Mesopotamian credit. Long-form deliverable: a 1,200-word essay-review in the style of Foreign Affairs or the JEL essay-review section. Native verdict at end: original contribution / competent synthesis / not for specialists. Score all dimensions; scholarly apparatus and originality are your home dimensions.

**3. Sympathetic heterodox reviewer in the chartalist / MMT / post-Keynesian credit-money tradition.** Lineage: Stephanie Kelton, L. Randall Wray, Pavlina Tcherneva, Perry Mehrling, Daniel Carrigan, Eric Tymoigne. Has read Innes's 1913–14 essays, Knapp's State Theory of Money, Lerner on functional finance, Minsky on financial fragility, and the modern MMT canon. Reading for: faithfulness to the source tradition; whether steelmanning has hedged the argument into mush; whether productive-capacity lands with the force its source tradition demands; whether policy implications are clear or buried; whether the political economy is honest about who benefits from the orthodox framing. Read in full: the Preface, all chapters, the Epilogue, and the Notes on Sources. Long-form deliverable: a 1,200-word essay-review for a publication like American Affairs, Phenomenal World, or Boston Review. Native verdict at end: faithful translation / partial / too apologetic, plus a one-sentence note on whether you would publicly endorse the book. Score all dimensions; faithfulness to source tradition and policy clarity are your home dimensions.

**4. Target lay reader.** A 42-year-old senior product manager living in Brooklyn or San Francisco; humanities BA from a good school; voted center-left in recent presidential elections; subscribes to Foreign Affairs (gets through about a third of each issue), listens to Odd Lots and the Ezra Klein Show. Reading history: finished and loved Graeber's Debt, Tooze's Crashed, and Lewis's The Big Short; gave up twice on Ahamed's Lords of Finance around the German chapters; finished Kelton's The Deficit Myth without loving it. No formal economics training. Plenty of patience for long-form narrative when the writing earns it. Read the entire manuscript. Long-form deliverable: a Goodreads review, 700–900 words, conversational and personal, with a star rating out of five (half stars permitted). The review should describe the actual reading experience — where you leaned in, where you leaned out, what surprised you, whether you'd recommend it and to whom. Rate honestly. Score all dimensions in the rubric that you can speak to as a non-specialist reader; engagement curve and audience fit are your home dimensions; mark scholarly apparatus and faithfulness-to-source-tradition n/a if you cannot speak to them.

============================
PROCESS
============================

Spawn all four subagents in parallel using the Agent tool with subagent_type "general-purpose." Each agent should:
- **Read the entire manuscript end-to-end before forming any view.** This is a holistic review of the book as a complete work, not an evaluation of any revision or recent change. Read every chapter, the Preface, the Epilogue, and the Notes on Sources from start to finish before writing a single line of the review.
- Do not score, comment on, or make suggestions about any chapter not read in full.
- Stay in voice throughout — no meta-commentary, no "as an AI," no preamble.
- Produce the two-part deliverable described above (long-form review + structured rubric + the two follow-up structured questions).

Once all four reviews are returned:

1. Save all four reviews plus the synthesis to /Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Reviews/PERSONA-CRITIQUES-{today's date}-v5.md.

2. Produce a synthesis at the end of that file with four components:

**Part A — Dimension-level heat map.** Build a single combined table aggregating all four reviewers' scores per dimension (or n/a). Highlight the dimensions with the lowest median score across the bench, the dimensions with the widest spread (high disagreement), and the dimensions all four reviewers agree are at ceiling.

**Part B — Convergent fix list.** Pull together the "three highest-leverage revisions" lists from all four reviewers. Where two or more reviewers independently name the same revision, that is high-confidence signal. List the convergent items first (with which reviewers named them), then unique items per reviewer. For each convergent item, name the chapter or scene it touches and the manuscript-tier movement it would unlock.

**Part C — Native verdicts.** Restate each persona's native verdict (acquire / pass; original contribution / competent synthesis / not for specialists; faithful / partial / too apologetic; star rating) with a one-sentence summary of the key finding driving the verdict.

**Part D — Tier diagnosis.** Final paragraph answering: where does this manuscript currently sit on the tier ladder (broken draft / publishable / well-reviewed / must-read / breakout), and what is the highest-leverage revision pass that would move it up one tier? Distinguish craft fixes (addressable by revision) from strategic trade-offs (which require an author decision rather than a manuscript change).
```

---

## Notes on running this

- **The prompt is a near-clone of v4 by design.** The format, rubric, persona specs, and reading discipline are intentionally preserved so v5 results are directly comparable to v4 along every dimension. The only substantive changes from v4 are the round number and the manuscript title.
- **No diff-signaling.** Reviewers are not told what Path A was, what changed, or where to look. They read the manuscript as a complete published book. The synthesis will reveal whether the v4 convergent fix list has been addressed, by comparison.
- **The rubric is the operative output.** The long-form reviews give voice and texture; the rubric gives an actionable diff list. When synthesizing, the rubric is what feeds revision.
- **Half-star ratings and half-point scores are intentional.** Half-points are the smallest granularity that distinguishes genuine improvement from noise.
- **Watch for the heterodox / lay reader pull-apart.** Earlier rounds surfaced a strategic tension: the heterodox path (sharper forcing argument, restored policy clarity) and the establishment-credible path (steelmanning intact, balance preserved) are not jointly satisfiable. v5 will expose whether the manuscript has shifted that trade-off — but the trade-off itself is an author decision, not a manuscript craft fix.
