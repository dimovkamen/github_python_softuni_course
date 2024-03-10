products_dictionary = {}

while True:
    command = input()

    if command == "buy":
        break

    product_list = command.split()

    product = product_list[0]
    price = float(product_list[1])
    quantity = int(product_list[2])

    if product in products_dictionary:
        products_dictionary[product][0] = price
        products_dictionary[product][1] += quantity
    else:
        products_dictionary[product] = [price, quantity]

for product, items in products_dictionary.items():
    price = products_dictionary[product][0] * products_dictionary[product][1]
    print(f"{product} -> {price :.2f}")

# print(products_dictionary)
