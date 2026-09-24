#Acceso por clave, `.keys()`, `.items()`, diccionarios anidados.
#2. Cree una función que reciba un diccionario de notas de estudiantes y devuelva el promedio general.


def grade_students(dic):
    total = 0
    div = 0
    for grade in dic.values():
        total += grade
        div += 1
    print(total / div)


grade = ({
    'Paulo': 100,
    'Alek': 50,
    'Jean': 75,
})

grade_students(grade)  