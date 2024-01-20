maiden_party_price = float(input())
love_texts_count = int(input())
wax_roses_count = int(input())
key_holders_count = int(input())
caricature_count = int(input())
luck_surprises_count = int(input())

all_items_count = luck_surprises_count + wax_roses_count + key_holders_count + caricature_count + luck_surprises_count

all_items_price = (love_texts_count * 0.60 +
                   wax_roses_count * 7.20 +
                   key_holders_count * 3.60 +
                   caricature_count * 18.20 +
                   luck_surprises_count * 22)

if all_items_count >= 25:
    all_items_price *= 0.65

money_won = all_items_price * 0.9

difference = abs(money_won - maiden_party_price)
if money_won >= maiden_party_price:
    print(f"Yes! {difference :.2f} lv left.")
else:
    print(f"Not enough money! {difference :.2f} lv needed.")
