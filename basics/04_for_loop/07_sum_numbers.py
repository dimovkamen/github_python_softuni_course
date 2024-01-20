numbers_count = int(input())
numbers_sum = 0

for index in range(1, numbers_count + 1):
    next_number = int(input())
    numbers_sum += next_number

print(numbers_sum)
