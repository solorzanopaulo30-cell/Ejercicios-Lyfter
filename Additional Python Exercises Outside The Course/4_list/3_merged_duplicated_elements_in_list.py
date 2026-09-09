#`.append()`, `.extend()`, `.remove()`, `.sort()`, slicing, comprensión de listas.
#3. Cree una función que reciba dos listas y devuelva los elementos que están en ambas.


def new_lst(lst1,lst2):
    new = []
    for item in lst1:
        if item in lst2:
            new.append(item)
    print(new)

new_lst([1,5,9,7,3],[1,5,9,8,4,6,2])