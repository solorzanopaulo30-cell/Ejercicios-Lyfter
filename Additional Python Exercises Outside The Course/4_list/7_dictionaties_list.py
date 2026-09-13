#`.append()`, `.extend()`, `.remove()`, `.sort()`, slicing, comprensión de listas.
#7. Cree una función que reciba una lista de diccionarios de productos y devuelva el más caro.


def most_expensive_product(products):
    if not products:
        return None
    most_expensive = products[0]
    for product in products:
        if product['price'] > most_expensive['price']:
            most_expensive = product
    return most_expensive

products = [
    {'name': 'Laptop', 'price': 1000},
    {'name': 'Phone', 'price': 500},
    {'name': 'Tablet', 'price': 300}
]

print(most_expensive_product(products))