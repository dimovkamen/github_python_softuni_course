first_str, second_str = input().split()

min_length = min(len(first_str), len(second_str))
max_length = max(len(first_str), len(second_str))

sum_chars = 0

for index in range(0, max_length):
    if index < min_length:
        sum_chars += ord(first_str[index]) * ord(second_str[index])
    else:
        if len(first_str) > min_length:
            sum_chars += ord(first_str[index])
        if len(second_str) > min_length:
            sum_chars += ord(second_str[index])

print(sum_chars)
