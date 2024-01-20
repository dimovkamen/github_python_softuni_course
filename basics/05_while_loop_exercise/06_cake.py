width = int(input())
length = int(input())
pieces_all = width * length

command = input()
pieces_eaten_all = 0

while command != 'STOP':
    pieces_eaten = int(command)
    pieces_eaten_all += pieces_eaten
    if pieces_eaten_all >= pieces_all:
        break

    command = input()

if pieces_eaten_all <= pieces_all:
    difference = pieces_all - pieces_eaten_all
    print(f"{difference} pieces are left.")
else:
    difference = pieces_eaten_all - pieces_all
    print(f"No more cake left! You need {difference} pieces more.")
