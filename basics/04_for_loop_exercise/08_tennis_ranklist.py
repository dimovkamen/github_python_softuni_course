import math

tournaments_count = int(input())
starting_points = int(input())

earned_points = 0
tournaments_won = 0

for index in range(tournaments_count):
    stage_reached = input()
    if stage_reached == "W":
        earned_points += 2000
        tournaments_won += 1
    elif stage_reached == "F":
        earned_points += 1200
    elif stage_reached == "SF":
        earned_points += 720

sum_all_points = starting_points + earned_points
print(f"Final points: {sum_all_points}")

average_points = math.floor(earned_points / tournaments_count)
print(f"Average points: {average_points}")

percent_tournaments_won = tournaments_won / tournaments_count
print(f"{percent_tournaments_won :.2%}")
