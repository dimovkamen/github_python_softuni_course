start_index, last_index = int(input()), int(input())
final_string = ""

# for index in range(start_index, last_index + 1):
#     print(f"{chr(index)}", end=' ')

for index in range(start_index, last_index + 1):
    final_string += chr(index) + " "

print(final_string.strip())
 