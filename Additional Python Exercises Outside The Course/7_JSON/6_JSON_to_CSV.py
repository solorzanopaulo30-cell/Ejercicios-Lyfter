#`json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`.
#6. Cree un programa que convierta un archivo JSON a un archivo CSV.


import json
import csv


def json_to_csv(json_file, csv_file):
    with open (json_file,"r") as file:
        data = json.load(file)

    with open(csv_file,"w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())

    