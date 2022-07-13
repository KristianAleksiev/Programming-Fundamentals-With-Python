banned_words = input().split(", ")
input_string = input()

for word in banned_words:
    input_string = input_string.replace(word, "*" * len(word))

print(input_string)