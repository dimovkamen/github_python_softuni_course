bad_grades_threshold = int(input())

command = input()

task_last = ""
grades_count = 0
grades_sum = 0
bad_grades_count = 0
is_break_needed = False

while command != "Enough":
    task_name = command
    task_grade = int(input())
    if task_grade <= 4:
        bad_grades_count += 1
    if bad_grades_count == bad_grades_threshold:
        is_break_needed = True
        break
    grades_count += 1
    grades_sum += task_grade
    task_last = task_name
    command = input()

if is_break_needed:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    average_grade = grades_sum / grades_count
    print(f"Average score: {average_grade :.2f}")
    print(f"Number of problems: {grades_count}")
    print(f"Last problem: {task_last}")
