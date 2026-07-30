import json

def reader(path):
    with open(path, 'r')as file:
        pokemones = json.load(file)
        return pokemones


def stats1(path):
    pokemones = path
    for pokemon in pokemones:
        print(pokemon['name'])
        print(f"ataque {pokemon['stats']['attack']}")
        print(f"defensa {pokemon['stats']['defense']}")
        print(f"velocidad {pokemon['stats']['speed']}")
        print()
    return pokemones


def main():
    x = reader("pokemones.json")
    stats1(x)


if __name__ == '__main__':
    main()

