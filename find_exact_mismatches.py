#!/usr/bin/env python3

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Track bracket/paren stacks (excluding content in strings/templates)
bracket_stack = []
paren_stack = []
in_string = False
string_char = None
in_template = False

code_lines = []

for line_num, line in enumerate(lines, 1):
    in_string = False
    in_template = False
    i = 0
    
    while i < len(line):
        char = line[i]
        
        # Handle string literals
        if char in ('"', "'") and (i == 0 or line[i-1] != '\\'):
            if not in_template:
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
        
        # Handle template literals
        elif char == '`' and (i == 0 or line[i-1] != '\\'):
            in_template = not in_template
        
        # Track brackets/parens outside strings
        elif not in_string and not in_template:
            if char == '[':
                bracket_stack.append((line_num, i, line.strip()))
            elif char == ']':
                if bracket_stack:
                    opened = bracket_stack.pop()
                else:
                    print(f"✗ Extra ] at line {line_num}, col {i}")
                    print(f"  Context: {line.strip()[:80]}")
           elif char == '(':
                paren_stack.append((line_num, i, line.strip()))
            elif char == ')':
                if paren_stack:
                    opened = paren_stack.pop()
                else:
                    print(f"✗ Extra ) at line {line_num}, col {i}")
                    print(f"  Context: {line.strip()[:80]}")
            
        i += 1

if paren_stack:
    print(f"\n✗ Unclosed ( parentheses ({len(paren_stack)}):")
    for line_num, col, content in paren_stack[-3:]:
        print(f"  Line {line_num}, Col {col}: {content[:60]}")
