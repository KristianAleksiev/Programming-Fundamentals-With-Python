number_list = list(map(int, input().split(", ")))

indices = [index for index in range(len(number_list)) if number_list[index] % 2 == 0]
print(indices)
