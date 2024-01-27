companions_count = int(input())
days_of_adventure = int(input())
coins_sum = 0
coins_per_companion = 0

for day_number in range(1, days_of_adventure + 1):
    if day_number % 10 == 0:
        companions_count -= 2
    if day_number % 15 == 0:
        companions_count += 5
    coins_sum += 50
    coins_sum -= companions_count * 2
    if day_number % 3 == 0:
        coins_sum -= 3 * companions_count
    if day_number % 5 == 0:
        coins_sum += 20 * companions_count
        if day_number % 3 == 0:
            coins_sum -= 2 * companions_count

coins_per_companion = coins_sum // companions_count
print(f"{companions_count} companions received {coins_per_companion} coins each.")
