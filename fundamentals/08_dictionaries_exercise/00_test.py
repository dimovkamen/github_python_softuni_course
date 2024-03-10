# get
# keys
# values
# items
# copy     --> create new dictionary
# fromkeys --> create dictionary with keys with the same value
# pop     --> takes and deletes element
# popitem --> takes and deletes last one
# clear vs del
# setdefault
# update  --> add elements from other dictionary
# zip     --> from 2 lists make dictionary key(first list) value(second list)

dictionary_1 = dict.fromkeys(["a", "b", "c"], 5)
print(dictionary_1)

element_a = dictionary_1.pop("a")

print(element_a)
print(dictionary_1)

element_last = dictionary_1.popitem()
print(element_last)
print(dictionary_1)

#value = dictionary_1.setdefault("d", 0)
value = 0
dictionary_1["d"] = value

print(value)
print(dictionary_1)

dictionary_1.update({"z": 3, "y" : 5})
print(dictionary_1)

print()
dictionary_5 = [1, 2, 3]
dictionary_6 = ["apple", "banana", "kiwi"]
zip_dictionary = dict(zip(dictionary_5, dictionary_6))
print(zip_dictionary)
