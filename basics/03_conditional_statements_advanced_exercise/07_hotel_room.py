month = input()
days = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < days <= 14:
        studio_price = studio_price * 0.95
    elif days > 14:
        studio_price = studio_price * 0.7
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if days > 14:
        studio_price = studio_price * 0.80
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if days > 14:
    apartment_price = apartment_price * 0.9

print(f"Apartment: {apartment_price * days :.2f} lv.")
print(f"Studio: {studio_price * days :.2f} lv.")
