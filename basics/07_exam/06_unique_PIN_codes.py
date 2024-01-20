first_digit_max = int(input())
second_digit_max = int(input())
third_digit_max = int(input())

for first_number in range(1, first_digit_max + 1):
    if first_number % 2 != 0:
        continue
    for second_number in range(1, second_digit_max + 1):
        if second_number == 1 or second_number == 4 or second_number == 6 or second_number == 8 or second_number == 9:
            continue
        for third_number in range(1, third_digit_max + 1):
            if third_number % 2 != 0:
                continue
            print(f"{first_number} {second_number} {third_number}")
