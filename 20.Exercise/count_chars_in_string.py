symbols = "".join(s for s in input().split())
letters = {}

for letter in symbols:
    if letter not in letters: # letters.keys()
        letters[letter] = 0
    letters[letter] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")

