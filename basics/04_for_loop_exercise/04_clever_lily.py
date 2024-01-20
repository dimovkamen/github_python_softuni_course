age = int(input())
washing_machine_price = float(input())
one_toy_price = int(input())

money_sum = 0
price_for_current_birthday = 0
toys_sold_sum = 0


for index in range(1, age + 1):
    if index % 2 == 0:
        price_for_current_birthday += 10
        money_sum += price_for_current_birthday - 1
    else:
        toys_sold_sum += one_toy_price

total_sum = money_sum + toys_sold_sum

difference = total_sum - washing_machine_price
if difference >= 0:
    print(f"Yes! {difference :.2f}")
else:
    print(f"No! {abs(difference) :.2f}")
