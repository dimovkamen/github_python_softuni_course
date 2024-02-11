def is_palindrome(number_str):
    # is_the_same = True
    # len_number_str = len(number)
    # for index in range(0, len_number_str // 2):
    #     if number_str[index] != number_str[len_number_str - index - 1]:
    #         is_the_same = False
    #         break
    #
    # return is_the_same
    if number_str == number_str[::-1]:
        return True
    else:
        return False


input_list = input()
numbers_list = input_list.split(", ")

for number in numbers_list:
    if is_palindrome(number):
        print("True")
    else:
        print("False")
