import os
import shutil

def move_jpg_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for filename in os.listdir(source):
        if filename.endswith(".jpg"):
            shutil.move(os.path.join(source, filename), os.path.join(destination, filename))
            print(f"Moved: {filename}")

# Example usage
move_jpg_files("source_folder", "destination_folder")
