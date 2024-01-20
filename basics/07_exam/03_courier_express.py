weight_in_kilos = float(input())
type_of_delivery = input()
distance_in_kilometers = int(input())

price_for_kilometer = 0
over_price = 0
over_price_percent = 0
final_price = 0

if weight_in_kilos < 1:
    price_for_kilometer = 0.03
elif weight_in_kilos < 10:
    price_for_kilometer = 0.05
elif weight_in_kilos < 40:
    price_for_kilometer = 0.10
elif weight_in_kilos < 90:
    price_for_kilometer = 0.15
elif weight_in_kilos <= 150:
    price_for_kilometer = 0.20

# type_of_delivery == "standard":

final_price = distance_in_kilometers * price_for_kilometer

if type_of_delivery == "express":
    if weight_in_kilos < 1:
        over_price_percent = 80
    elif weight_in_kilos < 10:
        over_price_percent = 40
    elif weight_in_kilos < 40:
        over_price_percent = 5
    elif weight_in_kilos < 90:
        over_price_percent = 2
    elif weight_in_kilos <= 150:
        over_price_percent = 1

    over_price = distance_in_kilometers * weight_in_kilos * (price_for_kilometer * (over_price_percent / 100))
    final_price += over_price

print(f"The delivery of your shipment with weight of {weight_in_kilos :.3f} kg. would cost {final_price :.2f} lv.")
