import os
import glob
import csv
import json

path = 'newData/original'
extension = 'csv'
os.chdir(path)
csv_files = glob.glob('*.{}'.format(extension))

artists=[]
words=[]
all_artist_words=[]


for csv_file in csv_files:
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            artist_string = row[1].replace("{\'", "{\"").replace(" \'", " \"").replace("\':", "\":").replace("\"\"", "\"").replace("\'","")
            artist_json = json.loads(artist_string)
            for word in artist_json.keys():
                if word in words: continue
                words.append(word)

artists = []
for csv_file in csv_files:
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            artist = row[0]
            if artist == "Artist": break
            if artist in artists: break
            artists.append(artist)
            artist_string = row[1].replace("{\'", "{\"").replace(" \'", " \"").replace("\':", "\":").replace("\"\"", "\"").replace("\'","")
            artist_json = json.loads(artist_string)
            artist_words=[]
            for word in words:
                if word in artist_json:
                    artist_words.append(artist_json[word])
                else:
                    artist_words.append(0)
            all_artist_words.append(artist_words)

word_sums = {}
max_word_count = 0
for i in range(len(words)):
    count = 0
    for artist_word_counts in all_artist_words:
        count += artist_word_counts[i]
    word_sums[words[i]] = count
    if count > max_word_count:
        max_word_count = count

zipped_artist_words = zip(*all_artist_words)
all_word_artists = []
for i in zipped_artist_words:
    all_word_artists.append(list(i))

filtered_words = []
filtered_word_artists = []
for i in range(len(words)):
    if word_sums[words[i]] > 180:
        filtered_words.append(words[i])
        filtered_word_artists.append(all_word_artists[i])
words = filtered_words
all_word_artists = filtered_word_artists

print(len(words))
print(len(all_word_artists))
print(len(artists))
with open("words.csv", "w") as file:
    words_writer = csv.writer(file)
    words_writer.writerow(["Words"] + artists)
    for i in range(len(words)):
        words_writer.writerow([words[i]] + all_word_artists[i])

with open("rapper_names.csv", "w") as file:
    words_writer = csv.writer(file)
    words_writer.writerow(["Artists"])
    for i in range(len(artists)):
        words_writer.writerow([artists[i]])
