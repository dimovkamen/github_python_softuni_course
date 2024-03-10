countries_list = input().split(", ")
capitals_list = input().split(", ")

dict_countries_capitals = dict(zip(countries_list, capitals_list))

for key, value in dict_countries_capitals.items():
    print(f"{key} -> {value}")
