text_input = input()
last_symbol = ""
final_text = ""

for index in range(len(text_input)):
    if text_input[index] == last_symbol:
        continue
    else:
        final_text += text_input[index]
        last_symbol = text_input[index]

print(final_text)
