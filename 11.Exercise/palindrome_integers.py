def palindrome(sequence):
    for element in sequence:
        if element == element[::-1]:
            print("True")
        else:
            print("False")


sequence_input = input().split(", ")
palindrome(sequence_input)