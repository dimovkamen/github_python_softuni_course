budget = int(input())
season = input()
fisherman_count = int(input())
boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fisherman_count <= 6:
    boat_rent *= 0.90
elif 6 < fisherman_count <= 11:
    boat_rent *= 0.85
elif fisherman_count >= 12:
    boat_rent *= 0.75

if fisherman_count % 2 == 0 and not season == "Autumn":
    boat_rent *= 0.95

diff = budget - boat_rent
if diff >= 0:
    print(f"Yes! You have {abs(diff):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva.")
