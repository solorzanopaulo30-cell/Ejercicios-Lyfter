#`.append()`, `.extend()`, `.remove()`, `.sort()`, slicing, comprensión de listas.
#2. Cree una función que reciba una lista y devuelva una nueva sin elementos repetidos.


def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
