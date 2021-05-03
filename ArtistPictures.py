import os
import glob
import csv
import json
from PIL import Image

basewidth = 75
cropwidth = 50

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

artists = []
with open("rapper_names.csv", 'r') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        if i > 0:
            artists.append(row[0])
        i += 1

with open("rappers.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Artists","Pictures"])
    for artist in artists:
        # Resize Images
        img = Image.open(os.getcwd() + "/artistsPictures/" + artist + ".png")
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img = crop_center(img, cropwidth, cropwidth)
        img.save(os.getcwd() + "/artistsPictures/" + artist + "_resized_cropped.png", optimize = True, quality = 1)

        # Write image file names
        writer.writerow([artist, "/a4-hiphoptalks/artistsPictures/" + artist + "_resized_cropped.png"])
        # writer.writerow([artist, "/artistsPictures/" + artist + "_resized_cropped.png"])
