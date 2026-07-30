
import csv


def ask_clasification(path):
    clas1 = input("Ingrese Clasificacion: ")
    filter1 = []
    with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header =next(reader)
            for line in reader:
                if line[3] == clas1:
                    filter1.append(line)
                    print(f"el juego con esa clasificacion es: {line[0]}")
    if not filter1:
        print("No se se encontraron archivos con esa clasificacion")


def main():
    ask_clasification("ranking_video_games.csv")


if __name__ == '__main__':
    main()
