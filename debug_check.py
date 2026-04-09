from pathlib import Path
text = Path('index.html').read_text(encoding='utf8')
start = text.find('// Note: ^ in Java is XOR')
if start == -1:
    print('marker not found')
    raise SystemExit
slice_start = max(0, start-40)
slice_end = min(len(text), start+120)
print(repr(text[slice_start:slice_end]))
print('---')
print(text[slice_start:slice_end])
