import re

text = input()
word = input()

# pattern = rf'\b{re.escape(word)}\b'
# result = re.findall(pattern, text, re.IGNORECASE)

pattern = rf'(?i)\b{re.escape(word)}\b'
result = re.findall(pattern, text)

print(len(result))
