import os

full_path = "/home/user/documents/reports.txt"

directory_name = os.path.dirname(full_path)

basename = os.path.basename(full_path)


print(f"directory name: {directory_name}")
print(f"basename: {basename}")