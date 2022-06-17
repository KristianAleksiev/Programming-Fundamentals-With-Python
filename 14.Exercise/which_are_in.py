sequence_one = input().split(", ")
sequence_two = input().split(", ")

substrings = []

for first_word in sequence_one:
    for second_word in sequence_two:
        if first_word in second_word and first_word not in substrings:
            substrings.append(first_word)

print(substrings)