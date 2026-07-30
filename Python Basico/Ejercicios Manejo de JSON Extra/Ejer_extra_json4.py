import json

def reader(path):
    with open(path, 'r')as file:
        pokemones = json.load(file)
        return pokemones


def selected_group(path):
    groups = {}
    for pokemon in path:
        type1 = pokemon['type']
        level = pokemon['level']
        if type1 not in groups:
            groups[type1] = []
            groups[type1].append(level)
    return groups


def average_by_type(path):
    for type1, levels in path.items():
        average = sum(levels) / len(levels)
        print(f"{type1}: average level {average}")


def main():
    x = reader("pokemones.json")
    groups = selected_group(x)
    average_by_type(groups)

if __name__ == '__main__':
    main()
