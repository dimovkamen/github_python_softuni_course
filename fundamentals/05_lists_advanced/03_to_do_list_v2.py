unsorted_list = []

while True:
    command = input()
    if command == "End":
        break

    unsorted_list.append(command)

sorted_list = sorted(unsorted_list, key=lambda n: int(n.split('-')[0]))
sorted_list = [note.split("-")[1] for note in sorted_list]
print(sorted_list)
 