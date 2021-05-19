import os
import glob
import csv
import json
import sys

csv.field_size_limit(sys.maxsize)

path = 'newData/pairings'
extension = 'csv'
os.chdir(path)
csv_files = glob.glob('*.{}'.format(extension))

word_pairings = {}
for csv_file in csv_files:
    with open(csv_file, 'r') as file:
        artist_name = csv_file[:-4]
        reader = csv.reader(file)
        row_index = 0
        for row in reader:
            if row_index > 0:
                word = row[0]
                pairings_str = row[1].replace("\"{", "{").replace("}\"", "}").replace("{\'", "{\"").replace(" \'", " \"").replace("\':","\":")
                pairings = json.loads(pairings_str)
                if word not in word_pairings:
                    word_pairings[word] = {}
                if artist_name not in word_pairings[word]:
                    word_pairings[word][artist_name] = {}
                for paired_word in sorted(pairings, key = pairings.get, reverse=True)[0:5]:
                    word_pairings[word][artist_name][paired_word] = pairings[paired_word] 
            row_index += 1

import json 
with open("artistwordpairings.json", "w") as outfile: 
    json.dump(word_pairings, outfile)
