#`open()`, `.readlines()`, `.write()`, modos `'r'`/`'w'`/`'a'`.
#1. Cree un programa que escriba una lista de tareas en un archivo de texto, una por línea.


tareas = ["Comprar pan", "Estudiar Python", "Lavar el auto"]

with open("tareas.txt", "w") as file:
    for tarea in tareas:
        file.write(tarea + "\n")