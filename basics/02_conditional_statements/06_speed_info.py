# Да се напише програма, която чете скорост (реално число), въведена от потребителя и отпечатва информация за скоростта.
# •	При скорост до 10 (включително) отпечатайте "slow"
# •	При скорост над 10 и до 50 (включително) отпечатайте "average"
# •	При скорост над 50 и до 150 (включително) отпечатайте "fast"
# •	При скорост над 150 и до 1000 (включително) отпечатайте "ultra fast"
# •	При по-висока скорост отпечатайте "extremely fast"

real_speed = float(input())

if real_speed <= 10:
    print("slow")
elif real_speed <= 50:
    print("average")
elif real_speed <= 150:
    print("fast")
elif real_speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")