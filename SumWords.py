import os
import glob
import csv
import json

with open("words.csv", 'r') as rfile:
    reader = csv.reader(rfile)
    with open("wordsums.csv", 'w') as wfile:
        writer = csv.writer(wfile)

        for row in reader:
            if row[0] == "Words": continue
            word = row[0]
            count = 0
            for i in range(1, len(row)):
                count += int(row[i])
            writer.writerow([word, count])

