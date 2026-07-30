
import csv


def dev(file_path):
    searching = input("Ingrese Desarrollador: ")
    found = []
    with open(file_path, 'r', encoding='utf-8') as file:
        developers = csv.reader(file)
        headers = next(developers)
        for line in developers:
            if searching.lower() in line[2].lower():
                found.append(line)
                print(f"Juego: {line[0]} | Genero: {line[1]} | Desarrollador: {line[2]} | Clasificacion: {line[3]}")
    if not found:
        print(f"No se encontraron videojuegos desarrollados por '{searching}'.")


dev("ranking_video_games.csv")