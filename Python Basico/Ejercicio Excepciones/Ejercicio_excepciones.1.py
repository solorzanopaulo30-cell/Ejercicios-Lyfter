def show_menu():
    print("hola, esta es una calculadora en python")
    print("para sumas precione 1, para restas precione 2, para multiplicaciones precione 3, para dividir precione 4 y si quieres borrar el primer numbero precione 5")


def read_option():
    num = int(input("ingrese numero: "))
    return num


def read_option2():
    num_2 = int(input("ingrese el numero para calcular: "))
    return num_2


def rum(opcion, current_number, num_2):
    sum = 1
    rest = 2
    multi = 3
    division = 4
    detele_result = 5

    if opcion == sum:
        result = current_number + num_2
        print(result)
        return result
    elif opcion == rest:
        result = current_number - num_2
        print(result)
        return result
    elif opcion == multi:
        result = current_number * num_2
        print(result)
        return result
    elif opcion == division:
        result = current_number / num_2
        print(result)
        return result
    elif opcion == detele_result:
        result = 0
        print(result)
        return result
    else:
        print("Opción inválida. Seleccione un número del 1 al 5.")
        return current_number


def calculator():
    current_number = 2
    show_menu()
    while True:
        try:
            option = read_option()
            if option == 5:
                current_number = rum(option, current_number, 0)
            elif option in (1, 2, 3, 4):
                num_2 = read_option2()
                current_number = rum(option, current_number, num_2)
            else:
                rum(option, current_number, 0)
        except (ValueError, ZeroDivisionError) as error:
            print("ingrese numero valido")


if __name__ == '__main__':
    calculator()



