def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False


input_numbers = input()
list_ints = list(map(int, input_numbers.split()))
print(list(filter(is_even_number, list_ints)))
