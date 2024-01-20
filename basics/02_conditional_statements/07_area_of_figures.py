# square, rectangle, circle, triangle
# import math
#
# figure_type = input()
#
# if figure_type == "square":
#     side_length = float(input())
#     area_of_square = side_length * side_length
#     print(f"{area_of_square :.3f}")
# elif figure_type == "rectangle":
#     side_1_length = float(input())
#     side_2_length = float(input())
#     area_of_rectangle = side_1_length * side_2_length
#     print(f"{area_of_rectangle :.3f}")
# elif figure_type == "circle":
#     radius = float(input())
#     area_of_circle = math.pi * (radius * radius)
#     print(f"{area_of_circle :.3f}")
# elif figure_type == "triangle":
#     side_length = float(input())
#     height_length = float(input())
#     area_of_triangle = side_length * height_length / 2
#     print(f"{area_of_triangle :.3f}")

import math

figure_type = input()

area = 0

if figure_type == "square":
    side_length = float(input())
    area = side_length * side_length
elif figure_type == "rectangle":
    side_1_length = float(input())
    side_2_length = float(input())
    area = side_1_length * side_2_length
elif figure_type == "circle":
    radius = float(input())
    area = math.pi * (radius * radius)
elif figure_type == "triangle":
    side_length = float(input())
    height_length = float(input())
    area = side_length * height_length / 2

print(f"{area :.3f}")
