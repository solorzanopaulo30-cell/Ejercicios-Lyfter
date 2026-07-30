import csv


def ask_game():
    name = input("Nombre :")
    type1 = input("Genero :")
    dev = input("Desarrollador :")
    clasification = input("Clasificacion :")
    game = {"Nombre": name, "Genero": type1, "Desarrollador": dev, "Clasificacion": clasification}
    return game


def video_games_dev(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = ("Nombre", "Genero", "Desarrollador", "Clasificacion")
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)


def main():
    games = []
    while True:
        game = ask_game()
        games.append(game)
        conti = input("¿Cargar otro juego? (s/n): ")
        if conti.lower() == "n":
            break
    video_games_dev('ranking_video_games_by_tab.csv', games)


if __name__ == '__main__':
    main()