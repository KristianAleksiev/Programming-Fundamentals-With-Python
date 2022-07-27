def create_plants_data(plants, number):
    for _ in range(number):
        data = input().split("<->")
        plant_name = data[0]
        rarity = int(data[1])

        if plant_name not in plants:
            plants[plant_name] = {"rarity": rarity, "rating": []}
        else:
            plants[plant_name]["rarity"] += rarity

    return plants


def additional_plants_data(plants):
    while True:
        command = input().split(": ")

        if command[0] == "Exhibition":
            break

        data = command[1].split(" - ")
        type_of_command = command[0]
        plant = data[0]

        if plant not in plants:
            print("error")
            continue

        if type_of_command == "Rate":
            rating = int(data[1])
            plants[plant]["rating"].append(rating)

        elif type_of_command == "Update":
            new_rarity = int(data[1])
            plants[plant]["rarity"] = new_rarity

        elif type_of_command == "Reset":
            plants[plant]["rating"].clear()

    return plants


def print_func(plants):
    print("Plants for the exhibition:")

    for dict_element in plants:
        if len(plants[dict_element]["rating"]) > 0 and sum(plants[dict_element]["rating"]) > 0:
            average_rating = sum(plants[dict_element]["rating"]) / len(plants[dict_element]["rating"])
        else:
            average_rating = 0

        rarity = plants[dict_element]["rarity"]
        print(f"- {dict_element}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def plant_discovery(number):
    plants = {}

    create_plants_data(plants, number)
    additional_plants_data(plants)
    print_func(plants)


num = int(input())

plant_discovery(num)
