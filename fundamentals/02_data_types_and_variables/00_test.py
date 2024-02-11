# list [,,]                --> ordered (index), allow duplicates
# dictionary { :, :, : }   --> key value
# tuple (,,)               --> like list but immutable, unchangeable
# set {,,}                 --> unordered (no indexed), duplicates are not printed


# list1 = [123, 0.5, 'bus', "A"]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print()
# list1[2] = "Car"
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])

# dictionary1 = {'name': 'Kamen', 'age': 23, 'height': 180.3}
#
# print(dictionary1['name'])
# print(dictionary1['age'])
# print(dictionary1['height'])
#
# print(type(dictionary1))
#
# print(isinstance(dictionary1['name'], str))
#
# if 'a' in 'abc':
#     print('Yes')
# else:
#     print('No ')
#
#
# cars = [ ['mercedes', 'opel'], ["audi", "vw"]]
# print(cars[1][1])
#
# example_tuple = ( "apple", "cherry", "banana")
# print(example_tuple[1])



# set1 = {"car", "dog", "cat"}
# set1.add("dog")
# set1.add("puppy")
# print(set1)
#
#
# list1 = [123, 0.5, 'bus', "A"]
# list1.insert(1, "alo")
# list1[0] = 345
# print(list1)


# parm = None
# if parm is None:
#     print("Yes")
# else:
#     print("No")

word = "123"
digits_set = set(word)
print(len(digits_set))