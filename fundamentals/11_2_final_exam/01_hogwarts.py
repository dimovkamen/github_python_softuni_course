spell_str = input()

while True:
    command = input()
    if command == "Abracadabra":
        break

    command_list = command.split()
    action_spell = command_list[0]

    if action_spell == "Abjuration":
        upper_spell = ""
        for index in range(len(spell_str)):
            if spell_str[index].islower():
                upper_spell += spell_str[index].upper()
            else:
                upper_spell += spell_str[index]
        spell_str = upper_spell
        print(spell_str)
    elif action_spell == "Necromancy":
        spell_lower = ""
        for index in range(len(spell_str)):
            if spell_str[index].isupper():
                spell_lower += spell_str[index].lower()
            else:
                spell_lower += spell_str[index]
        spell_str = spell_lower
        print(spell_str)
    elif action_spell == "Illusion":
        #replaced_char_spell = ""
        illusion_index = int(command_list[1])
        illusion_letter = command_list[2]
        if illusion_index < len(spell_str):
            first_part = spell_str[0:illusion_index]
            second_part = spell_str[illusion_index + 1:]
            replaced_char_spell = first_part + illusion_letter + second_part
            spell_str = replaced_char_spell
            # print(spell_str)
            print("Done!")
        else:
            print("The spell was too weak.")
    elif action_spell == "Divination":
        # replaced_substg_spell = ""
        first_substr = command_list[1]
        second_substr = command_list[2]
        if first_substr in spell_str:
            replaced_1_with_2_substg_spell = spell_str.replace(first_substr, second_substr)
            spell_str = replaced_1_with_2_substg_spell
            print(spell_str)
    elif action_spell == "Alteration":
        substr = command_list[1]
        if substr in spell_str:
            replaced_substr_spell = spell_str.replace(substr, "")
            spell_str = replaced_substr_spell
            print(spell_str)
    else:
        print("The spell did not work!")
