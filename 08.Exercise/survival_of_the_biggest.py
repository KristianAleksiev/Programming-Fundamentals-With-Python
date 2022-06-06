input_list = input().split()
num_to_remove = int(input())

for _ in range(len(input_list)):
    input_list[_] = int(input_list[_])

for remove in range(num_to_remove):
    input_list.remove(min(input_list))

for numbers in range(len(input_list)):
    if numbers != len(input_list) - 1:
        print(input_list[numbers], end=", ")
    else:
        print(input_list[-1])
