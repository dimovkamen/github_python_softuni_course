import re

# METHODS
# .search
# .findall
# .match

#
# def test_regex(regex, text):
#     match = re.search(regex, text)
#
#     if match:
#         print('Match found:', match.group())
#     else:
#         print('No match')
#
#
# def test_regex_all(regex, text):
#     match = re.findall(regex, text)
#     print(match)
#
#
# test_regex('\w{5,5}',"the quick brown fox jump over the lazy dog and foxs ")
# test_regex('\\bfox\\b',"the quick brown fox jump over the lazy dog and foxs ")
# test_regex('\d+',"Kamen123")
# test_regex('\D+',"Kamen123")
# test_regex('\w+','Hello...Word')
# test_regex('\W+','Hello...Word')
#
# test_regex('\w{5,5}.\w{3,3}',"the quick brown fox jump over the lazy dog and foxs ")


text = "_ (underscores) are also word characters!"
pattern = '\\w+'
result = re.findall(pattern, text)
print(result)

text = "I am born on 22-May-1999. My father is born 01-Jan-1950"
pattern = '\\b\\d{1,2}-[A-Z][a-z]{2}-\\d{4}\\b'
result = re.findall(pattern, text)
print(result)

emails = ["valid123@email.bg", "invalid*name@email.bg"]
pattern = "^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$"
for email in emails:
    if re.match(pattern,email):
        print(f"{email} - is valid")
    else:
        print(f"{email} - is NOT valid")


text = 'There are 3 dogs and 4 cast'
result = re.sub(r'\d', '*', text)
print(result)

text = 'There are 3 dogs and 4 cast'
result = re.subn(r'\d', '*', text)
print(result)
