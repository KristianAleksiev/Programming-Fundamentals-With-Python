import math
budget = float(input())
price_flour = float(input())

price_eggs = 0.75 * price_flour
price_milk = 1.25 * price_flour
number_of_loaves = 0
price_per_loaf = price_flour + price_eggs + price_milk / 4

number_of_eggs = 0
while budget >= price_per_loaf:
    number_of_loaves += 1
    number_of_eggs += 3
    budget -= price_per_loaf
    if number_of_loaves % 3 == 0:
        number_of_eggs -= number_of_loaves - 2

print(f"You made {int(number_of_loaves)} loaves of Easter bread!"
      f" Now you have {number_of_eggs} eggs and {budget:.2f}BGN left.")