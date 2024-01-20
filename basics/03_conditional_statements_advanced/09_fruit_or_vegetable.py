product_name = input()

if product_name == "banana" \
    or product_name == "apple"  \
    or product_name == "kiwi"  \
    or product_name == "cherry" \
    or product_name == "lemon" \
    or product_name == "grapes":
    type = "fruit"
elif product_name == "tomato" \
    or product_name == "cucumber"  \
    or product_name == "pepper"  \
    or product_name == "carrot":
    type = "vegetable"
else:
    type = "unknown"

print(type)
