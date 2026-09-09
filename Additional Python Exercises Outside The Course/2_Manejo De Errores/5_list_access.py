#`try`/`except`, `raise`, excepciones específicas.
#5. Cree una función que acceda a una posición de una lista, y capture el error si el índice no existe.


def access_list_element(my_list, index):
    try:
        element = my_list[index]
        print(f"El elemento en el índice {index} es: {element}")
    except IndexError:
        print(f"Error: El índice {index} no existe en la lista.")

access_list_element([5,6,9,4,2,6,3],10)