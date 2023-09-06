# Saves a csv file as a json
import csv, json

with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        info = (', '.join(row))

with open('csv.json', 'w') as f2:
    f2.write(json.dumps(info))
    f2.close