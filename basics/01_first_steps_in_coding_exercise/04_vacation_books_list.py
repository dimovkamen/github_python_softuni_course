import math

pages_count = int(input())
pages_read_per_hour = int(input())
days_count = int(input())
time_sum = float((pages_count // pages_read_per_hour) / days_count)
print(math.floor(time_sum))
