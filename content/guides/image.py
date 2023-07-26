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
        with open(file_path, 'r') as file:
            text = file.read()

        # regex pattern for the image link
        img_pattern = r"!\[.*\]\((.*?)/(.*?)\)"
        img_matches = re.findall(img_pattern, text)

        for match in img_matches:
            # format the new image link
            new_img_link = f"![Photo Caption Coming](../../img/{match[1]})"
            
            # replace the old image link with the new one
            text = text.replace(f"![{match[0]}]", new_img_link)

        # write the transformed text back to the same file
        with open(file_path, 'w') as file:
            file.write(text)
