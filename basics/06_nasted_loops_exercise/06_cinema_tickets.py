film_name = input()
standard_tickets_count_all = 0
student_tickets_count_all = 0
kid_tickets_count_all = 0
all_tickets_count = 0

while film_name != 'Finish':
    free_seats = int(input())

    standard_tickets_count = 0
    student_tickets_count = 0
    kid_tickets_count = 0

    for _ in range(free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "standard":
            standard_tickets_count += 1
        elif ticket_type == "student":
            student_tickets_count += 1
        elif ticket_type == "kid":
            kid_tickets_count += 1

    percent = (standard_tickets_count + student_tickets_count + kid_tickets_count) / free_seats
    print(f"{film_name} - {percent :.2%} full.")

    standard_tickets_count_all += standard_tickets_count
    student_tickets_count_all += student_tickets_count
    kid_tickets_count_all += kid_tickets_count

    film_name = input()

all_tickets_count = standard_tickets_count_all + student_tickets_count_all + kid_tickets_count_all

standard_tickets_percent = standard_tickets_count_all / all_tickets_count
student_tickets_percent = student_tickets_count_all / all_tickets_count
kid_tickets_percent = kid_tickets_count_all / all_tickets_count

print(f"Total tickets: {all_tickets_count}")
print(f"{student_tickets_percent :.2%} student tickets.")
print(f"{standard_tickets_percent :.2%} standard tickets.")
print(f"{kid_tickets_percent :.2%} kids tickets.")
