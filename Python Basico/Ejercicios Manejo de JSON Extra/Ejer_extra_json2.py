import json

def type_of():
    type_of_pokemon = input("Ingrese el tipo de pokemon que busca: ")
    poke = type_of_pokemon
    return poke


def reader_json(path):
    with open(path, 'r') as file:
        poke2 = json.load(file)
        return poke2


def filter_type_pokemon(list1, type1):
    poke2 = []
    for pokemon in list1:
        if pokemon['type'].lower() == type1.lower():
            poke2.append(pokemon)
    return poke2


def print_poke(list_1):
    print("Los pokemones que existen de ese tipo son: ")
    for pokemon in list_1:
        print(pokemon['name'])


def main():
    x = reader_json("pokemones.json")
    y = type_of()
    z = filter_type_pokemon(x,y)
    n = print_poke(z)


if __name__ == '__main__':
    main()