words = input().split(" ")
even_length = [word for word in words if len(word) % 2 == 0]
#print(even_length)
# for word in even_length:
#     print(word)

print("\n".join(even_length))
