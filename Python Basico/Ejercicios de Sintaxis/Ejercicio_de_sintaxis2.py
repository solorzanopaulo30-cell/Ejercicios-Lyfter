
name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age <= 1:
    category = "Bebé"
elif age <= 10:
    category = "Niño"
elif age <= 12:
    category = "Preadolescente"
elif age <= 16:
    category = "Adolescente"
elif age <= 18:
    category = "Adulto Joven"
elif age <= 30:
    category = "Adulto"
elif age <= 60:
    category = "Adulto Mayor"
else:
    category = "Anciano"
print(f"{name} {last_name} es un {category}.")
