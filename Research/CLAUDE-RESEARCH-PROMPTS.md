# Claude Deep Research Prompts for Visual Graphics Data

These research prompts are designed for Claude with deep research capabilities to find citable (and write out the sources in Chicago style), academic-quality data for manuscript graphics.

---

## PROMPT 1: Federal Reserve Balance Sheet Quarterly Data (2007-2023)

**Research Request:**

I need quarterly Federal Reserve balance sheet data from 2007-2023 for a chart showing monetary expansion during financial crises. Please find and compile:

**Required Data Points:**
- Federal Reserve total assets ($ billions or trillions) for end of each quarter or year: Dec 2007, Dec 2008, Dec 2009, Dec 2010, Dec 2012, Dec 2014, Dec 2016, Dec 2019, March 2020, Dec 2020, June 2022, Dec 2022
- Corresponding US nominal GDP for each period
- Calculate: Fed assets as % of GDP for each data point

**Sources to Consult:**
1. Federal Reserve Statistical Release H.4.1 "Factors Affecting Reserve Balances of Depository Institutions and Condition Statement of Federal Reserve Banks" (archived weekly releases)
2. Federal Reserve Bank of St. Louis FRED database (series: WALCL - All Federal Reserve Banks: Total Assets)
3. Bureau of Economic Analysis GDP data (nominal GDP, quarterly)
4. Federal Reserve Bank historical data archives

**Citation Requirements:**
- Provide exact date of H.4.1 release for each data point
- Include FRED series identifiers
- Note any methodology changes in Fed reporting 2008-2023
- Distinguish between: Total Assets, Treasury Securities, Mortgage-Backed Securities holdings
- Chicago-style citations with page numbers

**Verification:**
- Cross-check against: Stella, Peter (2009) IMF Working Paper on Fed balance sheet
- Verify 2008-2014 data matches: "Fed assets grew from $891B (Dec 2007) to $4.5T (Oct 2014)"
- Confirm COVID expansion: approximately $4.2T (Dec 2019) to $8.9T (June 2022)

**Output Format:**
```
DATE | FED TOTAL ASSETS | US NOMINAL GDP | ASSETS % GDP | SOURCE (H.4.1 release date)
```

---

## PROMPT 2: Gold Standard Adoption Dates by Country (1717-1900)

**Research Request:**

I need country-by-country dates for gold standard adoption 1717-1900, including formal legal adoption dates and de facto implementation dates where they differ. list sources using Chicago-style citations with page numbers.

**Required Information for Each Country:**

**Core Countries:**
1. Britain (both 1717 "accidental" via Newton, and 1821 formal resumption)
2. Germany (post-unification 1871)
3. United States (1873 "Crime of 1873" de facto, 1900 Gold Standard Act de jure)
4. France (abandonment of bimetallism, 1870s)
5. Japan (Meiji era adoption, 1890s)
6. Russia (1890s adoption)
7. Austria-Hungary (1890s adoption)

**Additional Countries if data available:**
- Latin Monetary Union countries (France, Belgium, Italy, Switzerland) - individual dates
- Scandinavian countries (Sweden, Norway, Denmark)
- Netherlands
- Spain
- Portugal
- India (British colonial policy)
- Argentina, Brazil (Latin American attempts)
- Canada (as British dominion)

**Data Needed for Each:**
- Date of adoption (month and year if available)
- Type: De facto vs. de jure; formal legislation vs. market practice
- Motivation: Economic integration, access to London capital, competitive pressure, colonial policy
- Source legislation name if applicable
- Whether adoption was successful or abandoned

**Key Sources to Consult:**
1. Eichengreen, Barry. *Golden Fetters* (1992) - Chapter on gold standard spread
2. Bordo, Michael D. "The Classical Gold Standard: Some Lessons for Today" (Federal Reserve Bank of St. Louis Review, 1981)
3. Officer, Lawrence H. "Gold Standard" in *EH.net Encyclopedia*
4. Flandreau, Marc & Jobst, Clemens. "The Ties That Divide: A Network Analysis of the International Monetary System, 1890–1910" (Journal of Economic History, 2005)
5. League of Nations. *International Currency Experience* (1944)

**Special Attention:**
- Newton's 1717 mint ratio error in Britain (guinea revaluation)
- Germany's 1871 adoption triggering cascade
- "Crime of 1873" US silver demonetization debate
- Distinction between gold standard and gold-exchange standard

**Output Format:**
```
COUNTRY | ADOPTION DATE | TYPE | LEGISLATION/EVENT | MOTIVATION | SOURCE
```

---

## PROMPT 3: Chapter 7 Price Index Construction (1790-1824)

**Research Request:**

I need a comprehensive price index or multiple price series for Britain 1790-1824 to show inflation during Bank Restriction (1797-1821) vs. deflation after gold resumption (1821-1824). Make sure to use Chicago-style citations with page numbers.

**Required Data:**
- General price index (1790=100 baseline) for years 1790, 1795, 1797, 1800, 1805, 1810, 1815, 1818, 1821, 1822, 1823, 1824
- OR multiple commodity price indices that can be averaged
- Wheat prices per quarter (already have: 1813=108s, 1822=45s, need intermediate years)
- Any available Gayer-Rostow-Schwartz index data
- Wholesale price data if available

**Known Verified Data (to cross-check):**
- Cumulative inflation 1797-1815: approximately 22.3% (from research file)
- Wheat: 108s/quarter (1813) → 45s/quarter (1822), 58% decline
- General price level returned to approximately 1790 levels by 1824

**Sources to Consult:**
1. Gayer, Arthur D., W.W. Rostow, and Anna J. Schwartz. *The Growth and Fluctuation of the British Economy, 1790-1850* (1953)
2. Mitchell, B.R. *British Historical Statistics* (1988) - Price indices
3. Clark, Gregory. "The Condition of the Working-Class in England, 1209-2003" (JPE 2005) - includes price series
4. O'Brien, Patrick K. & Palma, Nuno. "Danger to the Old Lady: Bank Restriction Act and Regime Shift to Paper Money" (European Review of Economic History, 2020)
5. Bank of England "A millennium of macroeconomic data" spreadsheet

**Methodological Notes Needed:**
- Which commodities/goods included in any composite index
- Whether index is wholesale, retail, or mixed
- Urban vs. rural price differences if relevant
- How wartime distortions (blockades, etc.) affected specific goods

**Output Format:**
```
YEAR | PRICE INDEX (1790=100) | WHEAT (s/quarter) | MONETARY REGIME | NOTES | SOURCE
```

---

## PROMPT 4: Bretton Woods & Triffin Dilemma Quantitative Data

**Research Request:**

I need quantitative data for potential Bretton Woods/Triffin Dilemma visualization (if we decide to add this graphic):

**Required Data:**
1. US gold reserves (metric tons or $ value): 1944, 1950, 1955, 1960, 1965, 1970, 1971
2. US dollar liabilities held abroad: same years
3. Ratio: foreign dollar claims / US gold reserves
4. Major events: Marshall Plan disbursements, Korean War, Vietnam War costs

**Key Relationship to Document:**
- Triffin's prediction: gold reserves declining while dollar liabilities rising
- Crossover point where foreign dollar claims exceeded US gold backing
- Nixon's decision (August 15, 1971) when ratio became unsustainable

**Sources to Consult:**
1. Triffin, Robert. *Gold and the Dollar Crisis* (1960)
2. IMF *International Financial Statistics* - historical series
3. Federal Reserve historical data on gold stock
4. Bordo, Michael D. "The Bretton Woods International Monetary System" (various papers)
5. Eichengreen, Barry. *Globalizing Capital* (2008 edition)

**Output Format:**
```
YEAR | US GOLD (metric tons) | FOREIGN $ CLAIMS ($B) | RATIO | KEY EVENTS | SOURCE
```

---

## RESEARCH METHODOLOGY GUIDELINES

**For All Prompts:**

1. **Primary Sources Priority**: Government statistical releases, central bank archives, IMF/World Bank data
2. **Peer-Reviewed Verification**: Cross-check against academic journals (JEH, EEH, JPE, QJE)
3. **Citation Format**: Full Chicago-style citations with page numbers
4. **Data Confidence Levels**: Note any interpolations, estimates, or uncertain figures
5. **Methodology Notes**: Document how historical data was constructed/estimated
6. **Multiple Source Verification**: Confirm numbers appear in at least 2 independent sources when possible

**Red Flags to Watch:**
- Round numbers (often estimated rather than measured)
- Data that conflicts between sources (note discrepancies, explain likely cause)
- Gaps in time series (interpolation may be needed—make this explicit)
- Methodology changes mid-series (note break points)

**When Data Is Unavailable:**
- State explicitly what was searched and not found
- Suggest reasonable estimation methods if applicable
- Recommend whether graphic should be modified or placeholder maintained

---

## OUTPUT DELIVERABLES

For each research prompt, please provide:

1. **Data Table**: Clean, copy-pasteable format matching requested structure
2. **Source List**: Full citations for all data sources used
3. **Methodology Notes**: Brief explanation of how data was compiled/calculated
4. **Confidence Assessment**: High/Medium/Low for each data point
5. **Discrepancies**: Note any conflicting sources and resolution method
6. **Limitations**: Any caveats about data quality, gaps, or interpretation

**File Naming Convention:**
- `FED-Balance-Sheet-Data-2007-2023.md`
- `Gold-Standard-Adoption-Dates.md`
- `Britain-Price-Index-1790-1824.md`
- `Bretton-Woods-Triffin-Data.md`

Save completed research files in: `/Research/additional/[filename]`
