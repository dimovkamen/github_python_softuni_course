resources_dictionary = {}

while True:
    command = input()
    if command == "stop":
        break

    key = command
    value = int(input())

    # if key in resources_dictionary:
    #     resources_dictionary[key] += value
    # else:
    #     resources_dictionary[key] = value

    if key not in resources_dictionary:
        resources_dictionary[key] = 0
    resources_dictionary[key] += value

for key, value in resources_dictionary.items():
    print(f"{key} -> {value}")
