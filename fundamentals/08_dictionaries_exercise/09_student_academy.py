number = int(input())
students_dictionary = {}

for _ in range(number):
    name = input()
    grade = float(input())

    if name not in students_dictionary:
        students_dictionary[name] = {}
        students_dictionary[name]["average"] = 0
        students_dictionary[name]["grades"] = []

    students_dictionary[name]["grades"].append(grade)
    average = sum(students_dictionary[name]["grades"]) / len(students_dictionary[name]["grades"])
    students_dictionary[name]["average"] = average

students_above_avg = {name: info for name, info in students_dictionary.items() if info['average'] >= 4.5}

for name, info in students_above_avg.items():
    average_grades = info['average']
    print(f"{name} -> {average_grades :.2f}")
