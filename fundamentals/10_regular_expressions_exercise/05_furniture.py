import re

pattern = r'>>([a-zA-Z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)'
total_money = 0
names = []

while True:
    command = input()
    if command == "Purchase":
        break

    furniture_list = re.search(pattern, command)

    if furniture_list:
        name = furniture_list.group(1)
        price = float(furniture_list.group(2))
        quantity = int(furniture_list.group(3))
        names.append(name)
        total_money += price * quantity

print("Bought furniture:")
for name_furniture in names:
    print(name_furniture)
print(f"Total money spend: {total_money :.2f}")
