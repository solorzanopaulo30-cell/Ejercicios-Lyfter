#`json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`.
#2. Cree un programa que lea un archivo JSON con una lista de productos y calcule el valor total del inventario.


import json


with open("inventory.json","r") as file:
    products = json.load(file)
    total_value = 0
    for product in products:
        total_value += product["precio"] * product["cantidad"]
    print(f"El valor total del inventario es: {total_value}")
    