import os
import pandas as pd

# Define Directories
audio = './data/audio'
transcript = './data/transcripts'

# Get list of audio and transcript files
audio_files =  sorted([f for f in os.listdir(audio) if f.endswith('wav')])
transcript_files = sorted([f for f in os.listdir(transcript) if f.endswith('txt')])

# Ensure each list has same no of files
if len(audio_files) != len(transcript_files):
    raise ValueError('The length of audio files do not match the lenght of transcript files')

# Creating a Dictionary which consists of two keys that holds the location for all files
data =  {
           "audio_file" : [os.path.join(audio, f).replace('\\', '/') for f in audio_files],
           "transcript_file" : [os.path.join(transcript, f).replace('\\', '/') for f in transcript_files] 
        }

# Creating the DataFrame
df = pd.DataFrame(data)

# Converting DataFrame to CSV
df.to_csv("./data/metadata/data.csv", index=False)


