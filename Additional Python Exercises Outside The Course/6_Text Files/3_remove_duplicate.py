#`open()`, `.readlines()`, `.write()`, modos `'r'`/`'w'`/`'a'`.+
#3. Cree un programa que lea un archivo y elimine las líneas duplicadas, guardando el resultado en un archivo nuevo.


with open ("duplicates.txt","r") as file:
    lines = file.readlines()
    unique_lines = set(lines)

with open("unique_lines.txt", "w") as file:
    for line in unique_lines:
        file.write(line)
