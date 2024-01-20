NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
TINNER_PRICE = 5.00
BAGS_PRICE = 0.40

nylon_amount_square_meters = int(input())
paint_amount_liters = int(input())
tinner_amount_liters = int(input())
workman_hours = int(input())

nylon_sum = (nylon_amount_square_meters + 2) * NYLON_PRICE
paint_sum = (paint_amount_liters * 1.1) * PAINT_PRICE
tinner_sum = tinner_amount_liters * TINNER_PRICE

materials_price = nylon_sum + paint_sum + tinner_sum + BAGS_PRICE

workman_price_per_hour = materials_price * 0.3
workman_price_all_hours = workman_price_per_hour * workman_hours

final_sum = materials_price + workman_price_all_hours

print(f'{final_sum:.2f}')
