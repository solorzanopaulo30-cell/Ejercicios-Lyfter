#`.append()`, `.extend()`, `.remove()`, `.sort()`, slicing, comprensión de listas.
#6. Cree una función que reciba una lista de listas (matriz) y devuelva la suma de todos sus elementos.


def sums(matriz):
    total = 0
    for i in matriz:
        for num in i:
            total += num
    print(total)

sums([[9,7,5,3,1,0,5,4,8,6,2],[2],[5],[9,8,5,1],[4,9,7,5,3,2,0,4]])