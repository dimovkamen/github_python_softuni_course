dictionary_1 = {"name": "Kamen", "age": 40, "car": "Audi", 20: "number"}
print(dictionary_1)
dictionary_1["age"] = 30
dictionary_1[20] = "opa"
print(dictionary_1)
print(dictionary_1["car"])

dictionary_2 = dict(name="Ivan", age=35)
print(dictionary_2)

del dictionary_2['age']
print(dictionary_2)

print(dictionary_1.get("aaa"))

if "age" in dictionary_1.keys():
    print("yes")
else:
    print("No")

print()
for key in dictionary_1.keys():
    print(f"{key} --> {dictionary_1[key]}")

print(list(dictionary_1)[3])

print()
for value in dictionary_1.values():
    print(f"{value}")


print()
for key, value in dictionary_1.items():
    print(f"{key} --> {value}")

# dictionary_1.clear()
# print(dictionary_1)

dictionary_3 = dictionary_1.copy()
dictionary_3["name"] = "Kiro"
print(dictionary_1)
print(dictionary_3)

print(dictionary_1.popitem())
print(dictionary_1)
