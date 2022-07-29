def store_cars(car_dict, number):
    for _ in range(number):
        data = input().split("|")
        brand = data[0]
        mileage = int(data[1])
        fuel = int(data[2])

        car_dict[brand] = [mileage, fuel]

    return car_dict


def commands(car_dict):
    while True:
        command = input()
        if command == "Stop":
            break

        command = command.split(" : ")

        current_command = command[0]
        brand = command[1]

        if current_command == "Drive":
            distance = int(command[2])
            fuel = int(command[3])

            available_fuel = car_dict[brand][1]
            current_mileage = car_dict[brand][0]

            if available_fuel < fuel:
                print("Not enough fuel to make that ride")
            else:
                car_dict[brand][1] -= fuel
                car_dict[brand][0] += distance
                print(f"{brand} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if car_dict[brand][0] >= 100000:
                del car_dict[brand]
                print(f"Time to sell the {brand}!")

        elif current_command == "Refuel":
            fuel = int(command[2])
            available_fuel = car_dict[brand][1]

            if fuel + available_fuel > 75:
                fuel = 75 - available_fuel

            car_dict[brand][1] += fuel

            print(f"{brand} refueled with {fuel} liters")

        elif current_command == "Revert":
            kilometers = int(command[2])
            current_mileage = car_dict[brand][0]

            if current_mileage - kilometers < 10000:
                car_dict[brand][0] = 10000
            else:
                car_dict[brand][0] -= kilometers
                print(f"{brand} mileage decreased by {kilometers} kilometers")

    return car_dict


def final_print(car_dict):
    for brand in car_dict:
        fuel = car_dict[brand][1]
        mileage = car_dict[brand][0]

        print(f"{brand} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


def need_for_speed(number):
    car_dictionary = {}

    store_cars(car_dictionary, number)
    commands(car_dictionary)
    final_print(car_dictionary)


num = int(input())
need_for_speed(num)


