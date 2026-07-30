import json


def pokemos_list(path):
    with open(path, "r") as file:
        pokemones = json.load(file)
        return pokemones

def new_pokemon():
    newpokemon = {"name": "Porygon",
                "type": "Normal",
                "level": 20,
                "weight_kg": 36.5,
                "is_shiny": False,
                "held_item": None,
                "skills": ["Tackle", "Conversion", "Sharpen", "Psybeam"],

                "stats": {"hp": 65,
                        "attack": 60,
                        "defense": 70,
                        "sp_attack": 85,
                        "sp_defense": 75,
                        "speed": 40
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