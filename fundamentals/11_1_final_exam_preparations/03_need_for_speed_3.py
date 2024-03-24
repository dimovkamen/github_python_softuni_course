number_of_cars = int(input())
cars_dictionary = {}

for index in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars_dictionary[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input()
    if command == 'Stop':
        break

    car_command_list = command.split(" : ")

    car_command = car_command_list[0]
    if car_command == "Drive":
        car_model = car_command_list[1]
        drive_distance = int(car_command_list[2])
        fuel_needed = int(car_command_list[3])
        if cars_dictionary[car_model]["fuel"] < fuel_needed:
            print("Not enough fuel to make that ride")
        else:
            cars_dictionary[car_model]["mileage"] += drive_distance
            cars_dictionary[car_model]["fuel"] -= fuel_needed
            print(f'{car_model} driven for {drive_distance} kilometers. {fuel_needed} liters of fuel consumed.')
            if cars_dictionary[car_model]["mileage"] >= 100000:
                del cars_dictionary[car_model]
                print(f"Time to sell the {car_model}!")
    elif car_command == "Refuel":
        car_model = car_command_list[1]
        refuel_fuel = int(car_command_list[2])
        if cars_dictionary[car_model]["fuel"] + refuel_fuel <= 75:
            cars_dictionary[car_model]["fuel"] += refuel_fuel
            fuel_inserted = refuel_fuel
        else:
            fuel_inserted = 75 - cars_dictionary[car_model]["fuel"]
            cars_dictionary[car_model]["fuel"] = 75
        print(f"{car_model} refueled with {fuel_inserted} liters")
    elif car_command == "Revert":
        car_model = car_command_list[1]
        kilometers = int(car_command_list[2])
        if cars_dictionary[car_model]["mileage"] - kilometers >= 10000:
            cars_dictionary[car_model]["mileage"] -= kilometers
            print(f"{car_model} mileage decreased by {kilometers} kilometers")
        else:
            cars_dictionary[car_model]["mileage"] = 10000

for key, value in cars_dictionary.items():
    print(f'{key} -> Mileage: {value["mileage"]} kms, Fuel in the tank: {value["fuel"]} lt.')
