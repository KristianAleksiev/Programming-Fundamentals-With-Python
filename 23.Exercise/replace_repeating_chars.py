input_str = input()

chars = []

for letter in range(0, len(input_str) - 1):

    if input_str[letter] != input_str[letter + 1]:
        chars.append(input_str[letter])

chars.append(input_str[-1])

print(*chars, sep="")
