import re

valid_urls = []
searched_pattern = r"(w{3})\.([A-Za-z0-9]+)(\-[A-Za-z0-9]+)*(\.[a-z]+)+"

searched_sentence = input()

while searched_sentence:
    matches = re.search(searched_pattern, searched_sentence)

    if matches:
        valid_urls.append(matches.group(0))

    searched_sentence = input()

[print(x) for x in valid_urls]

