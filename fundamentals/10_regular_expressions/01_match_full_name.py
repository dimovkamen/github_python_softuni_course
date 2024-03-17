import re

names = input()
valid_names = []

regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
names_matches_list = re.findall(regex, names)

for name in names_matches_list:
    print(name, end=" ")
