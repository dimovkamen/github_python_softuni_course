budget = float(input())
season = input()

percent = 0
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        percent = 30
    elif season == "winter":
        percent = 70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        percent = 40
    elif season == "winter":
        percent = 80
elif budget > 1000:
    destination = "Europe"
    percent = 90

if destination == "Europe":
    place = "Hotel"
else:
    if season == "summer":
        place = "Camp"
    elif season == "winter":
        place = "Hotel"

holiday_cost = budget * (percent/100)

print(f"Somewhere in {destination}")
print(f"{place} - {holiday_cost :.2f}")
