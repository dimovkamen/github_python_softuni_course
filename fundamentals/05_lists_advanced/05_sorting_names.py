def sort_names(names_string):
    names_list = names_string.split(", ")
    sorted_names = sorted(names_list, key=lambda name: [-len(name), name])
    print(sorted_names)
    return sorted_names


names = input()
result_list = sort_names(names)
