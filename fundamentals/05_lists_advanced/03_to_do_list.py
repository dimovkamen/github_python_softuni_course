notes_ordered = [0] * 10

while True:
    command = input()
    if command == "End":
        break

    note_list = command.split("-")
    priority_number = int(note_list[0])
    task_text = note_list[1]

    notes_ordered.pop(priority_number - 1)
    notes_ordered.insert(priority_number - 1, task_text)

result = [element for element in notes_ordered if element != 0]

print(result)
