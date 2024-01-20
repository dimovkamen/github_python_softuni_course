exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minute = int(input())

exam_time_in_minutes = exam_hours * 60 + exam_minutes
arrival_time_in_minutes = arrival_hours * 60 + arrival_minute

if arrival_time_in_minutes > exam_time_in_minutes:
    print("Late")
elif 0 <= (exam_time_in_minutes - arrival_time_in_minutes) <= 30:
    print("On time")
elif exam_time_in_minutes - arrival_time_in_minutes > 30:
    print("Early")

if 0 < (exam_time_in_minutes - arrival_time_in_minutes) < 60:
    minutes = exam_time_in_minutes - arrival_time_in_minutes
    print(f"{minutes} minutes before the start")
elif (exam_time_in_minutes - arrival_time_in_minutes) >= 60:
    # "hh:mm hours before the start"
    minutes = exam_time_in_minutes - arrival_time_in_minutes
    hh = minutes // 60
    mm = minutes % 60
    print(f"{hh}:{mm :02d} hours before the start")
elif 0 < (arrival_time_in_minutes - exam_time_in_minutes) < 60:
    # •	 "mm minutes after the start"
    minutes = arrival_time_in_minutes - exam_time_in_minutes
    print(f"{minutes} minutes after the start")
elif (arrival_time_in_minutes - exam_time_in_minutes) >= 60:
    minutes = arrival_time_in_minutes - exam_time_in_minutes
    hh = minutes // 60
    mm = minutes % 60
    print(f"{hh}:{mm :02d} hours after the start")
