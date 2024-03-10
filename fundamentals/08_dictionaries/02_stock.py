products_input = input().split(" ")
stocks_d = {}

for index in range(0, len(products_input), 2):
    key = products_input[index]
    value = int(products_input[index + 1])
    stocks_d[key] = value

search_products = input().split(" ")

for product in search_products:
    if product in stocks_d.keys():
        quantity = stocks_d[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
