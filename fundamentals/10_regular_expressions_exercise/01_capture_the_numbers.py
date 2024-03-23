import re

line = input()
pattern = r"\d+"
numbers = []

while line:
    result = re.findall(pattern, line)
    numbers.extend(result)
    line = input()

print(" ".join(numbers))
