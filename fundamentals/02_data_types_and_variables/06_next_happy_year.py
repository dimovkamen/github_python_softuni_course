year = int(input())

while True:
    year += 1
    unique_digits_str = ""
    is_happy_year = True
    for digit_str in str(year):            # 1 0 0 1
        if digit_str in unique_digits_str:
            is_happy_year = False
            break
        else:
            unique_digits_str += digit_str # 10
    if is_happy_year:
        break

print(year)
