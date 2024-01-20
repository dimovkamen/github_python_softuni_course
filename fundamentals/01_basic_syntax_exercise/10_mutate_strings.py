string1 = input()
string2 = input()

string3 = ""
previous_string = string1

for index in range(0, len(string1), 1):
    string3 = string2[0:index+1] + string1[index+1:]
    if string3 != previous_string:
        print(string3)
        previous_string = string3
