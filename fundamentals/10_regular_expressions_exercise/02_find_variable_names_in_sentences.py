import re

text = input()
names_list = []

pattern = r'\b_([a-zA-Z0-9]+)\b'

result = re.finditer(pattern, text)

for names in result:
    names_list.append(names.group(1))

print(",".join(names_list))

# vars = re.findall(pattern, text)
# print(vars)