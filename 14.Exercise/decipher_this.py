messages = input().split()

final_message = []

for word in messages:
    number = ""
    current_message = ""

    for char in word:
        if char.isdigit():
            number += char
        else:
            break

    word = word.replace(number, "")
    number = int(number)
    current_message += chr(number)

    if len(word) >= 2:
        word = word[-1] + word[1:-1] + word[0]
    current_message += word
    final_message.append(current_message)

print(" ".join(final_message))
