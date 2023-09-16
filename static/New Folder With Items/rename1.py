import os
import re

# get the current directory
directory_path = os.getcwd()

# iterate over each file in the directory
for filename in os.listdir(directory_path):
    # construct the full file path
    file_path = os.path.join(directory_path, filename)

    # only process Markdown files
    if os.path.isfile(file_path) and filename.endswith('.md'):
        # make filename lowercase
        new_name = filename.lower()

        # remove string of 32 alphanumeric characters (assuming it's a MD5 hash)
        new_name = re.sub(r'[a-f0-9]{32}', '', new_name)

        # replace any spaces with dashes
        new_name = new_name.replace(' ', '-')

        # remove any existing dash
        new_name = new_name.replace('--', '-')

        # construct the new file path
        new_file_path = os.path.join(directory_path, new_name)

        # rename the file
        os.rename(file_path, new_file_path)
