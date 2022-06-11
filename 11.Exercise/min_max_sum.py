sequence_list = [int(digit) for digit in (input().split())]

min_int = min(sequence_list)
max_int = max(sequence_list)
sum_sequence = sum(sequence_list)

print(f"The minimum number is {min_int}")
print(f"The maximum number is {max_int}")
print(f"The sum number is: {sum_sequence}")