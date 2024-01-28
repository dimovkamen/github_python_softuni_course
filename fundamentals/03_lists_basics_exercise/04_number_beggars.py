money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integers = []

beggars_sum_list = []

for money in money_as_string:
    money_as_integers.append(int(money))

for index in range(1, number_of_beggars + 1):
    beggars_sum_list.append(0)

while len(money_as_integers) > 0:
    for beggar_number in range(0, number_of_beggars):
        if len(money_as_integers) > 0:
            beggars_sum_list[beggar_number] += money_as_integers.pop(0)
        else:
            break

print(beggars_sum_list)
