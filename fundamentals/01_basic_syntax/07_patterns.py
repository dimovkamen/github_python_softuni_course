number = int(input())

for index1 in range(1, number+1):
    for _ in range(0, index1):
        print('*', end='')
    print()

for index1 in range(number - 1, 0, -1):
    for _ in range(0, index1):
        print('*', end='')
    print()

