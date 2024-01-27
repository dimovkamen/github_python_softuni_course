lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_break_count = lost_fights_count // 2
sword_break_count = lost_fights_count // 3
shield_break_count = lost_fights_count // (2 * 3)
armor_break_count = shield_break_count // 2

expenses = (helmet_price * helmet_break_count +
            sword_price * sword_break_count +
            shield_price * shield_break_count +
            armor_price * armor_break_count)

print(f"Gladiator expenses: {expenses :.2f} aureus")
