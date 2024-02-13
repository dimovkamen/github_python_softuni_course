def sort_names(names_string):
    names_list = names_string.split(", ")
    #                            Kamen, Ivan, Petar --> [5,"Kamen"] | [4,"Ivan"] | [5,"Petar"] --> [5,"Kamen"]  [5,"Petar"] [4,"Ivan"]
    sorted_names = sorted(names_list, key=lambda name: [-len(name), name])
    print(sorted_names)
    return sorted_names


names = input()
result_list = sort_names(names)
