#print([-int(num) for num in input().split()])

numbers_list = input().split()
opposite_numbers_list = []

for number in numbers_list:
    opposite = -int(number)
    opposite_numbers_list.append(opposite)

print(opposite_numbers_list)
