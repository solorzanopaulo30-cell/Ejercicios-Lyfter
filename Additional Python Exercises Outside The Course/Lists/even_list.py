#`.append()`, `.extend()`, `.remove()`, `.sort()`, slicing, comprensión de listas.
#1. Cree una función que reciba una lista de números y devuelva solo los pares.


def even(even_list):
    verify_even = []
    for num in even_list:
        if (num % 2) == 0:
            verify_even.append(num)
    print(verify_even)

even([5,6,4,2,8,9,7,3,1])