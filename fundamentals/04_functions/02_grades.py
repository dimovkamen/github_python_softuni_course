def grade_string(grade_number):
    if grade_number <= 2.99:
        return "Fail"
    elif grade_number <= 3.49:
        return "Poor"
    elif grade_number <= 4.49:
        return "Good"
    elif grade_number <= 5.49:
        return "Very Good"
    elif grade_number <= 6:
        return "Excellent"


grade = float(input())
print(grade_string(grade))
