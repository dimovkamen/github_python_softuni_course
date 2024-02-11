def sum_numbers(n1, n2):
    return n1 + n2


def subtract(a, b):
    return a - b


def add_and_subtract(n1, n2, n3):
    return subtract(sum_numbers(n1, n2), n3)


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(add_and_subtract(n1, n2, n3))
