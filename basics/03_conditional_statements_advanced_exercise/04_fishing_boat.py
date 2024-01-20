# Вход
# От конзолата се четат три реда:
# •	Бюджет на групата - цяло число;
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари - цяло число.
# Изход
# На конзолата да се отпечата следното:
# •	Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

budget = int(input())
season = input()
fisherman_count = int(input())
boat_rent = 0

if season == "Spring":
    if fisherman_count <= 6:
        boat_rent = 3000 * 0.90
    elif 6 < fisherman_count <= 11:
        boat_rent = 3000 * 0.85
    elif fisherman_count >= 12:
        boat_rent = 3000 * 0.75
elif season == "Summer" or season == "Autumn":
    if fisherman_count <= 6:
        boat_rent = 4200 * 0.90
    elif 6 < fisherman_count <= 11:
        boat_rent = 4200 * 0.85
    elif fisherman_count >= 12:
        boat_rent = 4200 * 0.75
elif season == "Winter":
    if fisherman_count <= 6:
        boat_rent = 2600 * 0.90
    elif 6 < fisherman_count <= 11:
        boat_rent = 2600 * 0.85
    elif fisherman_count >= 12:
        boat_rent = 2600 * 0.75

if fisherman_count % 2 == 0 and not season == "Autumn":
    boat_rent = boat_rent * 0.95

if boat_rent <= budget:
    remaining = budget - boat_rent
    print(f"Yes! You have {remaining:.2f} leva left.")
else:
    not_enough = boat_rent - budget
    print(f"Not enough money! You need {not_enough:.2f} leva.")
