#`try`/`except`, `raise`, excepciones específicas.
#6. Cree una función `dividir_lista(numeros, divisor)` que capture tanto `ZeroDivisionError` como `TypeError` si la lista contiene un elemento no numérico.


def divide_list(numbers, divisor):
    try:
        return [num / divisor for num in numbers]
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: La lista contiene un elemento no numérico.")

divide_list([10, 20, 30, 'a', 50], 2)