# Ejercicio de Normalización: Empleados y Proyectos

## Tabla original

| Employee_ID | Employee_Name | Department | Department_Phone | Project_ID | Project_Name | Project_Budget |
| --- | --- | --- | --- | --- | --- | --- |
| 201 | Ana Rivera | IT | 2222-2222 | P001 | Web App | 50000 |
| 201 | Ana Rivera | IT | 2222-2222 | P002 | API REST | 25000 |
| 202 | Luis Mendez | Marketing | 1111-1111 | P003 | Campaña TV | 30000 |

## 1FN

La tabla queda igual, con la llave primaria compuesta (Employee_ID, Project_ID).

| Employee_ID | Employee_Name | Department | Department_Phone | Project_ID | Project_Name | Project_Budget |
| --- | --- | --- | --- | --- | --- | --- |
| 201 | Ana Rivera | IT | 2222-2222 | P001 | Web App | 50000 |
| 201 | Ana Rivera | IT | 2222-2222 | P002 | API REST | 25000 |
| 202 | Luis Mendez | Marketing | 1111-1111 | P003 | Campaña TV | 30000 |

Justificación: la tabla cumple la 1FN porque cada celda tiene un solo valor y la llave primaria es compuesta: (Employee_ID, Project_ID). Employee_ID se repite (201), pero la pareja con Project_ID no se repite.

## 2FN

Employees (PK: Employee_ID)

| Employee_ID | Employee_Name | Department | Department_Phone |
| --- | --- | --- | --- |
| 201 | Ana Rivera | IT | 2222-2222 |
| 202 | Luis Mendez | Marketing | 1111-1111 |

Projects (PK: Project_ID)

| Project_ID | Project_Name | Project_Budget |
| --- | --- | --- |
| P001 | Web App | 50000 |
| P002 | API REST | 25000 |
| P003 | Campaña TV | 30000 |

Employee_Projects (PK: Employee_ID, Project_ID. FK: ambas)

| Employee_ID | Project_ID |
| --- | --- |
| 201 | P001 |
| 201 | P002 |
| 202 | P003 |

Justificación: en la 2FN reviso qué columnas dependen solo de una parte de la llave (Employee_ID, Project_ID).

- Solo de Employee_ID: Employee_Name, Department y Department_Phone. Pasan a Employees.
- Solo de Project_ID: Project_Name y Project_Budget. Pasan a Projects.
- De las dos: ninguna. Por eso Employee_Projects solo guarda la llave y registra quién participa en qué proyecto.

## 3FN

Departments (PK: Department_ID)

| Department_ID | Department_Name | Department_Phone |
| --- | --- | --- |
| 1 | IT | 2222-2222 |
| 2 | Marketing | 1111-1111 |

Employees (PK: Employee_ID. FK: Department_ID)

| Employee_ID | Employee_Name | Department_ID |
| --- | --- | --- |
| 201 | Ana Rivera | 1 |
| 202 | Luis Mendez | 2 |

Projects y Employee_Projects quedan igual que en la 2FN.

Justificación: en la 3FN encuentro una dependencia transitiva: Department_Phone no depende directamente de Employee_ID, sino del departamento (Employee_ID → Department → Department_Phone). Creo una tabla Departments, con una fila por departamento y Department_ID como llave primaria. Employees guarda solo Department_ID como llave foránea. Así, el teléfono de cada departamento aparece una sola vez.