#!/usr/bin/env python3
"""
Count words in the book manuscript, excluding Sources sections.
"""

import re
from pathlib import Path

def count_words_excluding_sources(file_path):
    """Count words in a markdown file, excluding everything after '## Sources' or '# Sources'."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the position of Sources section (case-insensitive)
        # Matches patterns like "### **Sources & Further Reading**" or "## Sources"
        sources_match = re.search(r'^#{1,6}\s+\*?\*?Sources', content, re.MULTILINE | re.IGNORECASE)
        
        if sources_match:
            # Only count words before the Sources section
            content = content[:sources_match.start()]
        
        # Remove markdown formatting for accurate word count
        # Remove code blocks
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        # Remove inline code
        content = re.sub(r'`[^`]+`', '', content)
        # Remove links but keep link text
        content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
        # Remove images
        content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', content)
        # Remove headers markdown
        content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)
        # Remove bold/italic markers
        content = re.sub(r'[*_]{1,3}', '', content)
        
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
        "05-Epilogue/01-main.md",
    ]
    
    total_words = 0
    print("\n" + "="*70)
    print("WORD COUNT REPORT (Excluding Sources)")
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
