import os

path_comp_1 = "C:/Learn_PIP" 
path_comp_2 = "tmp"
file_name = "monthly report.pdf"

full_path = os.path.join(path_comp_1, path_comp_2, file_name)
print(f"joined path: {full_path}")