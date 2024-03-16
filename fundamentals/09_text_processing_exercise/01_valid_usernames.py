def is_length_valid(name):
    if 3 <= len(name) <= 16:
        return True
    else:
        return False


def are_chars_valid(name):
    for char in name:
        if char.isalnum() or char == "-" or char == "_":
            continue
        else:
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    else:
        return True


def is_username_valid(name):
    if is_length_valid(name) and are_chars_valid(name) and no_redundant_symbols(name):
        return True
    else:
        return False


usernames_list = input().split(", ")

for username in usernames_list:
    if is_username_valid(username):
        print(username)
