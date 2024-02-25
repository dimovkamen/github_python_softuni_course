class Car:
    color = "red"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is starting")

    def drive(self, distance):
        print(f"The {self.make} {self.model} is driving {distance} kilometers")

    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine is stopping")

    def print_info(self):
        print(f"{self.make} {self.model} {self.year}")


car_1 = Car('Ferrari', 'F450', 2015)
car_2 = Car("Porsche", "911 turbo S", 2015)
car_3 = Car("Lada", "Niva", 1985)

car_1.print_info()
car_1.start_engine()
car_1.drive(150)
car_1.stop_engine()
print()
car_2.print_info()
car_2.start_engine()
car_2.drive(50)
car_2.stop_engine()

print(car_1.color)
print(car_2.color)

car_1.color = "blue"
car_1.wheel = 16

print(car_1.color)
print(car_2.color)

Car.color = "black"

print(car_1.color)
print(car_2.color)

print(car_1.wheel)
