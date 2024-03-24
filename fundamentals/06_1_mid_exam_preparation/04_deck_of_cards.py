cards_list = input().split(", ")
number = int(input())

for _ in range(number):
    command_list = input().split(", ")
    operation = command_list[0]

    # "Add, {CardName}"
    if operation == "Add":
        card_name_add = command_list[1]
        if card_name_add not in cards_list:
            cards_list.append(card_name_add)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    # "Remove, {CardName}"
    if operation == "Remove":
        card_name_remove = command_list[1]
        if card_name_remove in cards_list:
            cards_list.remove(card_name_remove)
            print("Card successfully removed")
        else:
            print("Card not found")
    # "Remove At, {index}"
    if operation == "Remove At":
        card_index_remove_at = int(command_list[1])
        if 0 <= card_index_remove_at < len(cards_list):
            cards_list.pop(card_index_remove_at)
            print("Card successfully removed")
        else:
            print("Index out of range")
    # "Insert, {index}, {CardName}"
    if operation == "Insert":
        index_insert = int(command_list[1])
        card_name_insert = command_list[2]
        if 0 <= index_insert < len(cards_list):
            if card_name_insert not in cards_list:
                cards_list.insert(index_insert, card_name_insert)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(", ".join(cards_list))
