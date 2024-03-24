my_coffee_list = input().split()

number_of_the_command = int(input())

for coffees in range(number_of_the_command):

    current_command = input().split()
    action = current_command[0]

    if action == "Include":
        item = current_command[1]
        my_coffee_list.append(item)

    elif action == "Remove":
        action = current_command[0]
        item = current_command[1]
        count = int(current_command[2])

        if count <= len(my_coffee_list):
            if item == "first":
                for _ in range(count):
                    my_coffee_list.pop(0)
            elif item == "last":
                for _ in range(count):
                    my_coffee_list.pop(-1)

    elif action == "Prefer":
        coffe_index_1 = int(current_command[1])
        coffe_index_2 = int(current_command[2])
        if 0 <= coffe_index_1 < len(my_coffee_list) and 0 <= coffe_index_2 < len(my_coffee_list):
            coffee_on_index_1 = my_coffee_list[coffe_index_1]
            coffee_on_index_2 = my_coffee_list[coffe_index_2]
            my_coffee_list[coffe_index_1] = coffee_on_index_2
            my_coffee_list[coffe_index_2] = coffee_on_index_1

    elif action == "Reverse":
        my_coffee_list.reverse()

print("Coffees:\n" + " ".join(my_coffee_list))
