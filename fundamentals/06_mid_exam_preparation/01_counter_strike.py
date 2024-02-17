energy = int(input())
won_battles_count = 0
is_not_enough_energy = False

while True:
    command = input()
    if command == "End of battle":
        break

    distance = int(command)
    if distance <= energy:
        energy -= distance
        won_battles_count += 1
        if won_battles_count % 3 == 0:
            energy += won_battles_count
    else:
        is_not_enough_energy = True
        break

if is_not_enough_energy:
    print(f"Not enough energy! Game ends with {won_battles_count} won battles and {energy} energy")
else:
    print(f"Won battles: {won_battles_count}. Energy left: {energy}")
