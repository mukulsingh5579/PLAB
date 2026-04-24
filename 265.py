#Automated File Organizer
import os
import shutil

path = "./my_downloads"  # Change to your target folder
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for file in files:
    ext = file.split(".")[-1].lower()
    folder_path = os.path.join(path, ext)
    
    os.makedirs(folder_path, exist_ok=True)
    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

print("Files organized by extension!")