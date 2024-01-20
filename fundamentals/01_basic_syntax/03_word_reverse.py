word = str(input())
reverse_word = ""

for index in range(len(word)-1, -1, -1):
    reverse_word += word[index]

print(reverse_word)

#for char in word:
#    print(char, end=" ")
