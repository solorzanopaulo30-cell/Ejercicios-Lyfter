#`open()`, `.readlines()`, `.write()`, modos `'r'`/`'w'`/`'a'`.+
#6. Cree un programa que combine el contenido de 2 archivos de texto en uno solo, sin duplicar líneas.


with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

all_lines = lines1 + lines2
unique_lines = list(set(all_lines))

with open("merged_file.txt", "w") as file:
    for line in unique_lines:
        file.write(line)