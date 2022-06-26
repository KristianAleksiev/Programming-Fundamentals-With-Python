phones_list = input().split(", ")


while True:
    command = input()

    if command == "End":
        break
    else:
        action_list = command.split(" - ")
        current_action = action_list[0]
        current_phone = action_list[1]

        if current_action == "Add":
            if current_phone in phones_list:
                continue
            else:
                phones_list.append(current_phone)

        elif current_action == "Remove":
            if current_phone in phones_list:
                phones_list.remove(current_phone)
            else:
                continue

        elif current_action == "Bonus phone":
            bonus_phone = current_phone.split(":")
            current_bonus_phone = bonus_phone[1]
            current_old_phone = bonus_phone[0]

            if current_old_phone in phones_list:
                index = phones_list.index(current_old_phone)
                phones_list.insert(index + 1, current_bonus_phone)
            else:
                continue
                
        elif current_action == "Last":
            if current_phone in phones_list:
                switch_phone = phones_list.pop(phones_list.index(current_phone))
                phones_list.append(switch_phone)
            else:
                continue

print(", ".join(phones_list))
