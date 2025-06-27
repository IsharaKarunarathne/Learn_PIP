import shutil
import os

file_to_move = "repot.pdf"
target_dir = "archives"

with open(file_to_move, 'w') as f:
    f.write("confidential data")

os.makedirs(target_dir, exist_ok=True) #create total path for the targeted directory
print(f"created: {file_to_move} and {target_dir}")


try:
    shutil.move(file_to_move, target_dir)
    print(f"{file_to_move} moved to the {target_dir} successfully")
    print(f"new path:{os.path.join(target_dir, file_to_move)}")

except FileNotFoundError:
    print(f" source fle named{file_to_move} not found")

except Exception as e:
    print(f"error occured: {e}")


#cleanup
if os.path.exists(target_dir):
    shutil.rmtree(target_dir) #use rmtree as target_dir now contain
print ("cleaned up dummy directory")