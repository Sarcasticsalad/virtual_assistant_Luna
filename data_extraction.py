import sys
import re
import json
import argparse
import subprocess

# Sentence Splitter
def sentence_splitter(text):
    return list(filter(None, [s.strip() for s in re.split(r'[\n\.!\?]+',text)]))

# Extract Utternace with timestamps
def extract_utternace(transcript, alignment):
    aligned = json.loads(open(alignment).read())
    sentences = sentence_splitter(open(transcript).read())
    utterance_timestamp = []
    timestamp = []
    i = 0
    for s in sentences:
        words = s.replace('-',' ').split()
        for w in words:
            w = w.replace(',','')
            a = aligned['words'][i]['word']
            if a == w:
                if aligned['words'][i]['case'] == 'success':
                    timestamp.append([w, aligned['words'][i]['start'], aligned['words'][i]['end']])
                else:
                    timestamp.append([w, 'n/a', 'n/a'])    
            else:
                print('Word mismatch: %s %s'%(w,a)) 
            i += 1
        utterance_timestamp.append(timestamp)
        timestamp = []

    return utterance_timestamp

# Extract audio for the utterance
def extract_audio(audio, transcript, alignment):
    utterances_timestamp = extract_utternace(transcript, alignment)
    j = 0
    for u in utterances_timestamp:
        # Extract audio only if first and last words align
        if u[0][1] != 'n/a' and u[-1][2] != 'n/a':
            start = str(u[0][1])
            end = str(u[-1][2])
            text = ' '.join([w[0] for w in u])
            with open('audio-%s.txt'%(str(j+1)), 'w') as f:
                f.write(text)
            subprocess.run([r'C:\ffmpeg\bin\ffmpeg.exe','-i',audio,'-ss',start,'-to',end,'audio-%s.wav'%(str(j+1))]) 
            j += 1

def main():
    parser = argparse.ArgumentParser(description='Extract aligned audio bits')
    parser.add_argument("--audio",help="audio file", required=True)
    parser.add_argument("--transcript",help="transcript file", required=True)
    parser.add_argument("--alignment",help="json output of gentle", required=True)
    args = parser.parse_args()
    extract_audio(args.audio, args.transcript, args.alignment)

if __name__ == "__main__":
    main()