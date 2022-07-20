import re

searched_pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"  # \2 - Same as group 2 divider must be used

text = input()

result = re.findall(searched_pattern, text)

for element in result:
    print(f"Day: {element[0]}, Month: {element[2]}, Year: {element[3]}")
