word_1 = input()
word_2 = input()

while word_1 in word_2:
    word_2 = word_2.replace(word_1,"")

print(word_2)
