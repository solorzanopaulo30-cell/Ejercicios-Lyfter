#Acceso por clave, `.keys()`, `.items()`, diccionarios anidados.
#5. Cree una función que reciba una lista de diccionarios de empleados y agrupe sus nombres por departamento.


def group_by_department(employees):
    department_dict = {}
    for employee in employees:
        department = employee['department']
        name = employee['name']
        if department not in department_dict:
            department_dict[department] = []
        department_dict[department].append(name)
    return department_dict


employees = [
    {'name': 'Alice', 'department': 'Engineering'},
    {'name': 'Bob', 'department': 'Marketing'},
    {'name': 'Charlie', 'department': 'Engineering'},
    {'name': 'David', 'department': 'Marketing'}
]

print(group_by_department(employees))