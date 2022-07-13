# + - Concatenate
# * - Repeats the string
# Slicing

# Getting input from a few lines all together
def multiline_input(text):
    print(text)
    multi_input = ""
    while True:
        string = input()
        if string != "":
            multi_input += string + " "
        else:
            break
    return multi_input
