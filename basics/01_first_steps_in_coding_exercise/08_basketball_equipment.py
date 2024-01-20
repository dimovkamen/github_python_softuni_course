tax_per_one_year = int(input())

shoes_price = tax_per_one_year - (tax_per_one_year * 0.4)
# print(shoes_price)
kit_price = shoes_price - shoes_price * 0.2
# print(kit_price)
ball_price = kit_price / 4
# print(ball_price)
accessories_price = ball_price / 5
# print(accessories_price)

final_price = tax_per_one_year + shoes_price + kit_price + ball_price + accessories_price

print(final_price)
