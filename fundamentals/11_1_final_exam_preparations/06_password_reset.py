text = input()

while True:
    command = input()
    if command == "Done":
        break

    command_list = command.split()
    action = command_list[0]

    if action == "TakeOdd":
        new_text = ""
        for index in range(len(text)):
            if index % 2 == 1:
                new_text += text[index]
        text = new_text
        print(text)
    elif action == "Cut":
        action_index = int(command_list[1])
        action_length = int(command_list[2])
        first_part = text[0:action_index]
        second_part = text[action_index + action_length:]
        text = first_part + second_part
        print(text)
    elif action == "Substitute":
        sub_string = command_list[1]
        substitute = command_list[2]
        if sub_string in text:
            text = text.replace(sub_string, substitute)
            print(text)
        else:
            print("Nothing to replace!")

print(f"Your password is: {text}")
