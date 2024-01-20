days = int(input())
room_type = input()
evaluation = input()

nights = days - 1
discount = 0
holiday_price = 0

if room_type == "room for one person":
    holiday_price = 18 * nights
elif room_type == "apartment":
    if 0 < nights < 10:
        holiday_price = (25 * nights) * 0.70
    elif nights < 15:
        holiday_price = (25 * nights) * 0.65
    elif nights >= 15:
        holiday_price = (25 * nights) * 0.50
elif room_type == "president apartment":
    if 0 < nights < 10:
        holiday_price = (35 * nights) * 0.90
    elif nights < 15:
        holiday_price = (35 * nights) * 0.85
    elif nights >= 15:
        holiday_price = (35 * nights) * 0.80

if evaluation == "positive":
    holiday_price = holiday_price * 1.25
elif evaluation == "negative":
    holiday_price = holiday_price * 0.9

print(f"{holiday_price :.2f}")
