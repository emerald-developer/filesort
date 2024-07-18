import os
import json
import shutil

def sort_files(config_path):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    source_dir = config.get('source_directory', '.')

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Find the destination directory for this file type
        destination_dir = None
        for dir_path, extensions in config['mappings'].items():
            if extension in extensions:
                destination_dir = dir_path
                break

        # If a destination is found, move the file
        if destination_dir:
            # Create the destination directory if it doesn't exist
            os.makedirs(destination_dir, exist_ok=True)
            
            # Move the file
            shutil.move(file_path, os.path.join(destination_dir, filename))
            print(f"Moved {filename} to {destination_dir}")
        else:
            print(f"No mapping found for {filename}")

if __name__ == "__main__":
    config_path = "fileSortConfig.json"
    sort_files(config_path)