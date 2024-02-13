unsorted_list = ['2-Walk the dog', '1-Drink coffee', '6-Dinner', '10-Work']
print(unsorted_list)
sorted_list = sorted(unsorted_list, key=lambda list_element: int(list_element.split('-')[0]))
print(sorted_list)
sorted_list = [note.split("-")[1] for note in sorted_list]
print(sorted_list)
