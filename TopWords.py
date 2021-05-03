import os
import glob
import csv
import json

artist_words = {}
artists = []
words = []
with open("words.csv", 'r') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        if i == 0:
            for i in range(1, len(row)):
                artist = row[i]
                artist_words[artist] = []
                artists.append(artist)
        else:
            word = row[0]
            words.append(word)
            for j in range(1, len(row)):
                artist = artists[j-1]
                count = row[j]
                artist_words[artist].append((int(count), word))
        i += 1

top_words = {}
for artist in artist_words:
    top_words[artist] = []
    i = 0
    for word in sorted(artist_words[artist])[::-1]:
        top_words[artist].append(word[1])
        i += 1
        if i == 3: break   

print(top_words)
with open("topwords.csv", "w") as file:
    writer = csv.writer(file)
    for artist in top_words:
        writer.writerow([artist] + top_words[artist])

