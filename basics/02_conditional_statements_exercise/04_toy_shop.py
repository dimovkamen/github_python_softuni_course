vacation_cost = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

toys_count_all = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count
money_total = (puzzles_count * 2.60
               + talking_dolls_count * 3
               + teddy_bears_count * 4.10
               + minions_count * 8.20
               + trucks_count * 2)

if toys_count_all >= 50:
    money_total *= 0.75

money_total *= 0.90

if money_total >= vacation_cost:
    print(f"Yes! {(money_total - vacation_cost) :.2f} lv left.")
else:
    print(f"Not enough money! {(vacation_cost - money_total) :.2f} lv needed.")
