# Ejercicio de Normalización: Registro de Clases

## Tabla original

| Student_ID | Student_Name | Course_Code | Course_Name | Instructor_Name | Instructor_Email |
| --- | --- | --- | --- | --- | --- |
| 301 | Marco Gómez | CS101 | Python I | Juan Pérez | juan@uni.edu |
| 301 | Marco Gómez | CS102 | Python II | Laura Rojas | laura@uni.edu |
| 302 | Carla Ruiz | CS101 | Python I | Juan Pérez | juan@uni.edu |

## 1FN

La tabla queda igual, con la llave primaria compuesta (Student_ID, Course_Code).

| Student_ID | Student_Name | Course_Code | Course_Name | Instructor_Name | Instructor_Email |
| --- | --- | --- | --- | --- | --- |
| 301 | Marco Gómez | CS101 | Python I | Juan Pérez | juan@uni.edu |
| 301 | Marco Gómez | CS102 | Python II | Laura Rojas | laura@uni.edu |
| 302 | Carla Ruiz | CS101 | Python I | Juan Pérez | juan@uni.edu |

Justificación: la tabla cumple la 1FN porque cada celda tiene un solo valor y la llave primaria es compuesta: (Student_ID, Course_Code). Student_ID se repite (301) y Course_Code también (CS101), pero la pareja no se repite.

## 2FN

Students (PK: Student_ID)

| Student_ID | Student_Name |
| --- | --- |
| 301 | Marco Gómez |
| 302 | Carla Ruiz |

Courses (PK: Course_Code)

| Course_Code | Course_Name | Instructor_Name | Instructor_Email |
| --- | --- | --- | --- |
| CS101 | Python I | Juan Pérez | juan@uni.edu |
| CS102 | Python II | Laura Rojas | laura@uni.edu |

Enrollments (PK: Student_ID, Course_Code. FK: ambas)

| Student_ID | Course_Code |
| --- | --- |
| 301 | CS101 |
| 301 | CS102 |
| 302 | CS101 |

Justificación: en la 2FN reviso qué columnas dependen solo de una parte de la llave (Student_ID, Course_Code).

- Solo de Student_ID: Student_Name. Pasa a Students.
- Solo de Course_Code: Course_Name, Instructor_Name e Instructor_Email. Pasan a Courses.
- De las dos: ninguna. Por eso Enrollments solo guarda la llave y registra quién está inscrito en qué curso.

## 3FN

Instructors (PK: Instructor_ID)

| Instructor_ID | Instructor_Name | Instructor_Email |
| --- | --- | --- |
| 1 | Juan Pérez | juan@uni.edu |
| 2 | Laura Rojas | laura@uni.edu |

Courses (PK: Course_Code. FK: Instructor_ID)

| Course_Code | Course_Name | Instructor_ID |
| --- | --- | --- |
| CS101 | Python I | 1 |
| CS102 | Python II | 2 |

Students y Enrollments quedan igual que en la 2FN.

Justificación: en la 3FN encuentro una dependencia transitiva: Instructor_Email no depende directamente de Course_Code, sino del instructor (Course_Code → Instructor_Name → Instructor_Email). Creo una tabla Instructors con Instructor_ID como llave primaria, y uso un ID en lugar del nombre porque dos instructores podrían llamarse igual. Courses guarda solo Instructor_ID como llave foránea. Así, los datos de cada instructor aparecen una sola vez.

## Notas

- Supuesto: cada curso lo da un solo instructor.