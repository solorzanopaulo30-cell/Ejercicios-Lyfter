import csv
import os


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

def students_info():
    students_documentation =[
    {
        "nombre completo": "María José Solano Vargas",
        "seccion": "11B",
        "nota espanol": 85,
        "nota ingles": 92,
        "nota sociales": 78,
        "nota ciencias": 88
    },
    {
        "nombre completo": "Kendall Steven Rojas Mora",
        "seccion": "10A",
        "nota espanol": 70,
        "nota ingles": 65,
        "nota sociales": 80,
        "nota ciencias": 74
    },
    {
        "nombre completo": "Yendry Pamela Chacón Araya",
        "seccion": "11B",
        "nota espanol": 95,
        "nota ingles": 89,
        "nota sociales": 91,
        "nota ciencias": 93
    },
    {
        "nombre completo": "Jonathan Andrés Fallas Mora",
        "seccion": "9C",
        "nota espanol": 60,
        "nota ingles": 55,
        "nota sociales": 68,
        "nota ciencias": 62
    },
    {
        "nombre completo": "Dayana Michelle Salas Quesada",
        "seccion": "10A",
        "nota espanol": 88,
        "nota ingles": 80,
        "nota sociales": 85,
        "nota ciencias": 90
    },
    {
        "nombre completo": "Kevin Josué Alvarado Cordero",
        "seccion": "11A",
        "nota espanol": 72,
        "nota ingles": 78,
        "nota sociales": 75,
        "nota ciencias": 70
    },
    {
        "nombre completo": "Karla Vanessa Zúñiga Bermúdez",
        "seccion": "9C",
        "nota espanol": 90,
        "nota ingles": 87,
        "nota sociales": 82,
        "nota ciencias": 85
    },
    {
        "nombre completo": "Esteban Alonso Jiménez Castro",
        "seccion": "11A",
        "nota espanol": 65,
        "nota ingles": 60,
        "nota sociales": 58,
        "nota ciencias": 63
    },
    {
        "nombre completo": "Nicole Fernanda Ureña Barrantes",
        "seccion": "10B",
        "nota espanol": 93,
        "nota ingles": 95,
        "nota sociales": 90,
        "nota ciencias": 91
    },
    {
        "nombre completo": "Luis Diego Vindas Segura",
        "seccion": "10B",
        "nota espanol": 55,
        "nota ingles": 62,
        "nota sociales": 60,
        "nota ciencias": 58
    }
]
    return students_documentation