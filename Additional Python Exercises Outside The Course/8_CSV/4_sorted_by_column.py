#`csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`.
#4. Cree un programa que lea un CSV y lo ordene por una columna específica, guardando el resultado en un CSV nuevo.


import csv

def ordenar_csv(filename, columna, nuevo_filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        filas = list(reader)

    filas_ordenadas = sorted(filas, key=lambda fila: float(fila[columna]))

    with open(nuevo_filename, "w", newline="") as file:
        encabezados = filas_ordenadas[0].keys()
        writer = csv.DictWriter(file, fieldnames=encabezados)
        writer.writeheader()
        writer.writerows(filas_ordenadas)