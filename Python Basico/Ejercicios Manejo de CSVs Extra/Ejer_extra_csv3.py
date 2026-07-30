
import csv

def category(file_path):
    count = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        kind_of_game = csv.reader(file)
        header = next(kind_of_game)
        for game in kind_of_game:
            categories = game[1]
            if categories in count:
                count[categories] += 1
            else:
                count[categories] = 1
    for categories, amount in sorted(count.items()):
        print(f"{categories}: {amount}")
    return count


category("ranking_video_games.csv")