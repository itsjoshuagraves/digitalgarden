import os
import glob

def rename_files():
    # Get a list of all files in the current directory
    files = glob.glob('*')

    for filename in files:
        # Split the filename at the underscore character
        split_filename = filename.split('_')

        # If there's an underscore in the filename
        if len(split_filename) > 1:
            # The new filename is everything after the first underscore
            new_filename = '_'.join(split_filename[1:])
            # Rename the file
            os.rename(filename, new_filename)

rename_files()
