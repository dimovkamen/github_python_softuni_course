film_budget = float(input())
statists_count = int(input())
statist_suit_prize = float(input())

decor_film = film_budget * 0.1
statists_suits_cost = statists_count * statist_suit_prize

if statists_count > 150:
    statists_suits_cost = statists_suits_cost * 0.9

film_money_needed = decor_film + statists_suits_cost

if film_money_needed > film_budget:
    difference_in_budget = film_money_needed - film_budget
    #print("Not enough money!")
    #print(f"Wingard needs {difference_in_budget:.2f} leva more.")
    print(f"Not enough money!\nWingard needs {difference_in_budget:.2f} leva more.")
else:
    budget_more = film_budget - film_money_needed
    #print("Action!")
    #print(f"Wingard starts filming with {budget_more:.2f} leva left.")
    print(f"Action!\nWingard starts filming with {budget_more:.2f} leva left.")
