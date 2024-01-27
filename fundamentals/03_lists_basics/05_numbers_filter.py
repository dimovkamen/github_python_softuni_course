number = int(input())
numbers_list = []
filtered_list = []

for _ in range(number):
    current_number = int(input())
    numbers_list.append(current_number)

command = input()

if command == "even":
    for num in numbers_list:
        if num % 2 == 0:
            filtered_list.append(num)
elif command == "odd":
    for num in numbers_list:
        if num % 2 == 1:
            filtered_list.append(num)
elif command == "negative":
    for num in numbers_list:
        if num < 0:
            filtered_list.append(num)
elif command == "positive":
    for num in numbers_list:
        if num >= 0:
            filtered_list.append(num)

print(filtered_list)
