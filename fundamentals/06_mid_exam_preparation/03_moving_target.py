targets_list = [int(num) for num in input().split()]

while True:
    command = input()
    if command == "End":
        break

    commands = command.split()
    action = commands[0]
    index = int(commands[1])

    if action == "Shoot":
        power = int(commands[2])
        if 0 <= index < len(targets_list):
            if power >= targets_list[index]:
                targets_list.pop(index)
            else:
                targets_list[index] -= power
    elif action == "Add":
        value = int(commands[2])
        if 0 <= index < len(targets_list):
            targets_list.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(commands[2])
        index_start = index - radius
        index_end = index + radius
        if 0 <= index_start and index_end < len(targets_list):
            first = targets_list[0:index_start]
            second = targets_list[index_end + 1:]
            targets_list = first + second
        else:
            print("Strike missed!")

print("|".join(list(map(str, targets_list))))
