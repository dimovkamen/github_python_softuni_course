def show_menu():
    print("")
    print("------------- ToDo List Menu -------------")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Quit")
    print("------------------------------------------")


def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"--> Task /{task}/ added.")
    print("------------------------------------------")


def mark_completed(todo_list):
    task = input("Enter the task you want to complete: ")
    #print(todo_list)
    is_mark_completed = False

    for task_instance in todo_list:
        if task_instance["task"] == task:
            task_instance["completed"] = True
            print(f"Task /{task}/ completed.")
            is_mark_completed = True
            break

    if not is_mark_completed:
        print("Task not found.")

    print("------------------------------------------")


def view_tasks(todo_list):
    print("Tasks list below.")
    print(todo_list)
    print("------------------------------------------")


def todo_list_program():
    todo_list = []

    while True:
        show_menu()
        choice = input('Enter your choice (1-4): ')
        print("------------------------------------------")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            mark_completed(todo_list)
        elif choice == '3':
            view_tasks(todo_list)
        elif choice == '4':
            print("Exit! Bye :)")
            break
        else:
            print("Invalid. Please enter command again!")

    view_tasks(todo_list)


todo_list_program()
