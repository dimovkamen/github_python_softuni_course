lines_number = int(input())

heroes_dictionary = {}

for _ in range(lines_number):
    hero_name, hero_hit_p, hero_mana_p = input().split()
    hero_hit_p = int(hero_hit_p)
    hero_mana_p = int(hero_mana_p)
    heroes_dictionary[hero_name] = {"hero_hit_points": hero_hit_p, "hero_mana_points": hero_mana_p}

while True:
    command = input()
    if command == "End":
        break

    action_list = command.split(" - ")
    action = action_list[0]
    hero_name = action_list[1]

    if action == "CastSpell":
        mp_needed = int(action_list[2])
        spell_name = action_list[3]
        if heroes_dictionary[hero_name]["hero_mana_points"] >= mp_needed:
            heroes_dictionary[hero_name]["hero_mana_points"] -= mp_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes_dictionary[hero_name]["hero_mana_points"]} MP!')
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage = int(action_list[2])
        attacker = action_list[3]
        if heroes_dictionary[hero_name]["hero_hit_points"] - damage > 0:
            heroes_dictionary[hero_name]["hero_hit_points"] -= damage
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dictionary[hero_name]["hero_hit_points"]} HP left!')
        else:
            del heroes_dictionary[hero_name]
            print(f'{hero_name} has been killed by {attacker}!')
    elif action == "Recharge":
        amount = int(action_list[2])
        amount_recovered = 0
        if heroes_dictionary[hero_name]["hero_mana_points"] + amount <= 200:
            heroes_dictionary[hero_name]["hero_mana_points"] += amount
            amount_recovered = amount
        else:
            amount_recovered = 200 - heroes_dictionary[hero_name]["hero_mana_points"]
            heroes_dictionary[hero_name]["hero_mana_points"] = 200
        print(f"{hero_name} recharged for {amount_recovered} MP!")
    elif action == "Heal":
        amount = int(action_list[2])
        amount_recovered = 0
        if heroes_dictionary[hero_name]["hero_hit_points"] + amount <= 100:
            heroes_dictionary[hero_name]["hero_hit_points"] += amount
            amount_recovered = amount
        else:
            amount_recovered = 100 - heroes_dictionary[hero_name]["hero_hit_points"]
            heroes_dictionary[hero_name]["hero_hit_points"] = 100
        print(f"{hero_name} healed for {amount_recovered} HP!")


for hero_name, items_list in heroes_dictionary.items():
    print(f"""{hero_name}
  HP: {items_list['hero_hit_points']}
  MP: {items_list['hero_mana_points']}""")
