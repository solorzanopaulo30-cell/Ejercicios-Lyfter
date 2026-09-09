#`.append()`, `.extend()`, `.remove()`, `.sort()`, slicing, comprensión de listas.
#4. Cree una función que reciba una lista de números y devuelva el promedio.


def average(lst):
    num = 0
    div = 0
    for i in lst:
        num += i
        div += 1   
    return num / div

print(average([8,9,2,4,6,9,3,1]))


