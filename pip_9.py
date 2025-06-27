import os

folder_to_remove = "empty_folder_to_delete"
os.mkdir(folder_to_remove)


try:
    os.rmdir(folder_to_remove)   #remove directory
    print(f"directory; {folder_to_remove} removed successfully")

except OSError as e:
    print(f"error removing directory; {folder_to_remove}: {e}")