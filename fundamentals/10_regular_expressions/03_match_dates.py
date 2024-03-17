import re

dates = input()
valid_dates = []

regex = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
dates_match_list = re.findall(regex, dates)

for date_tuple in dates_match_list:
    full_date = f"Day: {date_tuple[0]}, Month: {date_tuple[2]}, Year: {date_tuple[3]}"
    print(full_date)
