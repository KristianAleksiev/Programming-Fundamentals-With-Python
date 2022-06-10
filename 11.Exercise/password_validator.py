def length_is_valid(string):
    if 6 <= len(string) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def symbols_are_valid(string):
    if string.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def digits_condition(string):
    digits_counter = 0
    for char in string:
        if char.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True

    print("Password must have at least 2 digits")
    return False


password = input()

validated = [length_is_valid(password),
             symbols_are_valid(password),
             digits_condition(password)]

if all(validated):
    print("Password is valid")


