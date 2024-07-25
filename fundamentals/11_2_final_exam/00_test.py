message = input()
command = input()

while command != 'End':
    command = command.split(' ')
    action = command[0]
    if action == 'Translate':
        given_char = command[1]
        replacement = command[2]
        message = message.replace(given_char, replacement)
        print(message)
    elif action == 'Includes':
        search_string = command[1]
        if search_string in message:
            print("True")
        else:
            print('False')
    elif action == 'Start':
        start_string = command[1]
        if message.startswith(start_string):
            print('True')
        else:
            print('False')
    elif action == 'Lowercase':
        message_lowercase = message.lower()
        message = message_lowercase
        print(message)
    elif action == 'FindIndex':
        find_index_char = command[1]
        for index in range(len(message) - 1, -1, -1):
            if message[index] == find_index_char:
                print(index)
                break
    elif action == 'Remove':
        start_index = int(command[1])
        count = int(command[2])
        before_string = message[0:start_index]
        after_string = message[start_index + count:]
        message = before_string + after_string
        print(message)

    command = input()
