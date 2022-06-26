needed_experience = int(input())
count_of_battles = int(input())

exp_gain = 0
battle_count = 0
successful = False

for current_battle in range(1, count_of_battles + 1):

    experience = int(input())

    if current_battle % 3 == 0:
        experience *= 1.15
    elif current_battle % 5 == 0:
        experience *= 0.90

    exp_gain += experience
    battle_count += 1

    if exp_gain >= needed_experience:
        successful = True
        break

if successful:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")

else:
    diff = needed_experience - exp_gain
    print(f"Player was not able to collect the needed experience, {diff:.2f} more needed.")