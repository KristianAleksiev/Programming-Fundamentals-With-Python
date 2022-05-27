capacity = 255
number_of_lines = int(input())
liters_in_tank = 0

for _ in range(number_of_lines):
    add_liters = int(input())
    if capacity - add_liters < 0:
        print("Insufficient capacity!")
        continue
    liters_in_tank += add_liters
    capacity -= add_liters

print(liters_in_tank)
