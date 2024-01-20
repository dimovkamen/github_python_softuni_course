# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) -
# въведени от потребителя и проверява дали офисът на фирма е отворен,
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително

hour = int(input())
day_of_week = input()

if day_of_week == "Sunday" or (hour < 10 and hour > 18):
    print("closed")
else:
    print("open")

# if (day_of_week == "Monday" \
#         or day_of_week == "Tuesday" \
#         or day_of_week == "Wednesday" \
#         or day_of_week == "Thursday" \
#         or day_of_week == "Friday" \
#         or day_of_week == "Saturday") \
#         and 10 <= hour < 18:
#     print("open")
# else:
#     print("closed")
