length = int(input())
width = int(input())
height = int(input())

sand_heater_pump_percent = float(input())

aquarium_liters = (length * width * height) / 1000
# print(aquarium_liters)

sand_heater_pump_in_liters = aquarium_liters * (sand_heater_pump_percent / 100)

water_needed_in_liters = aquarium_liters - sand_heater_pump_in_liters
print(water_needed_in_liters)
