import os
import shutil

# get the current directory
directory_path = os.getcwd()

# iterate over each item in the directory
for item in os.listdir(directory_path):
    # construct the full item path
    item_path = os.path.join(directory_path, item)

    # only process directories
    if os.path.isdir(item_path):
        # iterate over each file in the directory
        for filename in os.listdir(item_path):
            # construct the full file path
            file_path = os.path.join(item_path, filename)

            # move the file to the parent directory
            shutil.move(file_path, directory_path)
