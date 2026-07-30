import json

def pokemon_list(path):
    with open(path, "r") as file:
        pokemones = json.load(file)
        return pokemones

def showed_pokemons(list):
    for pokemon in list:
        print(f"Nombre: {pokemon['name']}, Tipo: {pokemon['type']}, Nivel: {pokemon['level']}, Peso: {pokemon['weight_kg']}")


def main():
    showed_pokemons(pokemon_list("pokemones.json"))

if __name__ == '__main__':
    main()