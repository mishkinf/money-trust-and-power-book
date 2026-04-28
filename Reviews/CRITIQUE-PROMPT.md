# Multi-Persona Critique Prompt

Self-contained prompt for use in a fresh Claude Code session. Spawns five independent subagent reviewers in parallel to surface honest critique of the manuscript before sending it out for endorsements or to publishers.

**How to use**: copy everything inside the code block below and paste it as the first message of a fresh session. The assistant should spawn the five subagents in parallel.

---

```
I have a complete trade-nonfiction manuscript I want critiqued from multiple independent perspectives before sending it out for endorsement or to publishers. The book is "Money, Trust, and Power: Five Thousand Years of Credit, Crisis, and the Institutions That Make Money Work" — roughly 67,000 words across 12 chapters tracing money from Mesopotamian grain credits to modern fiat money and cryptocurrency.

The manuscript lives at:
/Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Content/

Structure:
- 00-Preface/01-main.md
- 01-Part-I-Origins/01-Chapter-1/01-main.md (The Birth of Credit)
- 01-Part-I-Origins/02-Chapter-2/01-main.md (Merchants of Trust)
- 01-Part-I-Origins/03-Chapter-3/01-main.md (The Sovereign's Dilemma)
- 02-Part-II-Institutional-Revolution/04-Chapter-4/01-main.md (When Private Money Failed)
- 02-Part-II-Institutional-Revolution/05-Chapter-5/01-main.md (The Bank of England Solution — includes new Paterson set piece)
- 03-Part-III-Gold-Standard/06-Chapter-6/01-main.md (Newton's Accident)
- 03-Part-III-Gold-Standard/07-Chapter-7/01-main.md (Paper Proves Itself)
- 03-Part-III-Gold-Standard/08-Chapter-8/01-main.md (The Great Forgetting — merged Currency School/Bank Charter Act 1844)
- 04-Part-IV-Breaking-Beyond/09-Chapter-9/01-main.md (The Interwar Catastrophe)
- 04-Part-IV-Breaking-Beyond/10-Chapter-10/01-main.md (Bretton Woods and the Bancor That Wasn't)
- 04-Part-IV-Breaking-Beyond/11-Chapter-11/01-main.md (The Breaking of Bretton Woods)
- 04-Part-IV-Breaking-Beyond/12-Chapter-12/01-main.md (The Age of Pure Fiat)
- 05-Epilogue/01-main.md
- 06-Glossary/glossary.md

The book's central thesis: money is not a commodity but a relationship — credit recorded by institutions powerful enough to enforce it. Taxation drives currency demand. Productive capacity, not gold or accounting balances, is the real constraint on money creation. The book steelmans the Currency School, Friedman's monetarism, Buchanan-Wagner public-choice critique, Sargent-Wallace unpleasant monetarist arithmetic, and Cochrane's Fiscal Theory of the Price Level — engaging them seriously rather than dismissing them.

I want five independent persona critiques, each spawned as a separate subagent running in parallel. Each subagent should read the relevant chapters and produce a substantive review IN VOICE. Critical: each persona must be willing to give a negative review if the book deserves one. I am not looking for cheerleading. I want to find out what's wrong before a real reviewer does.

PERSONAS:

**1. NYT Book Review staff reviewer.** General-intelligent-reader perspective. Has read Ahamed's *Lords of Finance*, Graeber's *Debt*, Kelton's *Deficit Myth*, Tooze's *Crashed*, Lewis's *The Big Short*. Cares about: narrative momentum, character work, prose quality, novelty of argument, whether it earns its scope. Output: a 1,200–1,500 word review in NYT style. Verdict at the end: strong recommend / qualified recommend / mixed / don't recommend, with one-sentence pull quote.

**2. Skeptical mainstream economist.** In the lineage of Larry Summers, Olivier Blanchard, John Cochrane, Ken Rogoff. Suspicious of MMT and the productive-capacity framework. Will scrutinize whether the steelman of orthodox positions is genuine or strawmanned, whether the Volcker treatment fairly engages alternatives, whether the 2021–22 inflation analysis honestly weighs supply vs demand factors, whether the public-choice critique gets a real reply. Output: a 1,200-word critique focused on intellectual fairness and analytical rigor, citing specific passages from specific chapters. Verdict: serious / partial / unserious treatment of opposing views.

**3. Trade nonfiction acquisitions editor at a Big 5 imprint** (Penguin Press, Norton, Crown, Knopf, Riverhead). Cares about: commercial viability, comp titles, target reader, hook strength, author platform requirements, length, structure. Output: an internal acquisitions memo, 800–1,000 words. Sections: book in one paragraph, comps, target reader, marketing hooks, structural concerns, would-recommend-acquiring (yes / yes-with-revisions / pass).

**4. Conservative / libertarian / sound-money critic.** Reader of Rothbard, Hayek, Friedman; sympathetic to gold standard, hostile to MMT. Will test whether the book engages cryptocurrency, the gold standard, the Austrian school fairly or whether the steelman is performative. Will also test whether the Volcker chapter unfairly disparages the policy that broke the inflation. Output: a 1,000-word review for a publication like *Reason*, *Cato Journal*, or *National Review*. Verdict at end.

**5. Working economic historian.** Someone like Adam Tooze, Perry Mehrling, Barry Eichengreen, Mary O'Sullivan. Cares about: factual accuracy, source quality, treatment of secondary literature, novelty of historical claims vs synthesis, footnote rigor. Will spot-check claims against the standard literature. Output: a 1,200-word essay-review in the style of *Foreign Affairs* or *Journal of Economic Literature* (essay-review section). Verdict: original contribution / competent synthesis / not for specialists.

PROCESS:

Spawn all five subagents in parallel using the Agent tool with subagent_type "general-purpose" (or "feature-dev:code-explorer" if available). Each agent should:
- Read the manuscript files relevant to their persona's concerns (the economist will want chapters 7, 8, 11, 12; the editor needs the whole; the conservative needs 12 plus the cryptocurrency section; the historian needs every chapter for fact-checking; the NYT reviewer needs the whole thing).
- Stay in voice throughout — no meta-commentary, no "as an AI."
- Be willing to be negative. The point of doing five persona reviews is to surface what each kind of reader will find weak.
- Produce the deliverable in the format specified for that persona.

Once all five reviews are returned, give me a synthesis: where do the personas agree, where do they diverge, and what are the highest-priority issues to address before sending the manuscript out?
```

---

## Notes on running this

- **Parallelism is the point**: in the fresh session, the assistant should make all five Agent tool calls in a single message, not serially. Independence requires that no persona has seen another's review.
- **Each persona reads different chapters**. That's intentional. The acquisitions editor reads end-to-end; the historian reads everything for fact-checking; the conservative critic focuses on Ch.12 plus the cryptocurrency section; the skeptical economist focuses on Chs.7, 8, 11, 12.
- **The synthesis at the end matters more than any individual review.** Where three out of five personas flag the same issue, that's strong signal. Where one is harshly negative and four are positive, you can weigh that one against the rest.
- **Be ready for harsh feedback.** If the prompt works, the conservative critic and the skeptical economist should land real punches. If every review comes back glowing, the prompt isn't strong enough — push back on the next session's assistant to make the personas bite harder.
- **Save the outputs.** Reviews/PERSONA-CRITIQUES-[date].md is a sensible place to drop the five reviews plus the synthesis once they come back.
