import os
import shutil

# Prompt the user to input the folder path
source_folder = input("Enter the full path to the folder you want to organize: ").strip()

# Make sure it's a valid folder
if not os.path.isdir(source_folder):
    print("The path entered is not a valid folder.")
    exit()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "ISOs": [".iso", ".img", ".bin", ".cue", ".nrg"],
    "eBooks": [".epub", ".mobi", ".azw3", ".djvu", ".fb2"],
    "Programs": [".exe", ".msi", ".apk", ".dmg", ".pkg"],
    "Others": []
}

# Walk through all subfolders and files
for root, _, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)

        # Skip hidden/system files
        if file.startswith("~") or file.startswith("."):
            continue

        file_ext = os.path.splitext(file)[1].lower()

        # Figure out destination category
        destination_folder = "Others"
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                destination_folder = folder_name
                break

        # Build full path for destination
        dest_folder_path = os.path.join(source_folder, destination_folder)
        os.makedirs(dest_folder_path, exist_ok=True)

        new_file_path = os.path.join(dest_folder_path, file)

        # Only move if it's not already in the right spot
        if os.path.abspath(file_path) != os.path.abspath(new_file_path):
            try:
                shutil.move(file_path, new_file_path)
                print(f"Moved: {file} → {destination_folder}")
            except Exception as e:
                print(f"Failed to move {file}: {e}")
