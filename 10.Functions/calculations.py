# def calculation_func(number_a, number_b, operation):
#
#     if operation == "multiply":
#         return number_a * number_b
#     elif operation == "divide":
#         return int(number_a / number_b)
#     elif operation == "add":
#         return number_a + number_b
#     elif operation == "subtract":
#         return number_a - number_b
#
#
# type_operation = input()
# first_number = int(input())
# second_number = int(input())
#
# print(calculation_func(number_a=first_number, number_b=second_number, operation=type_operation))

import operator


def calculations(number_a, number_b, operation):
    operation_dict = {
        "multiply": operator.mul,
        "divide": operator.truediv,
        "add": operator.add,
        "subtract": operator.sub
    }
    return int(operation_dict[operation](number_a, number_b))


type_operation = input()
first_number = int(input())
second_number = int(input())

print(calculations(number_a=first_number, number_b=second_number, operation=type_operation))
