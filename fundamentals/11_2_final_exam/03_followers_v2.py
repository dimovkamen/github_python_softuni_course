followers_dict = {}

while True:
    command = input()
    if command == "Log out":
        break

    command_actions = command.split(": ")
    action = command_actions[0]

    if action == "New follower":
        username = command_actions[1]
        if username in followers_dict.keys():
            pass
        else:
            followers_dict[username] = {"likes_count": 0, "comments_count": 0}
        # print(followers_dict)
    elif action == "Like":
        username = command_actions[1]
        likes_count = int(command_actions[2])
        if username in followers_dict.keys():
            followers_dict[username]["likes_count"] += likes_count
        else:
            followers_dict[username] = {"likes_count": likes_count, "comments_count": 0}
        # print(followers_dict)
    elif action == "Comment":
        username = command_actions[1]
        if username in followers_dict.keys():
            followers_dict[username]["comments_count"] += 1
        else:
            followers_dict[username] = {"likes_count": 0, "comments_count": 1}
        # print(followers_dict)
    elif action == "Blocked":
        username = command_actions[1]
        if username in followers_dict.keys():
            del followers_dict[username]
        else:
            print(f"{username} doesn't exist.")
        # print(followers_dict)

followers_total_count = len(followers_dict)
print(f"{followers_total_count} followers")

for user_name, user_name_items in followers_dict.items():
    total_sum = user_name_items["likes_count"] + user_name_items["comments_count"]
    print(f"{user_name}: {total_sum}")
