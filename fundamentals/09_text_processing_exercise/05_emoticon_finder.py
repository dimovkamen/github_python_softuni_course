string_in = input()

for index in range(len(string_in)):
    if string_in[index] == ":":
        print(f":{string_in[index+1]}")
