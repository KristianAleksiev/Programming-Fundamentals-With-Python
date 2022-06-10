def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract(first, second, third):
    sum_of_first_and_second = sum_numbers(first, second)
    result = subtract(sum_of_first_and_second, third)
    return result


first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

print(add_and_subtract(first_integer, second_integer, third_integer))
