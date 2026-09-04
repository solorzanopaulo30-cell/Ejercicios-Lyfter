import json
from datetime import date
from logica import FinancialMgmt, Movement,Entry,Spend 
import os


def save(manager, filename="finance.json"):
    movimientos_dict = [movement.to_dict() for movement in manager.movements]
    datos = {
        "categories": manager.categories,
        "movements": movimientos_dict
    }
    with open(filename, "w") as file:
        json.dump(datos, file, indent=4)


def load(filename="test_finance.json"):
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as file:
        data = json.load(file)
    manager = FinancialMgmt()
    manager.categories = data["categories"]
    for movimiento_dict in data["movements"]:
        movimiento_objeto = Movement.from_dict(movimiento_dict)
        manager.movements.append(movimiento_objeto)
        manager.balance += movimiento_objeto.apply()

    return manager