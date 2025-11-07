# PROMPT-11 Implementation Status: Add Human Stories

**Date:** December 2024  
**Status:** Research Phase - Generating Deep Research Prompts

---

## Research Inventory Summary

### ✅ EXISTING HUMAN STORIES (Already Documented in Research Folder)

#### **Excellent - Ready to Use:**
1. **Harry Todd** - British coal miner 1926 General Strike (Boldon Colliery, Durham)
   - File: `Human Cost of Monetary Orthodoxy.md` + `The Human Cost of the Gold Standard Collapse.md`
   - Documentation: HIGH - Full census records, family archives, wage data
   - Use: Chapter 10 (already has coal miner stories)

2. **Dean & Kaye Hagedorn** - Iowa farmers destroyed by Volcker's 21% interest rates (1982)
   - File: `Volcker Recession Victim.md`
   - Documentation: HIGH - Diary entries, PBS documentary, $18,000 interest payments, $94,000 seized
   - Use: Could supplement Chapter on Volcker era

3. **Dale Burr** - Iowa farmer foreclosure leading to 1985 tragedy
   - File: `Volcker Recession Victim.md`
   - Documentation: HIGH - $500,000 debt, specific creditor names, full book documentation
   - Use: Alternative Volcker story

4. **Donald Hartwell** - Nebraska Dust Bowl farmer with 5-year diary
   - File: `The Human Cost of the Gold Standard Collapse.md`
   - Documentation: HIGH - Personal diary at Nebraska Historical Society
   - Use: Chapter 10 Depression section

#### **Good - Usable with Notes:**
5. **Barbara Kantor** - 2008 credit freeze (Vedante Corporation, Boulder)
   - File: `Monetary History Vignettes.md`
   - Documentation: MEDIUM-HIGH - PBS NewsHour interview, some detail gaps
   - Use: Modern financial crisis example

6. **Samuel Gigney** - 1821 deflation farmer bankruptcy (Essex)
   - File: `Farmers Who Suffered During the 1821-1824 Deflation.md`
   - Documentation: MEDIUM - Name verified, needs archival research for full details
   - Use: Early gold standard return chapter

7. **Fulk Basset** - Medieval Bishop with surviving tally stick (1250s)
   - File: `Monetary History Vignettes.md`
   - Documentation: HIGH - Physical artifact survives, full biographical data
   - Use: Medieval credit system chapter

---

## ❌ MISSING STORIES (Per PROMPT-11 Requirements)

### 1. German Family During 1923 Hyperinflation ⚠️ NOT FOUND
**Need:** 300-400 words showing daily price increases, wages paid twice daily, wheelbarrows of currency

**Research Status:**
- `Hyperinflation - Real collapse precedes money printing.md` has EXTENSIVE data on Weimar (timeline, exchange rates, economic data)
- `Human Cost of Monetary Orthodoxy.md` has Weimar mechanics BUT NO NAMED FAMILY
- **GAP:** No individual German family identified with names and personal details

**What We Have:**
- Timeline: Mark went from 7.9/dollar (1918) → 4.2 trillion/dollar (Nov 1923)
- Bread costs: 160 marks (end 1922) → 200 billion marks (late 1923)
- Ruhr occupation January 1923 as trigger
- 98% of government spending from printing by Oct 1923

**What We Need:**
- Named German family (ideally with archival documentation)
- Personal diary entries or memoirs showing daily experience
- Specific examples: shopping in morning vs. afternoon, wage payment schedules

### 2. French Worker During Gold Standard Depression 1931-1936 ✅ PARTIAL FOUND
**Need:** 250-300 words on unemployment, wage cuts, political radicalization

**Research Status:**
- `Human Cost of Monetary Orthodoxy.md` Line 187: **Morvan Lebesque account of winter 1932-33**
- "Thousands of young men, forced out of their jobs by the crisis, struggled on to their last penny... groups of exhausted and starving young men would be trying not to die"
- French unemployment data: ~1 million (1934-35), sustained through 1939

**What We Have:**
- Morvan Lebesque (Breton journalist) - named individual with quote
- Industrial production fell 20% below 1929, never recovered before WWII
- Wage-price squeeze, credit crunch
- Political radicalization: Feb 6, 1934 riots, Popular Front, factory occupations 1936

**What We Need:**
- MORE detail on Lebesque's personal experience (age, family, job loss timeline)
- OR alternative named French industrial worker with fuller documentation
- Specific factory closures, union involvement, wage cut percentages

### 3. Japanese Worker During Lost Decades 1990s-2020s ⚠️ NOT FOUND
**Need:** 200-250 words on lifetime employment ending, salaryman unemployment, deflation psychology

**Research Status:**
- `Hyperinflation - Real collapse precedes money printing.md` has Japan macro data (deflation 1995-2013, BOJ QE)
- BUT NO NAMED INDIVIDUAL Japanese worker story

**What We Have:**
- 18 years deflation (1995-2013), averaging -0.3% annually
- BOJ balance sheet 125% of GDP
- "Lost generation" phenomenon mentioned
- Elderly hoarding cash despite zero interest

**What We Need:**
- Named Japanese salaryman or industrial worker
- Personal story: company layoff, age discrimination, shift to contract work
- Family impact: children's education, home purchase deferred
- Psychological impact of perpetual deflation

---

## NEXT STEPS: Claude Deep Research Required

### Priority 1: German Hyperinflation Family (HIGHEST PRIORITY)
**Research Approach:**
- Search for published German memoirs/diaries 1923-1924 (many exist, need English translations)
- Check academic sources: Adam Fergusson's *When Money Dies* (1975) likely has cases
- Stefan Zweig, *The World of Yesterday* for middle-class perspective
- Victor Klemperer diaries (though he's more about Nazi era)
- German newspapers digitized archives (if accessible)

**Ideal Find:**
- Middle-class family (professional father, housewife mother, children)
- Specific dates of shopping trips with price documentation
- Named individual (even if family pseudonym used in memoir)

### Priority 2: Expand French Story
**Research Approach:**
- Deep dive on Morvan Lebesque: dates of birth/death, journalism career, specific unemployment dates
- French unemployment statistics by sector (textiles, steel, mining)
- Search for translated French Depression memoirs
- Check if any "Popular Front" oral history projects exist

**Ideal Find:**
- Full biographical details on Lebesque OR
- Alternative named French factory worker with union involvement

### Priority 3: Japanese Lost Decades Worker
**Research Approach:**
- English-language books on Japanese economy crisis (Richard Katz, Richard Werner)
- Japanese business press coverage (Nikkei, translated)
- Academic papers on "lost generation" employment
- Documentary films about Japanese economy (NHK documentaries if accessible)

**Ideal Find:**
- Salaryman in 40s-50s laid off in late 1990s
- Specific company name, severance package details
- Family decisions about children's education

---

## CLAUDE DEEP RESEARCH PROMPTS

See attached file: `PROMPT-11-CLAUDE-RESEARCH-PROMPTS.md`

---

## IMPLEMENTATION NOTES

**Decision Rules (from PROMPT-11):**
- Only add stories where research is available OR can be quickly verified
- DO NOT invent details or use fictional characters
- Time estimate: 4-6 hours research + 3-4 hours writing = 7-10 hours total
- Success metric: 2-3 human stories (minimum 600 words total)

**Current Assessment:**
- French story: CAN implement now with Morvan Lebesque + aggregate data (250 words achievable)
- German & Japanese: NEED Claude deep research first
- Alternative: Focus on stories we HAVE (Todd, Hagedorn, Hartwell) and skip these gaps

**Recommendation:**
1. Run Claude deep research for all 3 missing stories
2. If research yields named individuals: implement all 3
3. If research incomplete: implement French only, defer German/Japanese for future edition
