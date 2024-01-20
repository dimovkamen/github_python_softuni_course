# •	"Mr." – мъж (пол 'm') на 16 или повече години
# •	"Master" – момче (пол 'm') под 16 години
# •	"Ms." – жена (пол 'f') на 16 или повече години
# •	"Miss" – момиче (пол 'f') под 16 години

age = float(input())
sex = input()

if age >= 16:
    if sex == "m":
        print("Mr.")
    else:
        print("Ms.")
else:
    if sex == "m":
        print("Master")
    else:
        print("Miss")
