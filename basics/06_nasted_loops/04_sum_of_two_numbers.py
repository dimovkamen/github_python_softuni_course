first_number = int(input())
second_number = int(input())
magic_number = int(input())

combination_count = 0

is_combination_found = False

final_number_1 = 0
final_number_2 = 0

for number1 in range(first_number, second_number + 1):
    for number2 in range(first_number, second_number + 1):
        combination_count += 1
        if number1 + number2 == magic_number:
            final_number_1 = number1
            final_number_2 = number2
            is_combination_found = True
            break
    if is_combination_found:
        break

if is_combination_found:
    print(f"Combination N:{combination_count} ({final_number_1} + {final_number_2} = {magic_number})")
else:
    print(f"{combination_count} combinations - neither equals {magic_number}")
