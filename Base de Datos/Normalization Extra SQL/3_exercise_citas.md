# Ejercicio de Normalización: Hospital y Citas Médicas

## Tabla original

| Appointment_ID | Patient_Name | Patient_Phone | Doctor_Name | Specialty | Date | Time |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Diana Vargas | 8888-1111 | Dr. Soto | Pediatría | 2024-08-01 | 10:00 AM |
| A02 | Diana Vargas | 8888-1111 | Dr. Soto | Pediatría | 2024-08-10 | 10:00 AM |
| A03 | Edwin Mora | 8999-2222 | Dr. Mora | Cardiología | 2024-08-05 | 01:00 PM |

## 1FN

La tabla queda igual, con la llave primaria Appointment_ID.

| Appointment_ID | Patient_Name | Patient_Phone | Doctor_Name | Specialty | Date | Time |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Diana Vargas | 8888-1111 | Dr. Soto | Pediatría | 2024-08-01 | 10:00 AM |
| A02 | Diana Vargas | 8888-1111 | Dr. Soto | Pediatría | 2024-08-10 | 10:00 AM |
| A03 | Edwin Mora | 8999-2222 | Dr. Mora | Cardiología | 2024-08-05 | 01:00 PM |

Justificación: la tabla cumple la 1FN porque cada celda tiene un solo valor y la llave primaria es Appointment_ID, que no se repite en ninguna fila.

## 2FN

La tabla queda igual que en la 1FN.

| Appointment_ID | Patient_Name | Patient_Phone | Doctor_Name | Specialty | Date | Time |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Diana Vargas | 8888-1111 | Dr. Soto | Pediatría | 2024-08-01 | 10:00 AM |
| A02 | Diana Vargas | 8888-1111 | Dr. Soto | Pediatría | 2024-08-10 | 10:00 AM |
| A03 | Edwin Mora | 8999-2222 | Dr. Mora | Cardiología | 2024-08-05 | 01:00 PM |

Justificación: la 2FN revisa las dependencias de una parte de la llave. Como la llave primaria es de una sola columna (Appointment_ID), no puede haber dependencias parciales, y la tabla ya cumple la 2FN sin cambios.

## 3FN

Patients (PK: Patient_ID)

| Patient_ID | Patient_Name | Patient_Phone |
| --- | --- | --- |
| 1 | Diana Vargas | 8888-1111 |
| 2 | Edwin Mora | 8999-2222 |

Doctors (PK: Doctor_ID)

| Doctor_ID | Doctor_Name | Specialty |
| --- | --- | --- |
| 1 | Dr. Soto | Pediatría |
| 2 | Dr. Mora | Cardiología |

Appointments (PK: Appointment_ID. FK: Patient_ID, Doctor_ID)

| Appointment_ID | Patient_ID | Doctor_ID | Date | Time |
| --- | --- | --- | --- | --- |
| A01 | 1 | 1 | 2024-08-01 | 10:00 AM |
| A02 | 1 | 1 | 2024-08-10 | 10:00 AM |
| A03 | 2 | 2 | 2024-08-05 | 01:00 PM |

Justificación: en la 3FN encuentro dos dependencias transitivas: Appointment_ID → Patient_Name → Patient_Phone y Appointment_ID → Doctor_Name → Specialty. El teléfono depende del paciente y la especialidad depende del doctor, no de la cita. Creo las tablas Patients y Doctors, cada una con su ID como llave primaria, y uso un ID en lugar del nombre porque dos personas podrían llamarse igual. Appointments guarda solo Patient_ID y Doctor_ID como llaves foráneas, más Date y Time, que dependen directamente de la cita. Así, los datos de cada paciente y de cada doctor aparecen una sola vez.

## Notas

- Supuesto: cada doctor tiene una sola especialidad.
- Supuesto: Diana Vargas aparece en dos citas con el mismo teléfono, así que se trata como un solo paciente.