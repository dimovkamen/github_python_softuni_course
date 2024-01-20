actor_name = input()
academy_points = float(input())
evaluate_count = int(input())

points_sum = academy_points

for index in range(evaluate_count):
    evaluate_name = input()
    evaluate_points = float(input())
    name_length = len(evaluate_name)
    points_given_by_eval = name_length * evaluate_points / 2
    points_sum +=points_given_by_eval
    if points_sum > 1250.5:
        break

if points_sum > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points_sum :.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - points_sum :.1f} more!")
