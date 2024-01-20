numbers_count = int(input())

sum_first_numbers = 0
sum_second_numbers = 0

for index in range(numbers_count):
    next_number = int(input())
    sum_first_numbers += next_number

for index in range(numbers_count, numbers_count * 2):
    next_number = int(input())
    sum_second_numbers += next_number

if sum_first_numbers == sum_second_numbers:
    print(f"Yes, sum = {sum_first_numbers}")
else:
    print(f"No, diff = {abs(sum_first_numbers - sum_second_numbers)}")
