#!/usr/bin/env python3

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read as bytes
with open(file_path, 'rb') as f:
    content = f.read()

# Replace UTF-8 encoded smart characters
# These are the literal byte sequences
replacements = [
    (b'\xe2\x80\x98', b"'"),  # Left single quotation mark
    (b'\xe2\x80\x99', b"'"),  # Right single quotation mark  
    (b'\xe2\x80\x9c', b'"'),  # Left double quotation mark
    (b'\xe2\x80\x9d', b'"'),  # Right double quotation mark
    (b'\xe2\x80\x93', b'-'),  # En dash
    (b'\xe2\x80\x94', b'-'),  # Em dash
    (b'\xc3\xa2\xc2\x80\x94', b'-'),  # Malformed em dash
    (b'\xc3\xa2\xc2\x80\x9c', b'"'),  # Malformed left quote
    (b'\xc3\xa2\xc2\x80\x9d', b'"'),  # Malformed right quote
]

for original, replacement in replacements:
    content = content.replace(original, replacement)

# Write back
with open(file_path, 'wb') as f:
    f.write(content)

print("✓ Fixed encoding at byte level")
