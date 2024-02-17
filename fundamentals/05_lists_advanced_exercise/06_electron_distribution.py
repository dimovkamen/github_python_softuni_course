electrons_count = int(input())
electrons_in_shells = []

shell_count = 1

while True:
    max_in_current_shell = 2 * (shell_count ** 2)
    if electrons_count > max_in_current_shell:
        electrons_in_shells.append(max_in_current_shell)
        electrons_count -= max_in_current_shell
    else:
        electrons_in_shells.append(electrons_count)
        break

    shell_count += 1

print(electrons_in_shells)
