
def int_convertor(my_list):
    for element in my_list:
        try:
            number = int(element)
            print(f"Convertido: {number}")
        except ValueError:
            print(f"No se pudo convertir el elemento: {element}")


int_convertor(["4", "hola", "10", "5.2", "2", "Jean"])