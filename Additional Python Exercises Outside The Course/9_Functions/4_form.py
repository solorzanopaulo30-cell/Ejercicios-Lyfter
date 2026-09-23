#4. Cree dos módulos que se complementen: uno con funciones de validación, otro que las use para un formulario simple.
from validation import validate_name, validate_email, validate_age


def validate_form(name, email, age):
    if not validate_name(name):
        return "Nombre inválido"
    if not validate_email(email):
        return "Correo electrónico inválido"
    if not validate_age(age):
        return "Edad inválida"
    return "Formulario válido"


validate_form("Juan", "juan@example.com", 25)