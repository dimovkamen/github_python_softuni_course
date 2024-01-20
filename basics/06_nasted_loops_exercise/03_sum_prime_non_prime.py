command = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0

while command != 'stop':
    number = int(command)

    if number < 0:
        print("Number is negative.")
    else:
        is_prime = True
        for index in range(2, number):
            if number % index == 0:
                is_prime = False
                break
        if is_prime:
            sum_prime_numbers += number
        else:
            sum_non_prime_numbers += number

    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
