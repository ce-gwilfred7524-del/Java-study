#!/usr/bin/env python3

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the corrupted sequences
# ''""' appears to be a corrupted checkmark
replacements = [
    ("''\"\"'", "'✓'"),  # Checkmark in single quotes
    ("''\"\" Marked done'", "'✓ Marked done'"),  # Checkmark with text
    ("''\"\" Correct!", "'✓ Correct!"),  # Checkmark with text
    ("''-‹", "'–"),  # Corrupted dash-like character
]

for old, new in replacements:
    content = content.replace(old, new)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Fixed corrupted checkmarks and dashes")
