import csv


def read_games(path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        games = []
        for line in reader:
            games.append(line)
    return games


def ask_classification():
    classification = input("Ingrese Clasificacion: ")
    return classification


def filter_by_classification(games, classification):
    filtered_games = []
    for game in games:
        if game[3] == classification:
            filtered_games.append(game)
    return filtered_games


def print_filtered_games(filtered_games):
    if not filtered_games:
        print("No se encontraron juegos con esa clasificacion")
    else:
        for game in filtered_games:
            print(f"El juego con esa clasificacion es: {game[0]}")


def main():
    games = read_games("ranking_video_games.csv")
    classification = ask_classification()
    filtered_games = filter_by_classification(games, classification)
    print_filtered_games(filtered_games)


if __name__ == '__main__':
    main()