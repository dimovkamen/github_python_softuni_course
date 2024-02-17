import math

numbers_list = list(map(int, input().split(", ")))
groups_count = math.floor( (max(numbers_list) - 1) / 10) + 1

for group_number in range(1, groups_count + 1):
    current_list = []
    for num in numbers_list:
        group_end = group_number * 10
        group_start = group_end - 9
        if group_start <= num <= group_end:
            current_list.append(num)

    print(f"Group of {group_number}0's: {current_list}")
