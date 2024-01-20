import sys

numbers_count = int(input())

max_number = -sys.maxsize
numbers_sum = 0

for index in range(numbers_count):
    current_number = int(input())
    numbers_sum += current_number
    if current_number > max_number:
        max_number = current_number

numbers_sum_without_max_number = numbers_sum - max_number

if numbers_sum_without_max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(numbers_sum_without_max_number - max_number)
    print("No")
    print(f"Diff = {difference}")
