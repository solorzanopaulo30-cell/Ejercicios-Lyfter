#Métodos de texto: `.strip()`, `.lower()`, `.split()`, `.join()`, indexado, slicing.
#6. Cree una función que reciba una lista de nombres y devuelva un solo string, separado por comas.

def join_names(names_list):
    return ', '.join(names_list)

print(join_names(['Alice', 'Bob', 'Alek', 'Charlie']))