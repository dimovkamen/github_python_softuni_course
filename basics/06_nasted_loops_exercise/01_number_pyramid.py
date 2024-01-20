number = int(input())
current_number = 0
is_final_number_reached = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        current_number += 1
        print(f"{current_number} ", end="")
        if current_number == number:
            is_final_number_reached = True
            break
    if is_final_number_reached:
        break
    print()
