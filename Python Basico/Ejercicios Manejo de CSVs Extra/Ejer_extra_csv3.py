import csv


def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        games = []
        for game in reader:
            games.append(game)
    return games


def count_by_genre(games):
    count = {}
    for game in games:
        genre = game[1]
        if genre in count:
            count[genre] += 1
        else:
            count[genre] = 1
    return count


def print_count(count):
    for genre, amount in sorted(count.items()):
        print(f"{genre}: {amount}")


def main():
    games = read_games("ranking_video_games.csv")
    count = count_by_genre(games)
    print_count(count)


if __name__ == '__main__':
    main()