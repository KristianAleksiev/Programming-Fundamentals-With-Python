import re

searched_pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
data = input()
result = re.findall(searched_pattern, data)

print(", ".join(result))