# my code

money_needed_for_trip = float(input())
money_currently = float(input())

spend_days_count = 0
is_failed_to_save_money = False
all_days = 0

while money_needed_for_trip > money_currently:
    all_days += 1

    action = input()  # "spend" "save";
    sum_spend_save_for_the_day = float(input())
    if action == "spend":
        spend_days_count += 1
        if money_currently > sum_spend_save_for_the_day:
            money_currently -= sum_spend_save_for_the_day
        else:
            money_currently = 0
    elif action == "save":
        money_currently += sum_spend_save_for_the_day
        spend_days_count = 0

    if spend_days_count >= 5:
        is_failed_to_save_money = True
        break

if is_failed_to_save_money:
    print("You can't save the money.")
    print(all_days)
else:
    print(f"You saved the money for {all_days} days.")
