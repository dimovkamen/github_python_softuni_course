fb_followers_dictionary = {}

while True:
    command = input()
    if command == "Log out":
        break

    fb_actions_list = command.split(": ")
    fb_action = fb_actions_list[0]
    fb_username = fb_actions_list[1]

    if fb_action == "New follower":
        if fb_username not in fb_followers_dictionary:
            fb_followers_dictionary[fb_username] = {"fb_likes": 0, "fb_comments": 0}
    elif fb_action == "Like":
        likes_count = int(fb_actions_list[2])
        if fb_username not in fb_followers_dictionary:
            fb_followers_dictionary[fb_username] = {"fb_likes": likes_count, "fb_comments": 0}
        else:
            fb_followers_dictionary[fb_username]["fb_likes"] += likes_count
    elif fb_action == "Comment":
        if fb_username not in fb_followers_dictionary:
            fb_followers_dictionary[fb_username] = {"fb_likes": 0, "fb_comments": 1}
        else:
            fb_followers_dictionary[fb_username]["fb_comments"] += 1
    elif fb_action == "Blocked":
        if fb_username not in fb_followers_dictionary:
            print(f"{fb_username} doesn't exist.")
        else:
            del fb_followers_dictionary[fb_username]

fb_followers_count = len(fb_followers_dictionary)
print(f"{fb_followers_count} followers")

for user, user_items in fb_followers_dictionary.items():
    likes_comments_sum = user_items["fb_likes"] + user_items["fb_comments"]
    print(f"{user}: {likes_comments_sum}")
