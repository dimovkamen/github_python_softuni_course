PENCIILS_PRICE = 5.8
MARKERS_PRICE = 7.2
CLEANER_PRICE = 1.2

pencils = int(input())
markers = int(input())
cleaner_liters = int(input())
percent_discount = int(input())

pencils_sum = float(pencils * PENCIILS_PRICE)
markers_sum = float(markers * MARKERS_PRICE)
cleaners_sum = float(cleaner_liters * CLEANER_PRICE)

sum_all = pencils_sum + markers_sum + cleaners_sum
sum_all_with_discount = sum_all - (sum_all * (percent_discount / 100))

print(f'{sum_all_with_discount:.2f}')
