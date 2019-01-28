#!/usr/bin/python

import os, sys, json, string
from collections import defaultdict

input_dir = sys.argv[1]
output_dir = sys.argv[2]

files = os.listdir(input_dir)
words = defaultdict(int)

def clean_text(line):
    line = line.lower()
    transmap = str.maketrans('','',string.punctuation)
    line = line.translate(transmap)
    return line

for dirpath, dirs, files in os.walk(input_dir):
    for file in files:
        with open(os.path.join(dirpath, file),'r') as text:
            for line in text:
                cleaned_text = clean_text(line)
                for word in cleaned_text.split():
                    words[word] += 1
                
        with open(os.path.join(output_dir, file.split('.')[0]+'.json'), 'w') as o:
            json.dump(words, o)                

                

            
                
        

