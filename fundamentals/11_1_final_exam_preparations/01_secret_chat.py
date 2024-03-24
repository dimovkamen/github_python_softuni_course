message = input()

while True:
    command = input()

    if command == "Reveal":
        break

    operations_list = command.split(":|:")
    operation = operations_list[0]

    if operation == "InsertSpace":
        index = int(operations_list[1])
        first_part = message[0:index:]
        second_part = message[index::]
        message = first_part + " " + second_part
        print(message)

    elif operation == "Reverse":
        substring = operations_list[1]
        if substring in message:
            message = message.replace(substring,"", 1)
            substring = substring[::-1]
            message += substring
            print(message)
        else:
            print("error")

    elif operation == "ChangeAll":
        substring = operations_list[1]
        replacement = operations_list[2]
        message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")
