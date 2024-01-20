import math

tv_serial_name = input()
episode_length = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4

time_needed = episode_length + lunch_time + relax_time

if time_needed <= break_time:
    time_left = break_time - time_needed
    time_left = math.ceil(time_left)
    print(f"You have enough time to watch {tv_serial_name} and left with {time_left} minutes free time.")
else:
    time_needed = time_needed - break_time
    time_needed = math.ceil(time_needed)
    print(f"You don't have enough time to watch {tv_serial_name}, you need {time_needed} more minutes.")
