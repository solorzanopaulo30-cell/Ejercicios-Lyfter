
import csv

def reader(i):
    with open(i, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for x in reader:
            print(f"El juego es {x[0]} del genero {x[1]} desarrollado por {x[2]} y de clasificacion {x[3]}")


reader('ranking_video_games.csv')
