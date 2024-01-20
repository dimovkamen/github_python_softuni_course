jury_count = int(input())
command = input()
sum_marks_all_presentation = 0
presentations_count = 0

while command != 'Finish':
    presentation_name = command
    sum_marks = 0

    for _ in range(jury_count):
        mark = float(input())
        sum_marks += mark

    average_mark_current_presentation = sum_marks / jury_count
    print(f"{presentation_name} - {average_mark_current_presentation :.2f}.")

    sum_marks_all_presentation += average_mark_current_presentation
    presentations_count += 1

    command = input()

average_mark_all_presentation = sum_marks_all_presentation / presentations_count
print(f"Student's final assessment is {average_mark_all_presentation :.2f}.")
