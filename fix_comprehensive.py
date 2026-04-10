#!/usr/bin/env python3

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The corrupted sequences that need fixing
corrupted_replacements = [
    # These are the corrupted patterns from the failed encoding fixes
    ("Q1''\"8", "Q1–8"),  # Should be Q1 to 8
    ("Q10''\"20", "Q10–20"),  # Should be Q10 to 20
    ("Q14''\"16", "Q14–16"),  # Should be Q14 to 16
    ("Q26''\"35", "Q26–35"),  # Should be Q26 to 35
    ("Q37''\"39", "Q37–39"),  # Should be Q37 to 39
    ("Q37''\"50", "Q37–50"),  # Should be Q37 to 50
    ("Q51''\"60", "Q51–60"),  # Should be Q51 to 60
    ("Q18,21,22,25 MCQ 2025. Section B Q20''\"", "Q18,21,22,25 MCQ 2025. Section B Q20–"),   
    
    # Fix the dashes/separators
    ("developers ''\"", "developers –"),
    (" ''\"", " –"),  # Standalone corrupted sequence
    ("True or False?''\"", "True or False? –"),
    ("false ''\"", "false –"),
    ("true ''\"", "true –"),
    ("'B' ''\"", "'B' –"),
    ("'55' ''\"", "'55' –"),
    ("'0' ''\"", "'0' –"),
    ("conversion ''\"", "conversion –"),
    
    # Fix the corrupted arrow sequences
    ("'†'", "→"),  # Corrupted arrow
]

for old, new in corrupted_replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Fixed: {old[:30]}... -> {new[:30]}...")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ All corrupted sequences fixed")
