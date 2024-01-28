factor = int(input())
count = int(input())
numbers_list = []

for current in range(1, count + 1):
    numbers_list.append(current * factor)

print(numbers_list)
