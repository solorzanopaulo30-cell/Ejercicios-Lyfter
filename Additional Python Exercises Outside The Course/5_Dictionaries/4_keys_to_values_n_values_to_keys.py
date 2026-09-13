#Acceso por clave, `.keys()`, `.items()`, diccionarios anidados.
#4. Cree una función que invierta un diccionario (claves pasan a ser valores y viceversa).


def keys_to_values(dict1):
    dict2 = {}
    for key,value in dict1.items():
        dict2[value] = key
    print(dict2)

dict1 = ({
    'Paulo': 100,
    'Alek': 50,
    'Jean': 75,
})


keys_to_values(dict1)