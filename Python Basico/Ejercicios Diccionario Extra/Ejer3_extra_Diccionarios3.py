
products = [
    {"name": "Cuaderno", "category": "Papelería", "price": 5},
    {"name": "Lapicera", "category": "Papelería", "price": 2},
    {"name": "Zapatillas", "category": "Ropa", "price": 60},
    {"name": "Campera", "category": "Ropa", "price": 95},
    {"name": "Mochila", "category": "Ropa", "price": 45},
]

category_totals = {}
for product in products:
    category =product["category"]
    price = product["price"]
    if category in category_totals:
        category_totals[category] += price
    else:
        category_totals[category] = price

print(category_totals)
