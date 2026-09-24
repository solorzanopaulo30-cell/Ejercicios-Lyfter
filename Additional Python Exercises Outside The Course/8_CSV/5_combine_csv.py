#`csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`.
#5. Cree un programa que lea 2 archivos CSV con la misma estructura y los combine en uno solo, sin duplicar filas


import csv


def combine_csv(file1, file2, output_file):
    with open (file1,"r") as f1, open (file2,"r") as f2:
        reader1 = csv.DictReader(f1)
        reader2 = csv.DictReader(f2)
    combined = list(reader1) + list(reader2)
    with_no_duplicates = []
    for row in combined:
        if row not in with_no_duplicates:
            with_no_duplicates.append(row)

    with open (output_file, "w", newline="") as file:
        header = with_no_duplicates[0].keys()
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        writer.writerows(with_no_duplicates)


