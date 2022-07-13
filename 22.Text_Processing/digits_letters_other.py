text = input()
letters = ""
digits = ""
others = ""

for letter in text:
    if letter.isalpha():
        letters += letter
    elif letter.isdigit():
        digits += letter
    else:
        others += letter

print(digits)
print(letters)
print(others)
