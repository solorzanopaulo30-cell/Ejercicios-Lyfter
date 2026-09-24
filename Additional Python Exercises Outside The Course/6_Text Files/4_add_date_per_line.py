#`open()`, `.readlines()`, `.write()`, modos `'r'`/`'w'`/`'a'`.+
#4. Cree un programa que agregue una fecha al inicio de cada línea de un archivo de log.


from datetime import date

with open("log.txt", "w") as file:
    file.write("Usuario inicio sesion\n")
    file.write("Error de conexion\n")
    file.write("Usuario cerro sesion\n")

with open("log.txt", "r") as file:
    lines = file.readlines()

today = date.today()

with open("log_with_date.txt", "w") as file:
    for line in lines:
        new_line = f"{today} - {line}"
        file.write(new_line)