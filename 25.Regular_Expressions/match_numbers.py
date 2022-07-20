import re

numbers = input()

searched_pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

result = re.finditer(searched_pattern, numbers)  # returns objects

for number in result:
    print(number.group(), end=" ")  # returns what was found in the groups




