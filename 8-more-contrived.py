import re

with open('test.html') as f:
    html = f.read()

# keepends=True to make sure the \n at the end of line is kept
lines = html.splitlines(keepends=True)

for index, line in enumerate(lines):
    # Match the pattern /rgb(XYZ, XYZ, XYZ)/
    match = re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)\s*\)', line)
    if not match:
        continue

    # red, green, and blue values as strings
    values = match.groups()

    # hex(int('123')) gives '0x7b', so [2:] gives '7b'
    hex_value = '#' + hex(int(values[0]))[2:] \
                    + hex(int(values[1]))[2:] \
                    + hex(int(values[2]))[2:]

    # Replace the matched regex with hex value
    lines[index] = line[:match.start()] + hex_value + line[match.end():]

with open('test.html', 'w') as f:
    html = f.writelines(lines)
