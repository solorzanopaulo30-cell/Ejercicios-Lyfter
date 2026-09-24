#`csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`.
#2. Cree un programa que exporte una lista de diccionarios (contactos) a un archivo CSV.


import csv

def export(filename,contacts):
    headers  = contacts[3].keys()
    with open (filename, "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = headers)
        writer.writeheader()
        writer.writerows(contacts)


contacts = [
    {"nombre": "Juan", "apellido": "Pérez", "email": "juan.perez@example.com"},
    {"nombre": "María", "apellido": "Gómez", "email": "maria.gomez@example.com"},
    {"nombre": "Carlos", "apellido": "López", "email": "carlos.lopez@example.com"},
    {"nombre": "Ana", "apellido": "Martínez", "email": "ana.martinez@example.com"}
]