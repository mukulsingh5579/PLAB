#Automated "Smart" Folder Organizer
import os
import shutil

path = '/Users/YourName/Downloads'
mapping = {
    'Images': ['.jpg', '.png', '.gif'],
    'Docs': ['.pdf', '.docx', '.txt'],
    'Code': ['.py', '.js', '.html']
}

for filename in os.listdir(path):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in mapping.items():
        if ext in extensions:
            dest = os.path.join(path, folder)
            os.makedirs(dest, exist_ok=True)
            shutil.move(os.path.join(path, filename), os.path.join(dest, filename))