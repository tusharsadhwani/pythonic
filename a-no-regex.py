lines = []
with open('test.html') as html:
    for index, line in enumerate(html):
        try:
            index = line.find('rgb(')
            if index == -1:
                continue

            rgb_string = line[index+4:].rstrip(');\n')
            values = rgb_string.split(',')

            # hex(int('123')) gives '0x7b', so [2:] gives '7b'
            hex_value = '#' + hex(int(values[0]))[2:] \
                            + hex(int(values[1]))[2:] \
                            + hex(int(values[2]))[2:]

            line = line[:index] + hex_value + ';\n'
        except ValueError:
            pass
        finally:
            lines.append(line)

with open('test.html', 'w') as f:
    html = f.writelines(lines)
