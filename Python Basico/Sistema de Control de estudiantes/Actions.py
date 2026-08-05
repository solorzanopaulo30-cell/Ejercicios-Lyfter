import Data
import csv
import os


# --------Numerar los estudiantes a ingresar - Not in use
#def amount_of_students():
#    amount = int(input("Ingrese la cantidad de estudiantes: "))
#    return amount


#---------Ingresar informacion de los estudiantes
def students_information(amount):
    students_documentation = []
    for number_of_students in range(amount):
        name = input(f"ingresee el nombre del estudiante numero {number_of_students + 1} : ")
        section = input("Ingrese la seccion (Ejemplo 11B): ")
        spanish_score = get_valid_grade("espanol")
        english_score = get_valid_grade("ingles")
        social_score = get_valid_grade("sociales")
        science_score = get_valid_grade("ciencias")
        new_student = {"nombre completo":name,"seccion":section,"nota espanol":spanish_score, "nota ingles":english_score, "nota sociales":social_score, "nota ciencias": science_score }
        students_documentation.append(new_student)
    return students_documentation


#----------Nota valida
def get_valid_grade(subjet_name):
    while True:
        score = input(f"Ingrese la nota de {subjet_name}: ")
        if not score.isdigit():
            print("Error: debe ingresar solo números, sin letras ni símbolos.")
            continue
        score = int(score)
        if score < 0 or score > 100:
            print("Error: la nota debe estar entre 0 y 100.")
            continue
        return score


# -------- Ver informacion de los estudiantes
def show_students_info(students_documentation):
    for student in students_documentation:
        print(f"Nombre completo: {student['nombre completo']}")
        print(f"Seccion: {student['seccion']}")
        print(f"Nota de espanol: {student['nota espanol']}")
        print(f"Nota de ingles: {student['nota ingles']}")
        print(f"Nota de sociales: {student['nota sociales']}")
        print(f"Nota de ciencias: {student['nota ciencias']}")
        print("------------------------------------------------")


# --------Promedio de los estudiantes
def average_students(students_documentation):
    students_with_average = []
    for student in students_documentation:
        average = (student['nota espanol']+student['nota ingles']+student['nota sociales']+student['nota ciencias'])/4
        students_with_average.append((student['nombre completo'], average))
    students_with_average.sort()
    return students_with_average


def average_students_v2(students_documentation):
    students_with_average = []
    for student in students_documentation:
        average = (student['nota espanol']+student['nota ingles']+student['nota sociales']+student['nota ciencias'])/4
        students_with_average.append((student['nombre completo'], average))
    students_with_average.sort()
    for name, average in students_with_average:
        print(f"Nombre: {name}, Promedio: {average}")      
    return students_with_average


#---------Buscar estudiante y ver nota
def search_student(students_documentation):
    searched_student = input("Ingrese el estudiante que desea buscar: ")
    found = False
    for student in students_documentation:
        if student['nombre completo'].lower() == searched_student.lower():
            print(f"Nombre: {student['nombre completo']}")
            print(f"Seccion: {student['seccion']}")
            print(f"Nota de espanol: {student['nota espanol']}")
            print(f"Nota de ingles: {student['nota ingles']}")
            print(f"Nota de sociales: {student['nota sociales']}")
            print(f"Nota de ciencias: {student['nota ciencias']}")
            print(f"Promedio: {(student['nota espanol']+student['nota ingles']+student['nota sociales']+student['nota ciencias'])/4}")
            found = True
    if not found:
        print("No estudiante registrado")


#-------- Ver Reprobados Por debajo de 60
def student_failed(average_students):
    print("Los estudiantes reprobados son: ")
    for name, average in average_students:
        if average < 60:
            print(f"Nombre: {name} y su promedio es: {average}")


#---------- Ver top 3 performance
def top_3_performance(average_students):
    sorted_student = sorted(average_students, key=lambda x: x[1], reverse=True)
    top3 = sorted_student[:3]
    for name, average in top3:
        print(f"Nombre: {name}, Promedio: {average}")


#----------- Eliminar Estudiante
def delete_student(student_documentation):
    print("Alerta para eliminar un estudiante necesitas el nombre completo y seccion")
    name = input("Ingrese estudiante a eliminar")
    section = input("Ingrese la seccion del estudiante a eliminar")
    found = False
    for student in student_documentation:
        if student['nombre completo'].lower() == name.lower() and student['seccion'].lower() == section.lower():
            found = True
            confirmation = input(f"¿Está seguro que desea eliminar a {student['nombre completo']}? (s/n): ")
            if confirmation.lower() == "s":
                student_documentation.remove(student)
                print("Estudiante eliminado")
            else:
                print("Eliminación cancelada")
            break
    if not found:
        print("Estudiante no encontrado")


#-----------Exportar CSV
def export_csv(student_documentation, filename="Estudiantes.csv"):
    fieldnames = student_documentation[0].keys()
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_documentation)  
    print(f"Datos exportados a {filename}")


#----------Importar datos

def import_from_csv(filename="estudiantes.csv"):
    if not os.path.exists(filename):
        print(f"No se encontró el archivo '{filename}'. Debe exportar los datos primero.")
        return None
    students_documentation = []
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['nota espanol'] = int(row['nota espanol'])
            row['nota ingles'] = int(row['nota ingles'])
            row['nota sociales'] = int(row['nota sociales'])
            row['nota ciencias'] = int(row['nota ciencias'])
            students_documentation.append(row)
    print(f"Datos importados correctamente desde '{filename}'.")
    return students_documentation