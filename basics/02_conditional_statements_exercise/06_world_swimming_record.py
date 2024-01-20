import math

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_one_meter = float(input())

how_many_15m = math.floor(distance_in_meters / 15)

ivan_swim_record = distance_in_meters * seconds_for_one_meter + how_many_15m * 12.5

#print(ivan_swim_record)

if ivan_swim_record < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {ivan_swim_record :.2f} seconds.")
else:
    print(f"No, he failed! He was {(ivan_swim_record - record_in_seconds) :.2f} seconds slower.")
