first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    string_number = str(number)
    sum_odd = 0
    sum_even = 0
    for index, char_number in enumerate(string_number):
        # print(f"{index} {char_number}")
        if index % 2 == 0:
            sum_even += int(char_number)
        else:
            sum_odd += int(char_number)
    # print(f"{sum_odd} {sum_even}")
    if sum_even == sum_odd:
        print(f"{number} ", end="")
