height_reached = 5364
days_climbing = 1
is_goal_reached = False

command = input()

while command != "END":
    sleeping = command  # Yes No
    meters_climbed = int(input())

    if sleeping == 'Yes':
        days_climbing += 1
        if days_climbing > 5:
            break

    height_reached += meters_climbed

    #print(f"{days_climbing} {height_reached}")

    if height_reached >= 8848:
        is_goal_reached = True
        break

    command = input()

if is_goal_reached:
    print(f"Goal reached for {days_climbing} days!")
else:
    print(f"Failed!")
    print(f"{height_reached}")
