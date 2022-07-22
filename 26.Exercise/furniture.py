import re

searched_pattern = r">{2}([A-Za-z]+)<<(\d+\.?\d*)\!(\d+)"

total_sum = 0
furniture = []

command = input()

while command != "Purchase":
    match = re.search(searched_pattern, command)

    if match:
        furniture_current, price, quantity = match.groups()
        furniture.append(furniture_current)
        total_sum += float(price) * int(quantity)

    command = input()

print("Bought furniture:")

for current_item in furniture:
    print(current_item)

print(f"Total money spend: {total_sum:.2f}")
