import math
# from math import ceil

number_of_people = int(input()) # 10
capacity = int(input()) # 3
courses = math.ceil(number_of_people/capacity)
print(courses)

# while True:
#     courses += 1                                    # 1 2 3  4
#     number_of_people = number_of_people - capacity  # 7 4 1 -2
#     if number_of_people <= 0:
#         break
#
# print(courses)
