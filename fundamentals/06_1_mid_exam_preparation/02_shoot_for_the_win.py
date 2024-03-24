targets_list = list(map(int, input().split()))
count_shooted_targets = 0

while True:
    command = input()
    if command == "End":
        break

    target_index = int(command)

    if target_index < len(targets_list):
        current_target_score = targets_list[target_index]
        if current_target_score != -1:
            for index, target in enumerate(targets_list):
                if target_index == index:
                    targets_list[target_index] = -1
                    count_shooted_targets += 1
                elif targets_list[index] != -1 and targets_list[index] > current_target_score:
                    targets_list[index] -= current_target_score
                elif targets_list[index] != -1 and targets_list[index] <= current_target_score:
                    targets_list[index] += current_target_score

final_targets_string = " ".join(list(map(str,targets_list)))
print(f"Shot targets: {count_shooted_targets} -> {final_targets_string}")
