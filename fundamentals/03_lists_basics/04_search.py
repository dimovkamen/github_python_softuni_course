number = int(input())
word = input()
words_list = []
words_matching_list = []

for _ in range(number):
    text = input()
    words_list.append(text)
    if word in text:
        words_matching_list.append(text)

print(words_list)
print(words_matching_list)
