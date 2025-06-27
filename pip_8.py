import os

new_folder_name = "my_new_folder"

try:
    os.mkdir(new_folder_name)
    print(f"directory; {new_folder_name} created successfully")

except FileExistsError:
    print(f"directory; {new_folder_name} already exist")

except Exception as e:
    print(f"error occured; {e} ")