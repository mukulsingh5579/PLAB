import os
import shutil
from pathlib import Path

def organize_folder(target_dir):
    # Define your mappings here
    EXTENSION_MAP = {
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
        '.pdf': 'Documents', '.docx': 'Documents', '.txt': 'Documents', '.xlsx': 'Documents',
        '.mp3': 'Audio', '.wav': 'Audio',
        '.zip': 'Archives', '.tar': 'Archives', '.gz': 'Archives'
    }
    
    target_path = Path(target_dir)
    if not target_path.exists():
        print("The specified directory does not exist.")
        return

    for file_path in target_path.iterdir():
        # Skip directories
        if file_path.is_dir():
            continue
            
        # Get the file extension
        ext = file_path.suffix.lower()
        
        if ext in EXTENSION_MAP:
            folder_name = EXTENSION_MAP[ext]
            dest_folder = target_path / folder_name
            
            # Create the destination folder if it doesn't exist
            dest_folder.mkdir(exist_ok=True)
            
            # Move the file
            shutil.move(str(file_path), str(dest_folder / file_path.name))
            print(f"Moved: {file_path.name} -> {folder_name}/")

# Example usage (Replace with your actual path)
# organize_folder("/Users/yourname/Downloads")