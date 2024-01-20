username = input()
password = input()

password_to_enter = input()
while password_to_enter != password:
    password_to_enter = input()

print(f"Welcome {username}!")
