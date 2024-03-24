import re

text = input()

pattern = r"((([#@])[a-zA-Z]{3,}\3)(\3[a-zA-Z]{3,}\3))"

result_list = re.findall(pattern, text)

mirror_words_list = []

if len(result_list) > 0:
    print(f"{len(result_list)} word pairs found!")

    for matched_pairs in result_list:
        first_word = matched_pairs[1][1:len(matched_pairs[1])-1]
        second_word = matched_pairs[3][1:len(matched_pairs[3])-1]
        reversed_second_word = second_word[::-1]
        if first_word == reversed_second_word:
            mirror_words_list.append(f"{first_word} <=> {second_word}")
else:
    print("No word pairs found!")

if len(mirror_words_list) > 0:
    print("The mirror words are:")
    print(", ".join(mirror_words_list))
else:
    print("No mirror words!")
