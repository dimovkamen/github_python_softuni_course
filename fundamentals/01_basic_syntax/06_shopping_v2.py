budget = int(input())
command = input()

while command != 'End':
    # if price_product == 'End':
    #     print("You bought everything needed.")
    #     break
    price_product = int(command)
    budget -= price_product
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
