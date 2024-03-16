string_input = input()
final_string = ""
explosion_strength = 0

for index in range(len(string_input)):
    # explosion
    if explosion_strength > 0 and string_input[index] != ">":
        explosion_strength -= 1
    # > mark
    elif string_input[index] == ">":
        final_string += string_input[index]
        explosion_strength += int(string_input[index + 1])
    # no explosion, no mark
    else:
        final_string += string_input[index]

print(final_string)
