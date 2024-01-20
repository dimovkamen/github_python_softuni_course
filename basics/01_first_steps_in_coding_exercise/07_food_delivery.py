CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15

DELIVERY_PRICE = 2.50

chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

all_menus_sum = chicken_menu_count * CHICKEN_MENU + fish_menu_count * FISH_MENU + vegetarian_menu_count * VEGETARIAN_MENU
desert_price = all_menus_sum * 0.2

final_price = all_menus_sum + desert_price + DELIVERY_PRICE

print(f"{final_price :.2f}")