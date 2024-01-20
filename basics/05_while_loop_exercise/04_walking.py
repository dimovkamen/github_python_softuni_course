command = input()
steps_sum = 0

while command != "Going home":
    steps = int(command)
    steps_sum += steps
    if steps_sum >= 10000:
        break
    command = input()

if command == "Going home":
    command = input()
    steps = int(command)
    steps_sum += steps

if steps_sum >= 10000:
    difference = steps_sum - 10000
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    difference = 10000 - steps_sum
    print(f"{difference} more steps to reach goal.")
