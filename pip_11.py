import os

old_name = "old.txt"
new_name = "new.txt"

with open(old_name, 'w') as f:
    f.write("am the old file")

try:
    os.rename(old_name, new_name)
    print(f"renamed file as: {old_name} to {new_name}")
    with open(new_name, 'w') as f:
        f.write("am the new file")

except FileNotFoundError:
    print(f"{old_name} does not exist")

except FileExistsError:
    print(f"{new_name} already there")

except Exception as e:
    print(f"error occured: {e}")


