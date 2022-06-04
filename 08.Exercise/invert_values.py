list_numbers = input().split()
# opposite_numbers = []

# for element in list_numbers:
#     opposite_numbers.append(-int(element))
#
# print(opposite_numbers)

list_numbers = [-int(number) for number in list_numbers]
print(list_numbers)
