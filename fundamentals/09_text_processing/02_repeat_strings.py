strings_list = input().split()

for word in strings_list:
    print(word * len(word), end="")

# repeated_list = [text * len(text) for text in strings_list]
# print("".join(repeated_list))