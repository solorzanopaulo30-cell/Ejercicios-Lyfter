import Data
import Actions

def show_menu():
    print("Hola, bienvenido al menu de Control de Estudiantes")
    print("Aca podras ver, ingresar,borrar informacion de los estudiantes de Lyfter")
    print("Como caracteristica especial si asi lo deseas podras ver informacion de estudiantes reprobados")
    print("Ver a nuestro tres mejores estudiantes, o promedio de todos los estudiantes")
    print("Buscar estudiante individual y ver sus notas y promedio")    
    print("Y exportar informacion en formato CSV para mayor comodidad")
    print("Demosle")
    print("Para buscar un estudiante marque 1")
    print("Para ver informacion de todos los estudiantes marque 2")
    print("Para ver a nuestros 3 mejores promedios marque 3")
    print("Para ver promedio de todos los estudiantes marque 4")
    print("Para ver a nuestros estudiantes reprobados marque 5")
    print("Para añadir un estudiante marque 6")
    print("Para eliminar un estudiante marque 7")
    print("Para exportar la informacion de nuestros estudiantes en formato csv marque 8")
    print("Para Importar la informacion de nuestros estudiantes en formato csv marque 9")


def menu_selection(students_documentation):
    print("Seleccione lo que desea realizar")
    searched_student = 1
    general_student_info =  2
    top_3_students = 3
    average_in_general = 4
    failed_students = 5
    add_student = 6
    delete_student = 7
    export_info = 8
    import_info = 9
    while True:
        picked = int(input("Marque numero, (si no esta entre el 1 al 9 no sera valido):  "))
        if picked == searched_student:
            Actions.search_student(students_documentation)

        elif picked == general_student_info:
            Actions.show_students_info(students_documentation)

        elif picked == top_3_students:
            average = Actions.average_students(students_documentation)
            Actions.top_3_performance(average)

        elif picked == average_in_general:
            Actions.average_students_v2(students_documentation)

        elif picked == failed_students:
            average = Actions.average_students(students_documentation)
            Actions.student_failed(average)

        elif picked == add_student:
            new = Actions.students_information(1)
            students_documentation.extend(new)

        elif picked == delete_student:
            Actions.delete_student(students_documentation)

        elif picked == export_info:
            Data.export_csv(students_documentation)

        elif picked == import_info:
            result = Data.import_from_csv()
            if result is not None:
                students_documentation = result

        else:
            print("Numero invalido")