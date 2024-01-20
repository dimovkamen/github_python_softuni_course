divisor = int(input())
boundary = int(input())
number = divisor

for index in range(boundary, divisor - 1, -1):
    if index % divisor == 0:
        number = index
        break

print(number)
