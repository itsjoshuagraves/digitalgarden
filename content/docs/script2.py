import os
import re
import datetime

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

        # regex pattern for the entire block
        block_pattern = r"(# .*?\nCreated: .*?\n\[Original post\].*?\nPublication: .*?\nTags: .*?\n)"
        blocks = re.findall(block_pattern, text, re.DOTALL)

        for block in blocks:
            # regex patterns for each line
            title_pattern = r"# (.*)"
            date_pattern = r"Created: (.*)"
            link_pattern = r"\[Original post\]\((.*)\)"
            pub_pattern = r"Publication: (.*)"
            tags_pattern = r"Tags: (.*)"

            # find matches
            title_match = re.search(title_pattern, block)
            date_match = re.search(date_pattern, block)
            link_match = re.search(link_pattern, block)
            pub_match = re.search(pub_pattern, block)
            tags_match = re.search(tags_pattern, block)

            if title_match and date_match and link_match and pub_match and tags_match:
                # convert the date to YYYY-MM-DD format
                date = datetime.datetime.strptime(date_match.group(1), "%B %d, %Y")
                date_str = date.strftime("%Y-%m-%d")

                # format the tags as a list
                tags_str = tags_match.group(1).replace(",", "")

                # format the block
                replacement = f"""---
date: {date_str}
link title: {title_match.group(1)}
title: {title_match.group(1)}
weight: 10
tags: {tags_str}
originalURL: {link_match.group(1)}
---

{link_match.group(0)}
"""
                # replace the original block with the formatted block
                text = text.replace(block, replacement)

        # write the transformed text back to the same file
        with open(file_path, 'w') as file:
            file.write(text)
