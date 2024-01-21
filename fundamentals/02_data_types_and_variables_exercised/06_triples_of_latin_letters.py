num = int(input())

# 97 --> a
# 98 --> b
# ..

for x in range(97, 97 + num):
    for y in range(97, 97 + num):
        for z in range(97, 97 + num):
            print(f"{chr(x)}{chr(y)}{chr(z)}")
