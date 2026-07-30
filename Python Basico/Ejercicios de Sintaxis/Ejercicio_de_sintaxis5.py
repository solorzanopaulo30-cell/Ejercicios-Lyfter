
n = int(input("¿Cuántas notas vas a ingresar?: "))

notes = []
for i in range(n):
    note = float(input(f"Ingrese la nota {i + 1}: "))
    notes.append(note)

aproved = [note for note in notes if note >= 70]
failed = [note for note in notes if note < 70]

total_average = sum(notes) / len(notes) if notes else 0
approved_average = sum(aproved) / len(aproved   ) if aproved else 0
disapproved_average = sum(failed) / len(failed) if failed else 0

print(f"\nNotas aprobadas: {len(aproved)}")
print(f"Notas desaprobadas: {len(failed)}")
print(f"Promedio general: {total_average:.2f}")
print(f"Promedio de aprobadas: {approved_average:.2f}")
print(f"Promedio de desaprobadas: {disapproved_average:.2f}")