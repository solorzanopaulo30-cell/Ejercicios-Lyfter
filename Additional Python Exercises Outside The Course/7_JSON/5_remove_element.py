#`json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`.
#5. Cree una función que elimine un elemento específico de una lista guardada en JSON, según un campo (ej: "id").


import json

def remove_element_from_json(file_path, element_id):
    with open(file_path, "r") as file:
        data = json.load(file)

    updated_data = []
    for item in data:
        if item.get("id") != element_id:
            updated_data.append(item)

    with open(file_path, "w") as file:
        json.dump(updated_data, file, indent=4)

    print(f"Elemento con id {element_id} eliminado.")