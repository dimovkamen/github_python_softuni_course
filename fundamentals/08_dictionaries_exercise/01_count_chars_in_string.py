words_list = input().split(" ")
letters_dictionary = {}

for word in words_list:
    for char in word:
        if char not in letters_dictionary:
            letters_dictionary[char] = 0
        letters_dictionary[char] += 1

for key, value in letters_dictionary.items():
    print(f"{key} -> {value}")
