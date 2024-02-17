targets_list = [int(num) for num in input().split()]
# print(targets_list)

while True:
    command = input()
    if command == "End":
        break

    commands = command.split()
    action = commands[0]
    index = int(commands[1])

    if action == "Shoot":
        if index < len(targets_list):
            power = int(commands[2])
            if power >= targets_list[index]:
                targets_list.pop(index)
            else:
                targets_list[index] -= power
    elif action == "Add":
        value = int(commands[2])
        if index < len(targets_list):
            targets_list[index] += value
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(commands[2])
        # print(index_start)
        # print(index_end)
        if index < len(targets_list):
            index_start = index - radius
            index_end = index + radius
            if index_start < 0 or index_end >= len(targets_list):
                print("Strike missed!")
                targets_list.pop(index)
            else:
                first = targets_list[0:index_start]
                second = targets_list[index_end + 1:]
                targets_list = first + second

print("|".join(list(map(str, targets_list))))
