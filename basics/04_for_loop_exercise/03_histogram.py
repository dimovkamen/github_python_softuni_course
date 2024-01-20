numbers_count = int(input())

range_1_count = 0
range_2_count = 0
range_3_count = 0
range_4_count = 0
range_5_count = 0

for index in range(numbers_count):
    current_number = int(input())
    if current_number < 200:
        range_1_count += 1
    elif 200 <= current_number <= 399:
        range_2_count += 1
    elif 400 <= current_number <= 599:
        range_3_count += 1
    elif 500 <= current_number <= 799:
        range_4_count += 1
    elif current_number >= 800:
        range_5_count += 1

print(f"{range_1_count / numbers_count * 100 :.2f}%")
print(f"{range_2_count / numbers_count * 100 :.2f}%")
print(f"{range_3_count / numbers_count * 100 :.2f}%")
print(f"{range_4_count / numbers_count * 100 :.2f}%")
print(f"{range_5_count / numbers_count * 100 :.2f}%")
