courses_dictionary = {}

while True:
    command = input()

    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name in courses_dictionary:
        courses_dictionary[course_name].append(student_name)
    else:
        courses_dictionary[course_name] = [student_name]

for course, students in courses_dictionary.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
