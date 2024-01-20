command = input()
word = ""

while command != "End":
    word = ""

    if command == "SoftUni":
        command = input()
        continue
    else:
        for char in command:
            word += char
            word += char
        print(word)

    command = input()
