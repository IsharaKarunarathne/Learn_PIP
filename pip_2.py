import os

new_directory = "./tmp"

print(os.path.basename)

if os.path.exists(new_directory) and os.path.isdir(new_directory):  #check whethere a directory
    os.chdir(new_directory)     #changed to new directory
    print(f"changed directort to: {os.getcwd()}")

else:
    print(f"{new_directory} does not exists")