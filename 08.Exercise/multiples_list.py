factor = int(input())
count = int(input())
completed_list = []

for multiplier in range(1, count + 1):
    completed_list.append(factor * multiplier)

print(completed_list)
