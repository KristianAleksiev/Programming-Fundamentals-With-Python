text = input()

for index in range(len(text)):
    emoticon = ":"

    if text[index] == ":":
        emoticon += text[index + 1]
        print(emoticon)