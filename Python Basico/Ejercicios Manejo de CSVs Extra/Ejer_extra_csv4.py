import csv


def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        games = []
        for line in reader:
            games.append(line)
    return games


def ask_developer():
    developer = input("Ingrese Desarrollador: ")
    return developer


def filter_by_developer(games, developer):
    found = []
    for game in games:
        if developer.lower() in game[2].lower():
            found.append(game)
    return found


def print_games(found, developer):
    if not found:
        print(f"No se encontraron videojuegos desarrollados por '{developer}'.")
    else:
        for game in found:
            print(f"Juego: {game[0]} | Genero: {game[1]} | Desarrollador: {game[2]} | Clasificacion: {game[3]}")


def main():
    games = read_games("ranking_video_games.csv")
    developer = ask_developer()
    found = filter_by_developer(games, developer)
    print_games(found, developer)


if __name__ == '__main__':
    main()