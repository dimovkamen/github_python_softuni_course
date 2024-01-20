student_name = input()

current_year = 1
sum_all_assessments = 0
bad_assessment_count = 0

while current_year <= 12: # 1 2 3 .. 11 12
    annual_school_assessment = float(input())
    if annual_school_assessment < 4:
        bad_assessment_count += 1
        if bad_assessment_count == 2:
            break
        continue
    sum_all_assessments += annual_school_assessment
    bad_assessment_count = 0
    current_year += 1

if current_year == 13:
    average_assessment = sum_all_assessments / 12
    print(f"{student_name} graduated. Average grade: {average_assessment :.2f}")
else:
    print(f"{student_name} has been excluded at {current_year} grade")
