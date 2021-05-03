import os
import glob
import csv
import json
import sys

csv.field_size_limit(sys.maxsize)

path = 'newData/temporalTotal'
extension = 'csv'
os.chdir(path)
csv_files = glob.glob('*.{}'.format(extension))

yearly_data = {}

for csv_file in csv_files:
    with open(csv_file, 'r') as file:
        artist_name = csv_file[:-4]
        reader = csv.reader(file)
        row_index = 0
        for row in reader:
            if row_index > 0:
                year = row[0]
                year_counts_str = row[1].replace("\"{", "{").replace("}\"", "}").replace("{\'", "{\"").replace(" \'", " \"").replace("\':","\":")
                year_counts = json.loads(year_counts_str)
                if year not in yearly_data:
                    yearly_data[year] = {}
                for word in year_counts.keys():
                    yearly_data[year][word] = year_counts[word]
            row_index += 1

import json 
     
with open("temporalwordstotals.json", "w") as outfile: 
    json.dump(yearly_data, outfile)
