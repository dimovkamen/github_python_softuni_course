groups_count = int(input())

all_people_count = 0
people_in_group_1_count = 0
people_in_group_2_count = 0
people_in_group_3_count = 0
people_in_group_4_count = 0
people_in_group_5_count = 0

for index in range(groups_count):
    people_in_current_group_count = int(input())
    all_people_count += people_in_current_group_count
    if people_in_current_group_count <= 5:
        people_in_group_1_count += people_in_current_group_count
    elif people_in_current_group_count <= 12:
        people_in_group_2_count += people_in_current_group_count
    elif people_in_current_group_count <= 25:
        people_in_group_3_count += people_in_current_group_count
    elif people_in_current_group_count <= 40:
        people_in_group_4_count += people_in_current_group_count
    else:
        people_in_group_5_count += people_in_current_group_count

print(f"{people_in_group_1_count/all_people_count :.2%}")
print(f"{people_in_group_2_count/all_people_count :.2%}")
print(f"{people_in_group_3_count/all_people_count :.2%}")
print(f"{people_in_group_4_count/all_people_count :.2%}")
print(f"{people_in_group_5_count/all_people_count :.2%}")
