#`csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`.
#1. Cree un programa que lea un archivo CSV de ventas y calcule el total vendido.


import csv

def calculate(filename):
    total = 0
    with open(filename,"r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            total += float(line["sold"])    
        return total

