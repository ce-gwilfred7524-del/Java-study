#!/usr/bin/env python3

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all corrupted quote patterns with a dash
import re

# Remove all instances of ''  (corrupted sequences)
content = re.sub(r"''[\"]?", "-", content)

# Remove any remaining corrupted patterns
content = re.sub(r"[\"][\']", "-", content)

# Fix the arrow-like corrupted sequences
content = content.replace("'†'", "→")
content = content.replace("'†", "→")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ All corrupted sequences cleaned")
