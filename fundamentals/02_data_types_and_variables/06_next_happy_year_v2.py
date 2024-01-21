year = int(input())

while True:
    year += 1
    year_str = str(year)
    year_str_len = len(year_str)
    unique_digits_set_len = len(set(year_str))
    if year_str_len == unique_digits_set_len:
        break

print(year)
