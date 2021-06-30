lines = []
with open('test.html') as html:
    for index, line in enumerate(html):
        try:
            index = line.find('rgb(')
            if index == -1:
                continue

            rgb_string = line[index+4:].rstrip(');\n')

            red, green, blue = (int(num) for num in rgb_string.split(','))
            hex_value = f'#{red:02x}{green:02x}{blue:02x}'

            line = line[:index] + hex_value + ';\n'
        except ValueError:
            pass
        finally:
            lines.append(line)

with open('test.html', 'w') as f:
    html = f.writelines(lines)
