import os

def rename_m3u8_to_ts(directory):
    ext1 = input("Enter the old extension");
    ext2 = input("Enter the new extension");
    # List all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file has a old extension
        if filename.endswith(ext1):
            # Construct the new filename with .new extension
            new_filename = filename.replace(ext1, ext2)
            # Create full path for the old and new filenames
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # Rename the file   
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Get input from the user
directory = input("Please enter the path that contains the files: ")

rename_m3u8_to_ts(directory)


# /home/rahul/Downloads/Week0