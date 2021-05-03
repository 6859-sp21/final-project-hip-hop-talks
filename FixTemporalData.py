import os
import glob
import csv
import json
import sys

extension = 'csv'
csv.field_size_limit(sys.maxsize)

yearly_data = {}
rows = []
with open("temporalwordstotal.csv", "r") as f:
    rows = f.readlines()

with open("temporalwords2.csv", "w") as f:
    f.write("".join(rows).replace("\'","\""))
