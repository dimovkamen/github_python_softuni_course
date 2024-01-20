paper_roll_price = 5.80
cloth_roll_price = 7.20
glue_liter_price = 1.20

paper_rolls_count = int(input())
cloth_rolls_count = int(input())
glue_liters_count = float(input())
percentage_discount = int(input())

paper_final_price = paper_rolls_count * paper_roll_price
cloth_final_price = cloth_rolls_count * cloth_roll_price
glue_final_price = glue_liters_count * glue_liter_price

all_final_price = paper_final_price + cloth_final_price + glue_final_price
all_final_price_with_discount = all_final_price * (100 - percentage_discount)/100

print(f"{all_final_price_with_discount :.3f}")
