# 200, 100, 50, 20, 10, 5, 2, 1

sum_change = float(input())
# sum_penny = int(sum_change * 100)
coins_count = 0

while round(sum_change, 2) > 0:
    coins_count += 1

    if sum_change >= 2:
        sum_change -= 2
    elif sum_change >= 1:
        sum_change -= 1
    elif sum_change >= 0.5:
        sum_change -= 0.5
    elif sum_change >= 0.20:
        sum_change -= 0.220
    elif sum_change >= 0.10:
        sum_change -= 0.10
    elif sum_change >= 0.05:
        sum_change -= 0.05
    elif sum_change >= 0.02:
        sum_change -= 0.02
    elif sum_change >= 0.01:
        sum_change -= 0.01

print(coins_count)
