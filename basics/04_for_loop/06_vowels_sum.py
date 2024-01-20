text = input()
sum_vowels = 0

for character in text:
    if character == "a":
        sum_vowels += 1
    elif character == "e":
        sum_vowels += 2
    elif character == "i":
        sum_vowels += 3
    elif character == "o":
        sum_vowels += 4
    elif character == "u":
        sum_vowels += 5

print(sum_vowels)
