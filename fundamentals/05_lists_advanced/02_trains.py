wagons_count = int(input())
train_list = [0 for _ in range(wagons_count)]
# train_list = [0] * int(input())

command = input()

while command != "End":
    commands_list = command.split()

    if commands_list[0] == "add":
        people_add = int(commands_list[1])
        train_list[-1] += people_add
    elif commands_list[0] == "insert":
        index_insert = int(commands_list[1])
        people_insert = int(commands_list[2])
        train_list[index_insert] += people_insert
    elif commands_list[0] == "leave":
        index_leave = int(commands_list[1])
        people_leave = int(commands_list[2])
        train_list[index_leave] -= people_leave

    command = input()

print(train_list)
