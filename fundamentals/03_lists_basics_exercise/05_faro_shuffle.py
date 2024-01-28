strings = input().split()
count_of_shuffles = int(input())

#middle_of_the_deck = int(len(strings) / 2)
middle_of_the_deck = len(strings) // 2

for _ in range(count_of_shuffles):
    shuffled_strings = []
    for index in range(0, middle_of_the_deck):
        shuffled_strings.append(strings[index])
        shuffled_strings.append(strings[index + middle_of_the_deck])

    strings = shuffled_strings

print(strings)
