def shoot(index, power, targets):
    if 0 <= index < len(targets):
        if targets[index] - power <= 0:
            targets.pop(index)
        else:
            targets[index] -= power
    return targets


def add(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def strike(index, radius, targets):
    validator_index = index - radius >= 0 and index + radius < len(targets)
    if validator_index:
        start_target_index = index - radius
        end_target_index = index + radius
        targets = [targets[i] for i in range(len(targets)) if i < start_target_index or i > end_target_index]
    else:
        print("Strike missed!")
    return targets


def moving_targets(targets):
    while True:

        command = input()
        if command == "End":
            print("|".join([str(num) for num in targets]))
            break

        command = command.split()
        current_command = command[0]
        first_element = int(command[1])
        second_element = int(command[2])

        if current_command == "Shoot":
            targets = shoot(first_element, second_element, targets)
        elif current_command == "Add":
            targets = add(first_element, second_element, targets)
        elif current_command == "Strike":
            targets = strike(first_element, second_element, targets)


data = list(map(int, input().split()))
moving_targets(data)
