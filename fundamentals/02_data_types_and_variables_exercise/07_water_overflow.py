capacity = 255
number_of_lines = int(input())
current_liters = 0

for _ in range(number_of_lines):
    liters_of_water = int(input())
    if current_liters + liters_of_water > capacity:
        print("Insufficient capacity!")
    else:
        current_liters += liters_of_water

print(current_liters)
