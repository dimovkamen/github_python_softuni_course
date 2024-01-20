# 1.	dog -> mammal
# 2.	crocodile, tortoise, snake -> reptile
# 3.	others -> unknown

animal_name = input()

if animal_name == "dog":
    print("mammal")
elif animal_name == "crocodile" or animal_name == "tortoise" or animal_name == "snake":
    print("reptile")
else:
    print("unknown")
