text = ""

while text != "End":
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue
    new_text = ""
    for char in text:
        new_text += char + char
    print(new_text)
