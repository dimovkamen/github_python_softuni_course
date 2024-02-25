list_of_phones = input().split(", ")

while True:
    command = input()
    if command == "End":
        break

    command_list = command.split(" - ")
    operation = command_list[0]

    if operation == "Add":
        phone_model = command_list[1]
        if phone_model not in list_of_phones:
            list_of_phones.append(phone_model)
    elif operation == "Remove":
        phone_model_remove = command_list[1]
        if phone_model_remove in list_of_phones:
            list_of_phones.remove(phone_model_remove)
    elif operation == "Bonus phone":
        old_phone = command_list[1].split(":")[0]
        new_phone = command_list[1].split(":")[1]
        if old_phone in list_of_phones:
            index_of_old_phone = list_of_phones.index(old_phone)
            list_of_phones.insert(index_of_old_phone + 1, new_phone )
    elif operation == "Last":
        phone_last = command_list[1]
        if phone_last in list_of_phones:
            list_of_phones.remove(phone_last)
            list_of_phones.append(phone_last)

print(", ".join(list_of_phones))
