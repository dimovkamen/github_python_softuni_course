# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.

# цвете	               Роза	  Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	3.80	2.80	3	2.50


flowers_type = input()
flowers_count = int(input())
budget = int(input())

prize = 0

# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.


if flowers_type == "Roses":
    if flowers_count > 80:
        prize = flowers_count * 5 * 0.9
    else:
        prize = flowers_count * 5
elif flowers_type == "Dahlias":
    if flowers_count > 90:
        prize = flowers_count * 3.80 * 0.85
    else:
        prize = flowers_count * 3.80
elif flowers_type == "Tulips":
    if flowers_count > 80:
        prize = flowers_count * 2.80 * 0.85
    else:
        prize = flowers_count * 2.80
elif flowers_type == "Narcissus":
    if flowers_count < 120:
        prize = flowers_count * 3.00 * 1.15
    else:
        prize = flowers_count * 3.00
elif flowers_type == "Gladiolus":
    if flowers_count < 80:
        prize = flowers_count * 2.50 * 1.2
    else:
        prize = flowers_count * 2.50

# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".

if prize <= budget:
    reminder = budget - prize
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {reminder:.2f} leva left.")
else:
    not_enough = prize - budget
    print(f"Not enough money, you need {not_enough :.2f} leva more.")