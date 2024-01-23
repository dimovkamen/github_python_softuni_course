student_name = input()
student_town = " "

while student_name != "Welcome!":
    name_check = len(student_name)

    if name_check < 5:
        student_town = "Gryffindor"
    elif name_check == 5:
        student_town = "Slytherin"
    elif name_check == 6:
        student_town = "Ravenclaw"
    elif name_check > 6:
        student_town = "Hufflepuff"

    if student_name == "Voldemort":
        print("You must not speak of that name!")
        break

    print(f"{student_name} goes to {student_town}.")
    student_name = input()
else:
    print("Welcome to Hogwarts.")