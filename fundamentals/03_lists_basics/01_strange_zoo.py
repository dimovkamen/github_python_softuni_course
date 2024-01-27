
# tail = input()
# body = input()
# head = input()

#meerkat = [head, body, tail]

#meerkat[2], meerkat[0] = meerkat[0], meerkat[2]

meerkat = []
for _ in range(3):
    data = input()
    meerkat.append(data)

#meerkat = meerkat[::-1]
meerkat.reverse()

print(meerkat)

