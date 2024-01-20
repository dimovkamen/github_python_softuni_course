number = int(input())

for number_from_range in range(1111, 9999 + 1):
    is_divisible_no_reminder = True
    for digit in str(number_from_range):
        if int(digit) == 0:
            is_divisible_no_reminder = False
            break
        elif number % int(digit) != 0:
            is_divisible_no_reminder = False
            break
    if is_divisible_no_reminder:
        print(f"{number_from_range}", end=" ")
