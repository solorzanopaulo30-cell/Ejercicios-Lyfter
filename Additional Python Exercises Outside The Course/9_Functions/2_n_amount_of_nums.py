#Parámetros, `return`, `*args`, `import`, separación en archivos.
#2. Cree una función que reciba una cantidad variable de números (`*args`) y devuelva la suma de todos.


def total_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(total_sum(5, 3, 8, 2))