# str --> make it string, from int for example
# split
# join
# slicing --> word_1 = word[0:3]. Works also with lists
# reverse --> slice notation word_1 = word[::-1]
# concatenation --> +
# repeat string --> "red" * 3
# formatting with f string
# .isdigit() --> True False
# .isupper() .islower()
# .upper() .lower()
# .strip() .lstrip() .rstrip() --> remove white spaces
# .capitalize() --> make only first char capital, all others lower case
# .count('')
# .endswith() .startswith()  --> True False
# .find('')
# .isalnum() --> True False --> checks if all are letters and numbers
# .isalpha() --> check if only letters
# .isnumeric()
# .isdigit()
# .isdecimal()
# .replace()
# word_1 in word_2 - > check if sting is inside other string
# .isalnum() --> a-z A-Z 0-9

message = '''<?xml version="1.0" encoding="UTF-8"?>
  <note> 
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>'''
print(message)

word = "Hello"
word_1 = word[0:3]
print(word_1)

reverse_word = word[::-1]
print(reverse_word)

print("red " * 3)
print("red\n" * 3)

word_5 = "Hello Word"
print(word_5.capitalize())

print(word_5.count("o"))

print(word_5.find('o'))