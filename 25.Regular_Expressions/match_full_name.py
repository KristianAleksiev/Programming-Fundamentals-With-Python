import re

text = input()
searched_pattern = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"
result = re.findall(searched_pattern, text)

print(" ".join(result))


