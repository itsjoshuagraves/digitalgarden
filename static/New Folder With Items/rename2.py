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

        # regex pattern for the metadata
        title_pattern = r"title: (.*?)\n"
        date_pattern = r"date: (.*?)\n"

        # find the metadata in the text
        title_search = re.search(title_pattern, text)
        date_search = re.search(date_pattern, text)

        # check if 'Title:' and 'Date:' fields are present, if not, skip this file
        if title_search and date_search:
            title = title_search.group(1)
            date = date_search.group(1)

            # generate the new filename
            new_filename = f"{date}-{title.replace(' ', '-').replace('“','').replace('”','').lower()}.md"
            new_file_path = os.path.join(directory_path, new_filename)

            # rename the file
            os.rename(file_path, new_file_path)
