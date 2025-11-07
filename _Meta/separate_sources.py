#!/usr/bin/env python3
"""
Separate sources sections from chapter main files.
"""
import re
import os
from pathlib import Path

def find_sources_section(content):
    """Find where sources section starts."""
    # Look for common patterns
    patterns = [
        r'\n---\n\n### \*\*Chapter Summary\*\*',
        r'\n---\n\n### \*\*Sources',
        r'\n---\n\n### \*\*Notes\*\*',
        r'\n---\n\n### \*\*Further Reading\*\*'
    ]
    
    earliest_match = None
    earliest_pos = len(content)
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match and match.start() < earliest_pos:
            earliest_pos = match.start()
            earliest_match = match
    
    if earliest_match:
        # Return position of the --- before the section
        return earliest_match.start()
    return None

def process_chapter(chapter_path):
    """Process a single chapter."""
    main_file = chapter_path / '01-main.md'
    if not main_file.exists():
        return False
        
    content = main_file.read_text()
    
    # Find sources section
    split_pos = find_sources_section(content)
    if split_pos is None:
        print(f"  No sources section found in {chapter_path.name}")
        return False
    
    # Split content
    narrative = content[:split_pos].rstrip() + '\n'
    sources = content[split_pos+5:].lstrip()  # Skip the first ---\n\n
    
    # Write sources file
    sources_file = chapter_path / 'sources.md'
    chapter_num = chapter_path.name.split('-')[0]
    
    # Add header to sources
    sources_content = f"# Chapter {chapter_num} Sources & Summary\n\n{sources}"
    sources_file.write_text(sources_content)
    
    # Update main file
    main_file.write_text(narrative)
    
    print(f"  ✓ Processed {chapter_path.name}")
    return True

# Main execution
base_path = Path("/Users/mishkinfaustini/workspace/Money, Trust, and Power Book/Content")

chapters_to_process = [
    "02-Part-II-Institutional-Revolution/04-Chapter-4",
    "02-Part-II-Institutional-Revolution/05-Chapter-5",
    "03-Part-III-Gold-Standard/06-Chapter-6",
    "03-Part-III-Gold-Standard/07-Chapter-7",
    "03-Part-III-Gold-Standard/08-Chapter-8",
    "03-Part-III-Gold-Standard/09-Chapter-9",
    "04-Part-IV-Breaking-Beyond/10-Chapter-10",
    "04-Part-IV-Breaking-Beyond/11-Chapter-11",
    "04-Part-IV-Breaking-Beyond/12-Chapter-12",
    "04-Part-IV-Breaking-Beyond/13-Chapter-13",
]

print("Processing chapters...")
for chapter_path_str in chapters_to_process:
    chapter_path = base_path / chapter_path_str
    process_chapter(chapter_path)

# Handle Epilogue separately
print("\nProcessing Epilogue...")
epilogue_path = base_path / "05-Epilogue"
epilogue_file = epilogue_path / "01-main.md"
content = epilogue_file.read_text()

# For epilogue, find the Notes section
match = re.search(r'\n---\n\n### \*\*Notes\*\*', content)
if match:
    narrative = content[:match.start()].rstrip() + '\n'
    sources = content[match.start()+5:].lstrip()
    
    # Write sources
    sources_file = epilogue_path / 'sources.md'
    sources_file.write_text(f"# Epilogue Sources\n\n{sources}")
    
    # Update main file
    epilogue_file.write_text(narrative)
    print("  ✓ Processed Epilogue")
else:
    print("  Could not find Notes section in Epilogue")

print("\nDone!")
