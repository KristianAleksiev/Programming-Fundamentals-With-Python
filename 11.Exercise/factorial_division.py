def calculate_factorial(number):
    for factorial in range(1, number):
        number *= factorial
    return number


first_integer = int(input())
second_integer = int(input())

first_number_factorial = calculate_factorial(first_integer)
second_number_factorial = calculate_factorial(second_integer)
result = first_number_factorial / second_number_factorial

print(f"{result:.2f}")

# math.factorial