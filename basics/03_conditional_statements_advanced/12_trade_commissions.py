city = input()
sales = float(input())
commission_percent = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        commission_percent = 5
    elif 500 < sales <= 1000:
        commission_percent = 7
    elif 1000 < sales <= 10000:
        commission_percent = 8
    elif 10000 < sales:
        commission_percent = 12
elif city == "Varna":
    if 0 <= sales <= 500:
        commission_percent = 4.5
    elif 500 < sales <= 1000:
        commission_percent = 7.5
    elif 1000 < sales <= 10000:
        commission_percent = 10
    elif 10000 < sales:
        commission_percent = 13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission_percent = 5.5
    elif 500 < sales <= 1000:
        commission_percent = 8
    elif 1000 < sales <= 10000:
        commission_percent = 12
    elif 10000 < sales:
        commission_percent = 14.5

if commission_percent != 0:
    commission = sales * commission_percent/100
    print(f"{commission :.2f}")
else:
    print("error")
