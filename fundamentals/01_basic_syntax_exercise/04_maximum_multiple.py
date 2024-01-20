divisor = int(input())
boundary = int(input())
number = 0

for index in range(1, boundary + 1):
    if index % divisor == 0:
        number = index

print(number)
