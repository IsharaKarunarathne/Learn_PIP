import os


path1 = r"C:\Learn_PIP\my_existing_file.txt"
path2 = r"C:\Learn_PIP"
path3 = "no.txt"

print(f"{path1} is a file: {os.path.isfile(path1)}")
print(f"{path1} is a directory: {os.path.isdir(path1)}")

print(f"{path2} is a file: {os.path.isfile(path2)}")
print(f"{path2} is a directory: {os.path.isdir(path2)}")

print(f"{path3} is a file: {os.path.isfile(path3)}")
print(f"{path3} is a directory: {os.path.isdir(path3)}")