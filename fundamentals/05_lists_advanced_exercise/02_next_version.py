list_int = [int(string) for string in input().split(".")]

list_int[-1] += 1
for index in range(len(list_int) - 1, 0, -1):
    if list_int[index] > 9:
        list_int[index] = 0
        list_int[index - 1] += 1

initial_version_list_str = [str(integer) for integer in list_int]

print(".".join(initial_version_list_str))
