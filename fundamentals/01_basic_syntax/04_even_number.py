count_numbers = int(input())

for _ in range(1, count_numbers + 1, 1):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")
