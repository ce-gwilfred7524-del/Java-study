#!/usr/bin/env python3
import re

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove strings and template literals first
# This is tricky - we need to remove strings without removing code syntax

# Strategy: find all strings/templates and replace with placeholders
content_cleaned = content

# Remove template literals
content_cleaned = re.sub(r'`[^`]*`', 'TEMPLATE', content_cleaned, flags=re.DOTALL)

# Remove single-quoted strings
content_cleaned = re.sub(r"'[^']*'", 'STRING', content_cleaned)

# Remove double-quoted strings  
content_cleaned = re.sub(r'"[^"]*"', 'STRING', content_cleaned)

# Now count brackets/  parens
open_brackets = content_cleaned.count('[')
close_brackets = content_cleaned.count(']')
open_parens = content_cleaned.count('(')
close_parens = content_cleaned.count(')')

print("After removing strings and templates:")
print(f"  [ = {open_brackets}, ] = {close_brackets} | Match: {'✓' if open_brackets == close_brackets else '✗'}")
print(f"  ( = {open_parens}, ) = {close_parens} | Match: {'✓' if open_parens == close_parens else '✗'}") 

if open_brackets != close_brackets:
    print(f"\n  Missing: {abs(open_brackets - close_brackets)} {'closing ]' if open_brackets > close_brackets else 'opening ['}")

if open_parens != close_parens:
    print(f"  Extra: {abs(open_parens - close_parens)} {'closing )' if open_parens < close_parens else 'opening ('}")
