numbers = input().split()
numbers_as_integers = []
for current_number in numbers:
    numbers_as_integers.append(int(current_number))

# numbers = [int(s) for s in input().split()]

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_integers))
print(result)
