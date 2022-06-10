def is_perfect(number):
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    if number == sum:
        return "We have a perfect number!"

    return "It's not so perfect."


random_number = int(input())

print(is_perfect(random_number))
