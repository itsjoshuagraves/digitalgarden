import os
import re
from datetime import datetime

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

        # regex pattern for the metadata
        title_pattern = r"# (.*?)\n"
        tags_pattern = r"Tags: (.*?)\n"
        date_pattern = r"Date: (\d{4})"

        # find the metadata in the text
        title_search = re.search(title_pattern, text)
        tags_search = re.search(tags_pattern, text)
        date_search = re.search(date_pattern, text)

        # check if 'Title:', 'Tags:', and 'Date:' fields are present, if not, use a default value
        title = title_search.group(1) if title_search else 'No Title'
        tags = tags_search.group(1) if tags_search else 'No Tags'
        year = date_search.group(1) if date_search else '0000'

        # create the new metadata block
        new_metadata = f"""---
title: {title}
tags: [{tags}]
date: {year}-01-01
---

"""

        # replace the old metadata with the new one
        text = re.sub(title_pattern + ".*?" + date_pattern, new_metadata, text, flags=re.DOTALL)

        # write the transformed text back to the file
        with open(file_path, 'w') as file:
            file.write(text)
