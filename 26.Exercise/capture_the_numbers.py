import re

searched_pattern = "\d+"

line = input()

while True:
    if line:
        match = re.findall(searched_pattern, line)
        if match:
            print(' '.join(match), end=" ")

        line = input()
    else:
        break


