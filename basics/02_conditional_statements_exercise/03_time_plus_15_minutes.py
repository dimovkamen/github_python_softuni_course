# hours = int(input())
# minutes = int(input())
#
# total_time = hours * 60 + minutes + 15
#
# if total_time >= 60 * 24:
#     total_time %= (60 * 24)
#
# hours = total_time // 60
# minutes = total_time % 60
#
# print(f'{hours}:{minutes :02d}')

hours = int(input())
minutes = int(input())

total_time = hours * 60 + minutes + 15

hours = total_time // 60
minutes = total_time % 60

if hours >= 24:
    hours = 0

print(f'{hours}:{minutes :02d}')
