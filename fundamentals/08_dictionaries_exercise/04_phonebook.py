phonebook_dictionary = {}
number = 0

while True:
    command = input()

    if command.isdigit():
        number = int(command)
        break

    # name = command.split("-")[0]
    # phone = command.split("-")[1]
    name, phone = command.split("-")

    phonebook_dictionary[name] = phone

# print(number)
# print(phonebook_dictionary)

for index in range(0, number):
    contact_name = input()

    if contact_name in phonebook_dictionary:
        print(f"{contact_name} -> {phonebook_dictionary[contact_name]}")
    else:
        print(f"Contact {contact_name} does not exist.")
