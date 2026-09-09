#`.append()`, `.extend()`, `.remove()`, `.sort()`, slicing, comprensión de listas.
#5. Cree una función que invierta una lista sin usar `.reverse()` ni slicing negativo.


def reverse(lst):
    new = []
    for i in range(len(lst) - 1, -1, -1):
        new.append(lst[i])
    print(new)

reverse([9,5,1,4,7,3,8,2,4,6])