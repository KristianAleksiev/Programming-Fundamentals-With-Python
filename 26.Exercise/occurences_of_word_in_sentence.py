import re

sentence = input()
searched_word = input()

searched_pattern = fr"\b{searched_word}\b"

match = re.findall(searched_pattern, sentence, flags=re.I)

length = len(match)
print(length)