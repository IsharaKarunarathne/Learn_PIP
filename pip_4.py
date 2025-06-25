import os

path_to_check_file = r"C:\Learn_PIP\my_existing_file.txt"
path_to_check_directory = r"C:\Learn_PIP"


with open(path_to_check_file, 'w') as f:
    f.write("Hello-892")
os.makedirs(path_to_check_directory, exist_ok = True)

if os.path.exists(path_to_check_file):
    print(f" {path_to_check_file} exists")
else:
    print(f" {path_to_check_file} does not exists")


if os.path.exists(path_to_check_directory):
    print(f" {path_to_check_directory} exists")
else:
    print(f" {path_to_check_directory} does not exists")