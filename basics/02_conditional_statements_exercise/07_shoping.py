budget = float(input())
video_card_count = int(input())
cpu_count = int(input())
ram_count = int(input())

video_card_prize = video_card_count * 250
cpu_prize = cpu_count * (video_card_prize * 0.35)
ram_prize = ram_count * (video_card_prize * 0.1)

sum_total = video_card_prize + cpu_prize + ram_prize

if video_card_count > cpu_count:
    sum_total = sum_total * 0.85

if budget >= sum_total:
    print(f"You have {(budget - sum_total):.2f} leva left!")
else:
    print(f"Not enough money! You need {(sum_total - budget):.2f} leva more!")
