#!/usr/bin/env python3
"""
Count words in the book manuscript, excluding non-prose elements:
- Sources sections
- Chapter Premise statements (editorial metadata)
- Part titles (e.g., "PART I: THE ORIGINS OF CREDIT MONEY")
- Visual aids (ASCII charts, diagrams in code blocks)
- Guide posts (blockquoted Understanding Check sections)
- Pedagogical sidebars (blockquoted UNDERSTANDING MECHANISM sections)
- Data tables and metadata sections
- Organizational headers (ALL CAPS section markers)
- Footnote markers (¹, ², ³, superscript letters)
"""

import re
from pathlib import Path

def count_words_excluding_sources(file_path):
    """Count words in a markdown file, excluding non-prose elements like visual aids, guide posts, and metadata."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the position of Sources section (case-insensitive)
        # Matches patterns like "### **Sources & Further Reading**" or "## Sources"
        sources_match = re.search(r'^#{1,6}\s+\*?\*?Sources', content, re.MULTILINE | re.IGNORECASE)
        
        if sources_match:
            # Only count words before the Sources section
            content = content[:sources_match.start()]
        
        # Remove Chapter Premise sections (editorial metadata, not narrative)
        content = re.sub(r'^\*{0,2}Chapter Premise:\*{0,2}.*?(?=\n\n|\n---|\Z)', '', content, flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)
        
        # Remove Part titles (e.g., "# PART I: THE ORIGINS OF CREDIT MONEY")
        content = re.sub(r'^#\s+PART\s+[IVX]+:.*?$', '', content, flags=re.MULTILINE | re.IGNORECASE)
        
        # Remove organizational section headers (ALL CAPS headers like "FAILED FIAT SYSTEMS:")
        content = re.sub(r'^\*{0,2}[A-Z][A-Z\s]+[A-Z]:\*{0,2}\s*$', '', content, flags=re.MULTILINE)
        
        # Remove visual aids, guide posts, and pedagogical sidebars (blockquoted sections)
        # These are marked with > at the start of lines
        # Includes: Understanding Check sections, UNDERSTANDING MECHANISM sidebars, etc.
        content = re.sub(r'^>.*?(?=\n[^>]|\n*$)', '', content, flags=re.MULTILINE | re.DOTALL)
        
        # Remove code blocks (includes ASCII charts and data tables)
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        
        # Remove metadata sections (lines starting with common metadata markers)
        # Matches: *Source:, *Data Citations:, **Figure, **CHART TYPE:, **KEY PHASES:, etc.
        content = re.sub(r'^\*{1,2}(Source|Data Citation|Figure|CHART TYPE|KEY PHASES|BALANCE SHEET DATA|KEY INSIGHT|Caption|CRITICAL COMPARISONS|The Pattern|The Critical Insight|THE LESSON)[:\s].*?(?=\n\n|\n#|\Z)', '', content, flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)
        
        # Remove markdown table syntax (| and separators)
        # First remove table separator lines (---|---|---)
        content = re.sub(r'^\|?[\s\-\|:]+\|?\s*$', '', content, flags=re.MULTILINE)
        # Then remove table cell markers but keep content
        content = re.sub(r'\|', ' ', content)
        
        # Remove inline code
        content = re.sub(r'`[^`]+`', '', content)
        
        # Remove links but keep link text
        content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
        
        # Remove images completely (including alt text for charts)
        content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', content)
        
        # Remove headers markdown (but keep the text)
        content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)
        
        # Remove bold/italic markers
        content = re.sub(r'[*_]{1,3}', '', content)
        
        # Remove horizontal rules
        content = re.sub(r'^-{3,}$', '', content, flags=re.MULTILINE)
        
        # Remove footnote markers (¹, ², ³, etc. and superscript letters)
        content = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰ᵃᵇᶜᵈᵉᵍʰⁱʲ]+', '', content)
        
        # Count words (split on whitespace)
        words = content.split()
        return len(words)
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def main():
    base_path = Path("/Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Content")
    
    files = [
        "00-Preface/01-main.md",
        "01-Part-I-Origins/01-Chapter-1/01-main.md",
        "01-Part-I-Origins/02-Chapter-2/01-main.md",
        "01-Part-I-Origins/03-Chapter-3/01-main.md",
        "02-Part-II-Institutional-Revolution/04-Chapter-4/01-main.md",
        "02-Part-II-Institutional-Revolution/05-Chapter-5/01-main.md",
        "03-Part-III-Gold-Standard/06-Chapter-6/01-main.md",
        "03-Part-III-Gold-Standard/07-Chapter-7/01-main.md",
        "03-Part-III-Gold-Standard/08-Chapter-8/01-main.md",
        "03-Part-III-Gold-Standard/09-Chapter-9/01-main.md",
        "04-Part-IV-Breaking-Beyond/10-Chapter-10/01-main.md",
        "04-Part-IV-Breaking-Beyond/11-Chapter-11/01-main.md",
        "04-Part-IV-Breaking-Beyond/12-Chapter-12/01-main.md",
        "04-Part-IV-Breaking-Beyond/13-Chapter-13/01-main.md",
        "05-Epilogue/01-main.md",
    ]
    
    total_words = 0
    print("\n" + "="*70)
    print("WORD COUNT REPORT - Narrative Prose Only")
    print("Excludes: Chapter premises, visual aids, guide posts, sidebars,")
    print("          tables, metadata, organizational headers, footnotes, sources")
    print("="*70 + "\n")
    
    for file_rel_path in files:
        file_path = base_path / file_rel_path
        word_count = count_words_excluding_sources(file_path)
        total_words += word_count
        
        # Extract chapter/section name
        section_name = file_rel_path.split('/')[0]
        if 'Chapter' in file_rel_path:
            chapter_num = file_rel_path.split('/')[-2]
            print(f"{chapter_num:20s} {word_count:>8,} words")
        elif 'Preface' in file_rel_path:
            print(f"{'Preface':20s} {word_count:>8,} words")
        elif 'Epilogue' in file_rel_path:
            print(f"{'Epilogue':20s} {word_count:>8,} words")
    
    print("\n" + "-"*70)
    print(f"{'TOTAL':20s} {total_words:>8,} words")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
