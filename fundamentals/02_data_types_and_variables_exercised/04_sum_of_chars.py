number_of_lines = int(input())
total_sum = 0

for _ in range(number_of_lines):
    character = input()
    #print(ord(character))
    #print(type(ord(character)))
    total_sum += ord(character)

print(f"The sum equals: {total_sum}")
