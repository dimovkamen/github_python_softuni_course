# # # # # # # # # # # # # # # # # # # # # # # #
# map use function for every list element
# # # # # # # # # # # # # # # # # # # # # # # #

strings_list = ["1", "26", "3", "478", "5"]

numbers_list = list(map(int, strings_list))
chars_len_list = list(map(len, strings_list))
print(strings_list)
print(numbers_list)
print(chars_len_list)

# with comprehension
numbers_list_2 = [int(num_str) for num_str in strings_list]
print(numbers_list_2)

# with lambda as function
numbers_list_doubled = list(map(lambda n_str: int(n_str) * 2, strings_list))
print(numbers_list_doubled)

# with comprehension
numbers_list_doubled_2 = [int(num_str) * 2 for num_str in strings_list]
print(numbers_list_doubled_2)

# # # # # # # # # # # # # # # # # # # # # # # #
# filter some elements with given condition --> True / False
# # # # # # # # # # # # # # # # # # # # # # # #

n_list = [0, 1, 26, 3, 478, 5]
#                                      True | False
even_numbers = list(filter(lambda num: num % 2 == 0, n_list))
even_numbers_2 = list(filter(lambda n: n % 2, n_list))
# as it uses only True | False, it will remove the 0 (False). Others are considered as (True)
even_numbers_3 = list(filter(lambda n: n * 2, n_list))
print(n_list)
print(even_numbers)
print(even_numbers_2)
print(even_numbers_3)
