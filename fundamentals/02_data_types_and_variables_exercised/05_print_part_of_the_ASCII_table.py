start_index, last_index = int(input()), int(input())

for index in range(start_index, last_index + 1):
    print(f"{chr(index)}", end=' ')
