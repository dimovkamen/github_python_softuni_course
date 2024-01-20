# 200, 100, 50, 20, 10, 5, 2, 1

sum_change = float(input())
sum_penny = int(sum_change * 100)
coins_count = 0

while sum_penny > 0:
    coins_count += 1

    if sum_penny >= 200:
        sum_penny -= 200
    elif sum_penny >= 100:
        sum_penny -= 100
    elif sum_penny >= 50:
        sum_penny -= 50
    elif sum_penny >= 20:
        sum_penny -= 20
    elif sum_penny >= 10:
        sum_penny -= 10
    elif sum_penny >= 5:
        sum_penny -= 5
    elif sum_penny >= 2:
        sum_penny -= 2
    elif sum_penny >= 1:
        sum_penny -= 10

print(coins_count)
