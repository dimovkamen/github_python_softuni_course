# comprehension --> make small fast operations with list fields and create new list for example
numbers = [1, 2, 3, 4, 5, 6]
numbers_squares = [index ** 2 for index in numbers if index % 2 == 0]

# numbers_squares = []
# for index in numbers:
#     if index % 2 == 0:
#         numbers_squares.append(index)

print(numbers)
print(numbers_squares)

# using set
sentence = 'Hello, Python!'
unique_chars = {char for char in sentence if char.isalpha()}

print(unique_chars)

# using if-else in list comprehansion
nums = [1, 2, 3, 4, 5]
is_even_list = [True if z % 2 == 0 else False for z in nums]
print(is_even_list)
