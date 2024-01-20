command = input()

while command != "End":
    destination = command
    minimum_budget = float(input())
    saved_sum_total = 0

    while saved_sum_total < minimum_budget:
        next_saved_sum = float(input())
        saved_sum_total += next_saved_sum

    print(f"Going to {destination}!")

    command = input()
