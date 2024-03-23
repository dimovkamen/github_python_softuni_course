import re

text = input()

# pattern =r'\b((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'
pattern =r'\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'

result = re.findall(pattern, text)
# print(result)
for email in result:
    # print(email)
    print(email[0])
