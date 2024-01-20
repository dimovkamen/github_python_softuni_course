numbers_count = int(input())

if numbers_count > 0:
    next_number = int(input())
    max_number = next_number
    min_number = next_number
    for index in range(2, numbers_count + 1):
        next_number = int(input())
        if next_number > max_number:
            max_number = next_number
        if next_number < min_number:
            min_number = next_number

    print(f"Max number: {max_number}")
    print(f"Min number: {min_number}")
