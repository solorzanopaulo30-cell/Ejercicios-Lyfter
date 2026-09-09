#`try`/`except`, `raise`, excepciones específicas.
#4. Cree una función `validar_edad(edad)` que lance un `ValueError` si la edad es negativa o mayor a 120.

def valid_age(age):
    if age < 0 or age > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")
    else:
        print(f"La edad {age} es válida.")

valid_age(25)  