import json
import os
from logica import FinancialMgmt, Movement, Category


def save(manager, filename="finance.json"):
    data = {
        "categories": [c.to_dict() for c in manager.categories],
        "movements": [m.to_dict() for m in manager.movements]
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load(filename="finance.json"):
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as file:
        data = json.load(file)
    manager = FinancialMgmt()
    manager.categories = [Category.from_dict(c) for c in data["categories"]]
    for movement_dict in data["movements"]:
        movement_object = Movement.from_dict(movement_dict, manager.categories)
        manager.movements.append(movement_object)
        manager.balance += movement_object.apply()
    return manager