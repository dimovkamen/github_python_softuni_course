days_of_adventure = int(input())
number_of_players = int(input())
groups_energy = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())

water_all = days_of_adventure * number_of_players * water_per_day_for_one_person
# print(water_all)
food_all = days_of_adventure * number_of_players * food_per_day_for_one_person
# print(food_all)

for day in range(1, days_of_adventure + 1):
    energy_loss = float(input())
    groups_energy -= energy_loss

    # print(groups_energy)

    if groups_energy <= 0:
        break

    if day % 2 == 0:
        groups_energy *= 1.05   # 100% + 5%
        water_all *= 0.7        # 100% - 30% = 70%
        # print(groups_energy)
        # print(water_all)

    if day % 3 == 0:
        food_all -= food_all / number_of_players
        groups_energy *= 1.10
        # print(groups_energy)
        # print(food_all)

if groups_energy > 0:
    print(f"You are ready for the quest. You will be left with - {groups_energy :.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_all :.2f} food and {water_all :.2f} water.")
