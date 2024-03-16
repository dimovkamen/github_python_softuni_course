text_input = input().split()
total_sum = 0

for word in text_input:
    number = int(word[1:-1:1])
    first_letter = word[0]
    last_letter = word[-1]
    result_number = 0

    if first_letter.isupper():
        letter_position = ord(first_letter) - ord("A") + 1
        result_number = number / letter_position
    else:
        letter_position = ord(first_letter) - ord("a") + 1
        result_number = number * letter_position

    if last_letter.isupper():
        letter_position = ord(last_letter) - ord("A") + 1
        result_number -= letter_position
    else:
        letter_position = ord(last_letter) - ord("a") + 1
        result_number += letter_position

    total_sum += result_number

print(f"{total_sum :.2f}")
