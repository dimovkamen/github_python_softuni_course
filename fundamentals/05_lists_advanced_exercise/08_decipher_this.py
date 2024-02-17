def decipher_word(word_cipher):
    word_decipher = ""
    first_char_code = int(''.join(filter(str.isdigit, word_cipher)))
    character = chr(first_char_code)
    word_decipher = word_cipher.replace(str(first_char_code), character)
    second_char = word_decipher[1]
    last_char = word_decipher[-1]
    word_list = list(word_decipher)
    word_list[1] = last_char
    word_list[-1] = second_char
    return "".join(word_list)


message_words_cipher = input().split()
message_words_decipher = []

for word in message_words_cipher:
    message_words_decipher.append(decipher_word(word))

print(" ".join(message_words_decipher))
