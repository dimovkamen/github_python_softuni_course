import re

pattern_pass = r'(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<^>]{3})<\1'
inputs_number = int(input())

for _ in range(inputs_number):
    password_str = input()
    passwords_list = re.findall(pattern_pass, password_str)
    # print(passwords_list)
    if len(passwords_list) > 0:
        encrypt_password = passwords_list[0][1] + passwords_list[0][2] + passwords_list[0][3] + passwords_list[0][4]
        print(f"Password: {encrypt_password}")
    else:
        print("Try another password!")
