width = int(input())
length = int(input())
height = int(input())

space_available = height * width * length

command = input()

while command != "Done":
    boxes = int(command)
    space_available -= boxes
    if space_available <= 0:
        break
    command = input()

if space_available > 0:
    print(f"{space_available} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space_available)} Cubic meters more.")
