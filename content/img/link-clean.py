import os
import re

# get the current directory
directory_path = os.getcwd()

# regex pattern for the image link
pattern = r'\!\[.*?\]\((.*?)\)'
new_path_prefix = '/img/'

# iterate over each file in the directory
for filename in os.listdir(directory_path):
    # construct the full file path
    file_path = os.path.join(directory_path, filename)

    # only process Markdown files
    if os.path.isfile(file_path) and filename.endswith('.md'):
        with open(file_path, 'r') as file:
            text = file.read()

        # replace image paths in the text
        new_text = re.sub(pattern, lambda m: f'![]({new_path_prefix}{os.path.basename(m.group(1))})', text)

        # write the transformed text back to the file
        with open(file_path, 'w') as file:
            file.write(new_text)
