import os

# Source Directory
source_path = "./Samrajya_Audio"

# Target Directory
target_path = "./raw_data/raw_audio"

def Rename_Files():
    # Index to track file number
    index = 26

    # Iteration through each file in the given directory
    for filename in os.listdir(source_path):
        
        # Constructing the old file path 
        # This is necessary because to perform any operations on the file (like renaming it, moving it, or reading from it)
        # you need the complete path to the file.
        # os.listdir(old_path) only gives the file name and not the path

        old_file_path = os.path.join(source_path, filename)

        # Renaming the files
        new_file_name = f"audio_sample_{index}.wav"

        # Increasing the index
        index += 1

        # Constructing the new file path
        new_file_path = os.path.join(target_path, new_file_name)

        # Moving and Renaming the file
        os.rename(old_file_path, new_file_path)


Rename_Files()

