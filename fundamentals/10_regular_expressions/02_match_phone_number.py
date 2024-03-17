import re

phones = input()
valid_phones = []

regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
phones_match_list = re.findall(regex, phones)

print(", ".join(phones_match_list))
