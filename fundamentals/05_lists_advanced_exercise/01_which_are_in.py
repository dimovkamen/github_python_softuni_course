# string_sequence_1 = "ala, bala, nica"
# string_sequence_2 = "alaala, bala, nica"

string_sequence_1 = input()
string_sequence_2 = input()

result_words_list = []

string_sequence_1_list = string_sequence_1.split(", ")
string_sequence_2_list = string_sequence_2.split(", ")

# print(string_sequence_1_list)
# print(string_sequence_2_list)

for word in string_sequence_1_list:
    for word_2 in string_sequence_2_list:
        if word in word_2:
            result_words_list.append(word)
            break

print(result_words_list)
