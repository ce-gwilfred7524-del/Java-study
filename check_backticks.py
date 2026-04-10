#!/usr/bin/env python3

file_path = r"c:\Users\kyeib\Desktop\Java study\script_temp.js"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check backticks (template literals)
backtick_count = 0
issues = []

for line_num, line in enumerate(lines, 1):
    backtick_count_in_line = line.count('`')
    backtick_count += backtick_count_in_line
    
    # If odd number, likely unclosed
    if backtick_count_in_line % 2 != 0:
        issues.append(f"Line {line_num}: Odd backtick count ({backtick_count_in_line}) - Total so far: {backtick_count}")

print(f"Total backticks: {backtick_count}")
print(f"Expected: even number (every template must close)")

if backtick_count % 2 != 0:
    print(f"\n⚠ ODD number of backticks! Missing closing backtick somewhere")
    print("\nLines with odd backtick counts:")
    for issue in issues[:20]:
        print(f"  {issue}")
