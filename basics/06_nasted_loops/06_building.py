number_of_floors = int(input())
number_of_rooms = int(input())

type_of_room = ""

for floor in range (number_of_floors, 0, -1 ): # 3 2 1
    if floor == number_of_floors:
        type_of_room = "L"
    elif floor % 2 == 0:
        type_of_room = "O"
    else:
        type_of_room = "A"

    for apartment in range(number_of_rooms): # 0 1 2 3 4
        print(f"{type_of_room}{floor}{apartment} ", end="")

    print("")
