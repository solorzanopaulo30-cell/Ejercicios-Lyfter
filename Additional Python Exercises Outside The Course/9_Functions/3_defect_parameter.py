#Parámetros, `return`, `*args`, `import`, separación en archivos.
#3. Cree una función con parámetros con valores por defecto, y pruébela llamándola con y sin esos argumentos.


def age(name, age = "Edad no proporcionada"):
    print(f"Hola {name},viejazo de {age}")

age("paolo",25)
age("paolo")