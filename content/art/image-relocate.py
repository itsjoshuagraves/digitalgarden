import os
import re

# get the current directory
directory_path = os.getcwd()

# regex pattern for the image link
image_pattern = r'!\[\]\((.*?)\)'

# iterate over each file in the directory
for filename in os.listdir(directory_path):
    # construct the full file path
    file_path = os.path.join(directory_path, filename)

    # only process Markdown files
    if os.path.isfile(file_path) and filename.endswith('.md'):
        with open(file_path, 'r') as file:
            text = file.read()

        # split the text into header and body
        header, body = text.split('---\n', 1)

        # search for the first image link in the body
        image_search = re.search(image_pattern, body)

        # if an image link is found
        if image_search:
            # remove the image link from the body
            body = body.replace(image_search.group(0), '', 1)

            # add the image link to the header
            header += f'image: {image_search.group(1)}\n'

        # join the header and body back together
        new_text = '---\n'.join([header, body])

        # write the transformed text back to the file
        with open(file_path, 'w') as file:
            file.write(new_text)
