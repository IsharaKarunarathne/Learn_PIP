import shutil
import os

source_dir = "my_source_project"

os.makedirs(os.path.join(source_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(source_dir, "js"), exist_ok=True)

with open(os.path.join(source_dir, "index.html"), 'w') as f: 
    f.write("<html><html>")

with open(os.path.join(source_dir, "css", "style.css"), 'w') as f: 
    f.write("body{}")
print(f"created dummy source directory: {source_dir}")

#copy the directory tree
destination_dir = "my_backup_project"

try: 
    shutil.copytree(source_dir, destination_dir)
    print(f"{source_dir} copied to {destination_dir} successfully")

    print("contents of destination directory")
    for root, dirs, files in os.walk(destination_dir):
        level = root.replace(destination_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level+1)
        for f in files:
            print(f"{sub_indent}{f}")

except FileExistsError:
    print(f"{destination_dir} already exist")

except Exception as e:
    print(f"error occured during copytree: {e}")

#cleanup
if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir) #use rmtree as target_dir now contain

if os.path.exists(source_dir):
    shutil.rmtree(source_dir) 
print("cleaned up dummy directory")
