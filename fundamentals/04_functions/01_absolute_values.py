numbers_list = input().split()

absolute_numbers = []

for number in numbers_list:
    absolute_numbers.append(abs(float(number)))
print(absolute_numbers)

# absolute_numbers = list(map(float, numbers_list))
# absolute_numbers_1 = list(map(abs, absolute_numbers))
#
# print(absolute_numbers_1)