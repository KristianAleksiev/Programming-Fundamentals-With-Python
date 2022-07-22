import re

searched_string = input()
searched_pattern = r"(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b"

matches = re.findall(searched_pattern, searched_string)

for match in matches:
    print(match[0])

