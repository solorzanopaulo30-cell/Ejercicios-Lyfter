#`csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`.
#6. Cree un programa que lea un CSV separado por punto y coma (`;`), usando el parámetro `delimiter`.


import csv

def leer_csv_con_punto_y_coma(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            print(row)