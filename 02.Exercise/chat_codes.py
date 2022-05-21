number = int(input())
text = ""
for num in range(number):
    number = int(input())
    if number != 88 and number != 86 and number < 88:
        text = "GREAT!"
    elif number == 88:
        text = "Hello"
    elif number == 86:
        text = "How are you?"
    else:
        text = "Bye."
    print(text)
