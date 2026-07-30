#Cree un programa que:
#Pida al usuario su nombre
#Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")

def name_1():
    while True:
        try:
            name = input("ingrese su nombre: ")
            if name.isdigit():
                raise ValueError ("El nombre no puede ser un numero")
            else:
                print(f"Bienvenido: {name} ")
                break
        except ValueError as error:
            print("ingrese nombre valido")
    return name


#Luego pida su edad
#Si no es un número válido, capture el ValueError y muestre un mensaje

def age_1():
    while True:
        try:
            age = int(input("ingrese su edad: "))
            print(f"Su edad es de: {age} anos ")
            break
        except ValueError as error:
            print("ingrese numero valido")
    return age

user_name = name_1()
user_age = age_1()

#Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"

print(f"Hola {user_name}, su edad es {user_age}")