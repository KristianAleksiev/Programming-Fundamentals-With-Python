text = input()

for char in text:
    new_char = chr(ord(char) + 3)
    print(new_char, end="")