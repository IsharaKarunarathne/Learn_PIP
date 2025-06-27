import shutil
import os

source_file = "source_doc.txt"

with open(source_file, 'w') as f: 
    f.write("original content")
print(f"created {source_file} for copying.")

destination_file = "copied_doc.txt"

try:
    shutil.copy(source_file, destination_file)
    print(f"{source_file} copied to destination file: {destination_file}")
    print(f"content of {destination_file}: {open(destination_file)}")

except FileNotFoundError:
    print(f" source fle named{source_file} not found")

except Exception as e:
    print(f"error occured: {e}")


if os.path.exists(source_file):
    os.remove(source_file)
if os.path.exists(destination_file):
    os.remove(destination_file)
print("cleaned up dummy directory")