#`csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`.
#3. Cree un programa que lea un CSV y filtre solo las filas donde una columna cumpla una condición (ej: precio > 100).

import csv


def filter_file(filename,column_name,condition):
    with open(filename,"r") as file:
        reader = csv.DictReader(file)
        filtered_rows = []
        for row in reader:
            if float(row[column_name]) >= condition:
                filtered_rows.append(row)
        return filtered_rows
