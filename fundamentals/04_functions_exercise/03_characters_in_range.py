def all_chars(first_char, second_char):
    result = ''
    for index in range(ord(first_char) + 1, ord(second_char)):
        #print(index)
        result += chr(index) + " "
    return result

first_char = input()
second_char = input()

print(all_chars(first_char, second_char))
