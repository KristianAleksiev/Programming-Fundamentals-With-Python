def odd(number):
    sum_odd = 0

    for current_number in number:
        if int(current_number) % 2 != 0:
            sum_odd += int(current_number)

    return sum_odd


def even(number):
    sum_even = 0
    for current_number in number:
        if int(current_number) % 2 == 0:
            sum_even += int(current_number)
    return sum_even


num = input()
result_odd = odd(num)
result_even = even(num)

print(f"Odd sum = {result_odd}, Even sum = {result_even}")

