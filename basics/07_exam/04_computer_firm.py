computer_count = int(input())
real_sales_count = 0
real_sales_count_all = 0
rating_all_sum = 0
average_rating = 0

for index in range(computer_count):
    number = int(input())
    rating = number % 10
    max_sales_count = number // 10

    rating_all_sum += rating

    if rating == 2:
        real_sales_count = 0
    elif rating == 3:
        real_sales_count = max_sales_count * 0.5
    elif rating == 4:
        real_sales_count = max_sales_count * 0.7
    elif rating == 5:
        real_sales_count = max_sales_count * 0.85
    elif rating == 6:
        real_sales_count = max_sales_count

    real_sales_count_all += real_sales_count


average_rating = rating_all_sum / computer_count
print(f"{real_sales_count_all :.2f}")
print(f"{average_rating :.2f}")
