#Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:


empleados = [
    {"nombre": "Juan", "correo": "juan@empresa.com", "departamento": "Ventas"},
    {"nombre": "María", "correo": "maria@empresa.com", "departamento": "Marketing"},
    {"nombre": "Pedro", "correo": "pedro@empresa.com", "departamento": "Ventas"},
    {"nombre": "Ana", "correo": "ana@empresa.com", "departamento": "RRHH"}
]

departamentos = {}
for empleado in empleados:
    dept = empleado["departamento"]
    if dept not in departamentos:
        departamentos[dept] = []
    departamentos[dept].append(empleado)
    
print("Departamentos:")
for dept, emp_list in departamentos.items():
    print(f"{dept}:")
    for emp in emp_list:
        print(f"  - {emp['nombre']}")