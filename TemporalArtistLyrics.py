import os
import glob
import csv
import json
import sys

csv.field_size_limit(sys.maxsize)

path = 'newData/temporalArtists'
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
                if artist_name not in yearly_data[year]:
                    yearly_data[year][artist_name] = {}
                for word in year_counts.keys():
                    yearly_data[year][artist_name][word] = year_counts[word]
            row_index += 1

with open("temporalwords.csv", "w") as file:
    print("opened file")
    writer = csv.writer(file)
    writer.writerow(["Year", "Counts"])
    for year in yearly_data.keys():
        writer.writerow([year, str(yearly_data[year])])

import json 
     
with open("temporalwords.json", "w") as outfile: 
    json.dump(yearly_data, outfile)
