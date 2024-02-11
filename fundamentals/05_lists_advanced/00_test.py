# append --> add element after last one
# extend --> add elements from other list after last one 1, 2, 3 extend 4, 5 --> 1, 2, 3, 4, 5 ( += also can be used)
# insert --> add element before specific index
# clear  --> remove all elements from the list, []
# remove --> remove first occurrence of a value (not by index!)
# pop    --> remove element by index from a list and returns it
# reverse--> reverse elements in a list
# index  --> return index of a specific value

# comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [num ** 2 for num in numbers if num % 2 == 0]
print(squares)

squares_dictionary = {num: num ** 2 for num in numbers if num % 2 == 0}
print(squares_dictionary)

keys = ['name', 'age']
values = ['Kamen', 20]
people_dictionary = {key: value for key, value in zip(keys, values)}
print(list(zip(keys, values)))
print(people_dictionary)

sentence = "Hello, Hi Python!"
unique_chars = {char for char in sentence if char.isalpha()}
print(unique_chars)
