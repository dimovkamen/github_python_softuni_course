import re

text = input()
total_calories = 0
total_days = 0
output_string = ""

pattern = r"([|#])([a-zA-Z\s]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]{1,4})\1"

items_result_list = re.findall(pattern, text)

# print(items_result_list)

for item in items_result_list:
    item_calories = int(item[3])
    total_calories += item_calories

total_days = total_calories // 2000
print(f"You have food to last you for: {total_days} days!")

for item in items_result_list:
    item_name = item[1]
    item_expiration_date = item[2]
    item_calories = int(item[3])
    total_calories += item_calories
    print(f"Item: {item_name}, Best before: {item_expiration_date}, Nutrition: {item_calories}")
