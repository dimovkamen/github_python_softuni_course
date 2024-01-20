number = int(input())

for _ in range(number):
    string = input()
    is_pure = True

    for index, symbol in enumerate(string):
        if symbol == "," or symbol == "." or symbol == "_":
            is_pure = False
            break

    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
