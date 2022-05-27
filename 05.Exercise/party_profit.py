group_size = int(input())
number_days = int(input())
coins = 0

for current_day in range(1, number_days + 1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    if current_day % 3 == 0:
        coins -= group_size * 3
    if current_day % 5 == 0:
        coins += 20 * group_size
        if current_day % 3 == 0:
            coins -= group_size * 2
    coins += 50
    coins -= group_size * 2

coins_per_group_member = int(coins / group_size)
print(f"{group_size} companions received {coins_per_group_member} coins each.")
