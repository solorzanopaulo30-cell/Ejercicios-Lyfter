#1 step variable definida dentro de una funcion desde afuera

def manzana(num1):
    fruit = num1 * 2
    return fruit


# Intento fallido: acceder a la variable local 'fruit' directamente desde afuera
# print(fruit)  # NameError: name 'fruit' is not defined
# (la variable 'fruit' de adentro de la función no existe en este scope)

# Lo que sí funciona: usar el valor que la función devolvió con return

result = manzana(5)
fruit = result
print(fruit)  

#2. step acceder a una variable global desde una funcion y cambiar su valor

big_boss = 1

def get_global_variable():
    global big_boss
    big_boss = 2

get_global_variable()
print(big_boss)       