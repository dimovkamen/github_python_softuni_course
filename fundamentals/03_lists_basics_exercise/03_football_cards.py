players_list = input().split()

sendoff_players_a = []
sendoff_players_b = []

players_count_a = 11
players_count_b = 11

is_match_terminated = False

for player in players_list:
    team = player[0]
    if team == "A":
        if player not in sendoff_players_a:
            players_count_a -= 1
            sendoff_players_a.append(player)
    elif team == "B":
        if player not in sendoff_players_b:
            players_count_b -= 1
            sendoff_players_b.append(player)

    if players_count_a < 7 or players_count_b < 7:
        is_match_terminated = True
        break

print(f"Team A - {players_count_a}; Team B - {players_count_b}")
if is_match_terminated:
    print("Game was terminated")
