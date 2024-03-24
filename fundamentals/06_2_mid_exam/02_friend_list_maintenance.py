all_friends_list = input().split(", ")
blacklisted_list = []
lost_list = []

while True:
    command = input()
    if command == "Report":
        break

    command_list = command.split()
    operation = command_list[0]

    # "Blacklist {name}":
    if operation == "Blacklist":
        friend_name = command_list[1]
        if friend_name in all_friends_list:
            index_in_list = all_friends_list.index(friend_name)
            #print(index_in_list)
            all_friends_list[index_in_list] = "Blacklisted"
            print(f"{friend_name} was blacklisted.")
            blacklisted_list.append(friend_name)
        else:
            print(f"{friend_name} was not found.")
    # "Error {index}":
    elif operation == "Error":
        index_in_list_error = int(command_list[1])
        if 0 <= index_in_list_error < len(all_friends_list):
            if all_friends_list[index_in_list_error] != "Blacklisted" and all_friends_list[index_in_list_error] != "Lost":
                name_lost = all_friends_list[index_in_list_error]
                all_friends_list[index_in_list_error] = "Lost"
                print(f"{name_lost} was lost due to an error.")
                lost_list.append(name_lost)
    # "Change {index} {new name}":
    elif operation == "Change":
        index_to_change = int(command_list[1])
        new_name_in_list = command_list[2]
        if 0 <= index_to_change < len(all_friends_list):
            current_list_name = all_friends_list[index_to_change]
            all_friends_list[index_to_change] = new_name_in_list
            print(f"{current_list_name} changed his username to {new_name_in_list}.")

print(f"Blacklisted names: {len(blacklisted_list)}")
print(f"Lost names: {len(lost_list)}")
print(" ".join(all_friends_list))
