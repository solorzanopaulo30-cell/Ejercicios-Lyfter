#`try`/`except`, `raise`, excepciones específicas.
#3. Cree un programa que pida repetidamente un número hasta que el usuario ingrese uno válido (`while` + `try/except`).

def get_valid_number():
    while True:
        try:
            number = int(input("Ingrese un número válido: "))
            print(f"El número ingresado es: {number}")
            break  
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

get_valid_number()