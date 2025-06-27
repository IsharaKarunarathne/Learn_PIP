import os
file_to_delete = "my_temp_file.txt"

#create a dummy file to check

with open(file_to_delete, 'w') as f:
    f.write("this is a temporary file")

try:
    os.remove(file_to_delete)    #command to dele a file
    print(f"file named: {file_to_delete} removed successfully")

except FileNotFoundError:
     print(f"file named: {file_to_delete} not exist")

except Exception as e:
    print(f"error occured: {e}")