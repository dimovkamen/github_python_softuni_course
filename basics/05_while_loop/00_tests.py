student_name = input()
total_grade = 0
bad_attempts = 0
current_class = 1
is_excluded = False
while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_attempts += 1
        if bad_attempts > 1:
            is_excluded = True
            break
        continue
    bad_attempts = 0
    current_class += 1
    total_grade += current_grade
if is_excluded: # if is_excluded == True
    print(f"{student_name} has been excluded at {current_class} grade")
else: #elif is_excluded == False
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")