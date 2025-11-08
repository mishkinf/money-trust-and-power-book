# Editorial Prompt: Add Understanding Checks to Chapters 11-12

## Objective
Add 2-3 Understanding Check boxes to Chapters 11 and 12 to help readers navigate the book's most conceptually dense material (Bretton Woods architecture and Triffin dilemma mechanics).

## Background
The manuscript currently has 4 Understanding Checks distributed across 13 chapters:
- [UC-1] Chapter 1: Taxation drives currency demand
- [UC-8] Chapter 8: Deflation's wealth transfer mechanism
- [UC-9] Chapter 9: Bank Charter Act's deposit oversight failure
- [UC-13] Chapter 13: Productive capacity constraint (concert hall analogy)

Chapters 11-12 contain the book's most complex economic concepts but lack these pedagogical aids. The editorial evaluation identified this as a minor revision that would improve reader comprehension without requiring new research.

## Specific Placements

### Understanding Check 11.1: Bancor vs. Dollar System Comparison
**Location:** Chapter 11, after the detailed exposition of Keynes's bancor proposal and before White's dollar-centered alternative (~page 168-180 range in current draft)

**Purpose:** Crystallize the fundamental architectural difference between the two proposals so readers can follow the conference politics that follow.

**Content Parameters:**
- Use two-column comparison table format (like existing UC boxes)
- Contrast: reserve currency (bancor = multilateral; dollar = US unilateral), adjustment burden (bancor = symmetrical; dollar = asymmetrical), power distribution, crisis vulnerability
- Draw ONLY from content already in Chapter 11 and existing research file `Bretton Woods Conference Quantitative Data.md`
- Keep to 150-200 words maximum
- Maintain neutral analytical tone (avoid "Keynes was right" framing)

**Citation Requirements:**
All factual claims must be sourced from:
- `Content/04-Part-IV-Breaking-Beyond/11-Chapter-11/sources.md` (existing citations)
- `Research/Bretton Woods Conference Quantitative Data.md`
- `Research/Bretton Woods & Triffin Dilemma Quantitative Data for Visualization (1944-1971).md`

If new data points are needed, FLAG FOR RESEARCH rather than inventing.

---

### Understanding Check 11.2: The Triffin Dilemma Explained
**Location:** Chapter 11, immediately after first mention of Triffin dilemma and before historical timeline of how it played out (~page 190-195 range)

**Purpose:** Ensure readers grasp the mathematical inevitability before seeing Nixon Shock as culmination (Chapter 12).

**Content Parameters:**
- Use the "designated driver" analogy if it appears in Chapter 11; otherwise use simple arithmetic example
- Format as step-by-step logic:
  1. World needs dollars for trade → US must run deficits
  2. Running deficits → more dollar liabilities than gold reserves
  3. More liabilities than gold → convertibility promise becomes incredible
  4. Incredible promise → eventual breakdown (1971)
- Maximum 200 words
- Include visual reference: "[See Visual Aid 11.1 for arithmetic]"

**Citation Requirements:**
Draw from existing content in Chapter 11-12 and:
- `Research/Bretton Woods & Triffin Dilemma Quantitative Data for Visualization (1944-1971).md`
- Existing Chapter 11 sources.md citations for Triffin's original formulation

---

### Understanding Check 12.1: Why Countries Couldn't Just Abandon Gold (Optional - if space permits)
**Location:** Chapter 12, after documenting de Gaulle's gold offensive and London Gold Pool collapse, before Nixon's decision (~page 220-225 range)

**Purpose:** Answer the likely reader question "Why didn't they just agree to end gold convertibility earlier?" 

**Content Parameters:**
- Explain the credibility trap: abandoning gold looks like admitting the dollar is weak
- International politics: other countries wanted gold option as leverage over US
- Domestic politics: "sound money" ideology made gold abandonment politically costly
- Maximum 150 words
- Conclude: "Nixon's unilateral closure was inevitable once the arithmetic became impossible"

**Citation Requirements:**
Draw from:
- Chapter 12 existing content on political resistance to ending gold
- `Research/Bretton Woods & Triffin Dilemma Quantitative Data for Visualization (1944-1971).md`
- Chapter 12 sources.md

**Flag for Research If Needed:**
If existing research doesn't contain sufficient political context for why gold convertibility persisted 1965-1971 despite obvious unsustainability, note: "ADDITIONAL RESEARCH NEEDED: Political economy of why Bretton Woods partners resisted gold window closure 1965-1971."

---

## Format Specifications

Match existing Understanding Check format exactly:

```markdown
### [UNDERSTANDING-CHECK-11]

**[Clear headline summarizing the concept]**

[Body text explaining the concept using tables, numbered lists, or analogies as appropriate]

---
```

## Quality Standards

1. **Accessibility:** Written for smart general readers, not economists
2. **Brevity:** 150-200 words maximum (existing UCs average 180 words)
3. **Visual clarity:** Use formatting (bold, numbered lists, tables) to aid scanning
4. **Source discipline:** Every factual claim must trace to existing research files or chapter sources.md
5. **No new claims:** If content requires research beyond existing files, FLAG rather than proceeding

## Implementation Steps

1. Review Chapter 11-12 current text to identify exact placement points
2. Review cited research files to confirm all necessary data exists
3. Draft Understanding Checks using ONLY existing research
4. Add source citations to Chapter 11/12 sources.md files using existing citation format
5. If gaps identified, create "RESEARCH NEEDED" note specifying what's missing

## Success Criteria

- Readers can grasp Triffin dilemma mechanics without re-reading Chapter 11 multiple times
- Understanding Checks feel like clarification aids, not redundant repetition
- No unsourced factual claims introduced
- Total addition: ~400-500 words across 2-3 boxes
