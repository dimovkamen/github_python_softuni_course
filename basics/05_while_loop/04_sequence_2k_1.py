number = int(input())

# 1 3 7 15 31

next_number = 1

while next_number <= number:
    print(next_number)
    next_number = next_number * 2 + 1
