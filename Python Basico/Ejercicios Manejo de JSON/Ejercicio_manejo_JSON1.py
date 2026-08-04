import json


def pokemos_list(path):
    with open(path, "r") as file:
        pokemones = json.load(file)
        return pokemones


def new_pokemon():
    name = input("Ingrese el nombre del Pokémon: ")
    type_ = input("Ingrese el tipo del Pokémon: ")
    level = int(input("Ingrese el nivel: "))
    weight_kg = float(input("Ingrese el peso en kg: "))
    is_shiny_input = input("¿Es shiny? (s/n): ")
    is_shiny = is_shiny_input.lower() == "s"
    held_item = input("Ingrese el objeto que porta (o deje vacío si no tiene): ")
    if held_item == "":
        held_item = None

    print("Ingrese 4 habilidades:")
    skill1 = input("Habilidad 1: ")
    skill2 = input("Habilidad 2: ")
    skill3 = input("Habilidad 3: ")
    skill4 = input("Habilidad 4: ")
    skills = [skill1, skill2, skill3, skill4]

    print("Ingrese las estadísticas:")
    hp = int(input("HP: "))
    attack = int(input("Ataque: "))
    defense = int(input("Defensa: "))
    sp_attack = int(input("Ataque especial: "))
    sp_defense = int(input("Defensa especial: "))
    speed = int(input("Velocidad: "))

    newpokemon = {
        "name": name,
        "type": type_,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed
        }
    }
    return newpokemon


def main():
    current = pokemos_list("pokemones.json")
    new = new_pokemon()
    current.append(new)
    with open("pokemones.json", "w") as file:
        json.dump(current, file, indent=4)


if __name__ == '__main__':
    main()