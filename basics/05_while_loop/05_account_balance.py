payment = input()
total_sum = 0

while payment != "NoMoreMoney":
    payment_float = float(payment)
    if payment_float < 0:
        print("Invalid operation!")
        break
    total_sum += payment_float
    print(f"Increase: {payment_float :.2f}")
    payment = input()

print(f"Total: {total_sum :.2f}")
