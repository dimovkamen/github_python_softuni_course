# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

projection_type = input()
rows = int(input())
columns = int(input())
price = 0

if projection_type == "Premiere":
    price = 12.00
elif projection_type == "Normal":
    price = 7.50
elif projection_type == "Discount":
    price = 5.00

total_income = price * rows * columns

print(f"{total_income :.2f} leva")
