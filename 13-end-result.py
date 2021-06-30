def hexify():
    with open('test.html') as html, open('output.html', 'w') as out:
        for index, line in enumerate(html):
            try:
                index = line.find('rgb(')
                if index == -1:
                    continue

                rgb_values = line[index+4:].rstrip(');\n')

                red, green, blue = (int(num) for num in rgb_values.split(','))
                hex_value = f'#{red:02x}{green:02x}{blue:02x}'
                line = line[:index] + hex_value + ';\n'
            except ValueError:
                pass
            finally:
                out.write(line)


if __name__ == '__main__':
    hexify()
