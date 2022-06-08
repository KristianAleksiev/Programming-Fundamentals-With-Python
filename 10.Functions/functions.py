# Functions overview
    # Splits large problems into small pieces
    # Better organization of the program
    # Improves code readability and understandability
    # Avoiding code repeating
    # Code reusability

# Declaring and invoking functions

# def function_name(parameter: type):
#     statement(s)

# Recursion
def countdown(number):
    """DOCSTRING"""
    print(number)
    if number == 0:
        return
    else:
        countdown(number - 1)


print(countdown.__doc__)
countdown(5)

# Return values
# =============================================
# Parameters vs Arguments- positional, keyword

#Paramenter - defining the variable in the function
#Argument - The actual value of the parameter, that we pass in the function

# =============================================
# Lambda functions
# anonymous one-time function
# x = lambda a: a + 10
# print(x(5)) => 15

x = lambda a, b, c: a + b + c
print(x(3, 6, 7))


# ============================================
# def even_or_odd_number(num):
#     if num % 2 == 0:
#         return "Even number"
#     else:
#         return "Odd number"
#
#
# number = int(input())
# even_or_odd_number(number)
# numbers = [1, 3, 5, 6, 7, 11]
#
#
# def check_numbers(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# result = list(filter(check_numbers, numbers)) - filter, something to filter(data)
# print(result)
# ===========================================
#map() - Елемент по елемент
# numbers = list(map(int, input().split(", ")))


numbers = [4, 2, 8, 6, 10]


def squared_numbers(number):
    return number * number


squared_numbers = list(map(squared_numbers, numbers))
sorted_numbers = sorted(squared_numbers)
print(sorted_numbers)
