searched_book_name = input()

checked_books_count = 0
is_book_found = False

next_book = input()

while next_book != "No More Books":
    if next_book == searched_book_name:
        is_book_found = True
        break
    checked_books_count += 1
    next_book = input()

if is_book_found:
    print(f"You checked {checked_books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books_count} books.")
