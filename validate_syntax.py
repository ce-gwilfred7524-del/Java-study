#!/usr/bin/env python3
import json
import re

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check basic syntax issues
issues = []

# Count brackets/braces/parens
open_braces = content.count('{')
close_braces = content.count('}')
open_brackets = content.count('[')
close_brackets = content.count(']')
open_parens = content.count('(')
close_parens = content.count(')')

print("Bracket/Brace/Paren counts:")
print(f"  {{ = {open_braces}, }} = {close_braces} | Match: {'✓' if open_braces == close_braces else '✗'}")
print(f"  [ = {open_brackets}, ] = {close_brackets} | Match: {'✓' if open_brackets == close_brackets else '✗'}")
print(f"  ( = {open_parens}, ) = {close_parens} | Match: {'✓' if open_parens == close_parens else '✗'}")

# Check for DATA object
if 'const DATA = {' in content:
    print("\n✓ DATA object found")
else:
    print("\n✗ DATA object NOT found")
    issues.append("Missing 'const DATA = {'")

# Check for closing of DATA
data_match = re.search(r'const DATA = \{.*?\};', content, re.DOTALL)
if data_match:
    print("✓ DATA object properly closed with };")
else:
    print("✗ DATA object NOT properly closed")
    issues.append("DATA object not properly closed")

# Look for common quote mismatch patterns
single_quotes = content.count("'")
double_quotes = content.count('"')
print(f"\nQuote counts:")
print(f"  Single quotes: {single_quotes}")
print(f"  Double quotes: {double_quotes}")

# Check for UTF-8 encoded characters (these are OK, just informational)
utf8_dashes = content.count('–') + content.count('—')
print(f"\nUTF-8 content:")
print(f"  Em/En dashes found: {utf8_dashes}")
print(f"  File encoding: UTF-8")

if issues:
    print("\n⚠ Issues found:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("\n✓ No major syntax issues detected!")

# Check file size
print(f"\nFile size: {len(content)} characters")
print(f"Lines: {len(content.splitlines())}")
