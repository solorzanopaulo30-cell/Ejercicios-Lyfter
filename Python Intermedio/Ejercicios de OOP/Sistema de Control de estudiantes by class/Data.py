import csv
import os


class Student():
    def __init__(self, name, section, spanish_score, english_score, social_score, science_score):
        self.name = name
        self.section = section
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.social_score = social_score
        self.science_score = science_score

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish_score": self.spanish_score,
            "english_score": self.english_score,
            "social_score": self.social_score,
            "science_score": self.science_score
        }

    @staticmethod
    def create_student(students_list):
        name = input("Ingrese el nombre del estudiante: ")
        section = input("Ingrese la sección (Ejemplo 11B): ")
        spanish_score = input("Inserte nota de español: ")
        english_score = input("Inserte nota de inglés: ")
        social_score = input("Inserte nota de sociales: ")
        science_score = input("Inserte nota de ciencias: ")
        students_list.append(Student(name, section, spanish_score, english_score, social_score, science_score))


#-----------Exportar CSV
def export_csv(student_documentation, filename="Estudiantes.csv"):
    dict_list = [student.to_dict() for student in student_documentation]
    fieldnames = dict_list[0].keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dict_list)
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
            spanish_score = int(row['spanish_score'])
            english_score = int(row['english_score'])
            social_score = int(row['social_score'])
            science_score = int(row['science_score'])
            student = Student(row['name'], row['section'], spanish_score, english_score, social_score, science_score)
            students_documentation.append(student)
    print(f"Datos importados correctamente desde '{filename}'.")
    return students_documentation