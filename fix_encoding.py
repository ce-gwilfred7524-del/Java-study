#!/usr/bin/env python3
import re

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace smart quotes and special characters
replacements = [
    ('\u2018', "'"),  # Left single quotation mark
    ('\u2019', "'"),  # Right single quotation mark  
    ('\u201C', '"'),  # Left double quotation mark
    ('\u201D', '"'),  # Right double quotation mark
    ('\u2013', '-'),  # En dash
    ('\u2014', '-'),  # Em dash
]

for original, replacement in replacements:
    content = content.replace(original, replacement)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Fixed all encoding issues")
