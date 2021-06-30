import re

lines = []
with open('test.html') as html:
    for index, line in enumerate(html):
        # Match the pattern /rgb(XYZ, XYZ, XYZ)/
        match = re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)\s*\)', line)
        if not match:
            lines.append(line)
            continue

        # red, green, and blue values as strings
        values = match.groups()

        # hex(int('123')) gives '0x7b', so [2:] gives '7b'
        hex_value = '#' + hex(int(values[0]))[2:] \
                        + hex(int(values[1]))[2:] \
                        + hex(int(values[2]))[2:]

        # Replace the matched regex with hex value
        lines.append(line[:match.start()] + hex_value + line[match.end():])

with open('test.html', 'w') as f:
    html = f.writelines(lines)
