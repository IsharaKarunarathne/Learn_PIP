import shutil
import os

#creating dummy directory for archiving

data_folder = "my_data_for_archieve"

os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)

with open(os.path.join(data_folder, "important.txt"), 'w') as f: 
    f.write("important data")

with open(os.path.join(data_folder, "docs", "notes.md"), 'w') as f: 
    f.write("imeeting notes")
print(f"created {data_folder} for archieving.")

#create a zip archieve
archive_name = "my_data_archieve"

try:
    archive_path = shutil.make_archive(archive_name, 'zip', root_dir=data_folder)
    print(f"archive created: {archive_path}")
    print(f"does archive exist: {os.path.exists(archive_path)}")

except Exception as e:
    print(f"error occured: {e}")


