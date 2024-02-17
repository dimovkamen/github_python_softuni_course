numbers_list = list(map(int,input().split(", ")))
positive_list = []
negative_list = []
even_list = []
odd_list = []

for number in numbers_list:
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

print("Positive: " + ", ".join(list(map(str, positive_list))))
print("Negative: " + ", ".join(list(map(str, negative_list))))
print("Even: " + ", ".join(list(map(str, even_list))))
print("Odd: " + ", ".join(list(map(str, odd_list))))
