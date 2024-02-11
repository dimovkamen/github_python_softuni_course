# input_string = input()
# vowels = 'aouei'
#
# result = [char for char in input_string if char.upper() not in vowels.upper()]
# print("".join(result))

input_string = input()
vowels = ('a', 'o', 'u', 'e', 'i')

result = [char for char in input_string if char.lower() not in vowels]
print("".join(result))
