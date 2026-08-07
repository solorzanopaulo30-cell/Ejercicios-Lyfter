import csv

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        games = []
        for row in csv_reader:
            games.append(row)
    return games


def print_games(games):
    for game in games:
        print(f"El juego es {game[0]} del genero {game[1]} desarrollado por {game[2]} y de clasificacion {game[3]}")


def main():
    games = read_games('ranking_video_games.csv')
    print_games(games)


if __name__ == '__main__':
    main()