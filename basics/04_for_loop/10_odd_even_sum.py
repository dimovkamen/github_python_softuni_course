numbers_count = int(input())

even_numbers_sum = 0
odd_numbers_sum = 0

for index in range(1, numbers_count + 1):
    next_number = int(input())
    if index % 2 == 0:
        even_numbers_sum += next_number
    else:
        odd_numbers_sum += next_number

if even_numbers_sum == odd_numbers_sum:
    print("Yes")
    print(f"Sum = {even_numbers_sum}")
else:
    difference = abs(even_numbers_sum - odd_numbers_sum)
    print("No")
    print(f"Diff = {difference}")
