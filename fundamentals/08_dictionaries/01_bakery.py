elements = input().split(" ")
bakery_d = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    bakery_d[key] = value

print(bakery_d)
