#!/usr/bin/python

import os, sys, json
from collections import defaultdict

input_dir = sys.argv[1]
output_dir = sys.argv[2]

files = os.listdir(input_dir)
words = defaultdict(int)

for dirpath, dirs, files in os.walk(input_dir):
    for file in files:
        with open(os.path.join(dirpath, file),'r') as text:
            word_counts = json.load(text)
            for k, v in word_counts.items():
                words[k] += v
                
with open(os.path.join(output_dir, 'total_words.json'), 'w') as o:
    json.dump(words, o)