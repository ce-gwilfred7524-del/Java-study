#!/usr/bin/env python3

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find lines with unmatched brackets/parens
bracket_stack = []
paren_stack = []
issues = []

for line_num, line in enumerate(lines, 1):
    for char_num, char in enumerate(line):
        if char == '[':
            bracket_stack.append((line_num, char_num))
        elif char == ']':
            if bracket_stack:
                bracket_stack.pop()
            else:
                issues.append(f"Line {line_num}: Extra ] closing bracket")
        elif char == '(':
            paren_stack.append((line_num, char_num))
        elif char == ')':
            if paren_stack:
                paren_stack.pop()
            else:
                issues.append(f"Line {line_num}: Extra ) closing paren")

# Report unclosed brackets/parens
if bracket_stack:
    print("Unclosed square brackets:")
    for line_num, char_num in bracket_stack[-1:]:  # Show last one
        print(f"  Line {line_num}, Column {char_num}")
        print(f"  Content: {lines[line_num-1].strip()[:80]}")

if paren_stack:
    print(f"\nUnclosed parentheses: {len(paren_stack)} missing")
    # Show first few
    for line_num, char_num in paren_stack[:3]:
        print(f"  Line {line_num}, Column {char_num}")
        print(f"  Content: {lines[line_num-1].strip()[:80]}")

print(f"\nTotal issues to find:")
print(f"  Missing ] brackets: {len(bracket_stack)}")
print(f"  Extra ) that shouldn't be there: We need to find these manually")
print(f"\nOther issues found: {len(issues)}")
for issue in issues[:5]:
    print(f"  {issue}")
