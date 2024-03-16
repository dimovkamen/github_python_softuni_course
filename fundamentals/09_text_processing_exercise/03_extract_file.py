path_str = input()
from_index = path_str.rindex('\\')
file = path_str[from_index+1:]
only_filename, only_extension = file.split(".")
print(f"File name: {only_filename}")
print(f"File extension: {only_extension}")