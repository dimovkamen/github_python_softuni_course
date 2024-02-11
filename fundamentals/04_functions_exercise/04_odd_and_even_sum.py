def calculate_sums(number):
    number_str = str(number)
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for digit in number_str:
        digit_numeric = int(digit)
        if digit_numeric % 2 == 0:
            sum_of_even_digits += digit_numeric
        else:
            sum_of_odd_digits += digit_numeric

    return sum_of_odd_digits, sum_of_even_digits


input_number = input()
sum_of_odd_digits, sum_of_even_digits = calculate_sums(input_number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")

