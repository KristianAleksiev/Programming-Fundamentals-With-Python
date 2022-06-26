total_tax = 0
input_cars_list = input().split(">>")

for current_element in range(len(input_cars_list)):
    current_list_of_cars = (input_cars_list[current_element].split())

    car_type = current_list_of_cars[0]
    years = current_list_of_cars[1]
    kilometers = current_list_of_cars[2]
    tax = 0

    if car_type == "family":
        tax = int(kilometers) // 3000 * 12 + (50 - int(years) * 5)
        total_tax += tax
        print(f"A family car will pay {tax:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        tax = int(kilometers) // 9000 * 14 + (80 - int(years) * 8)
        total_tax += tax
        print(f"A heavyDuty car will pay {tax:.2f} euros in taxes.")
    elif car_type == "sports":
        tax = int(kilometers) // 2000 * 18 + (100 - int(years) * 9)
        total_tax += tax
        print(f"A sports car will pay {tax:.2f} euros in taxes.")

    else:
        print(f"Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")









