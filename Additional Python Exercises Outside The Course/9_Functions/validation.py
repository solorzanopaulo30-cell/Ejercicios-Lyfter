#4. Cree dos módulos que se complementen: uno con funciones de validación, otro que las use para un formulario simple.



def validate_name(name):
    if len(name) < 3:
        return False
    return True

def validate_email(email):
    if "@" not in email:
        return False
    return True

def validate_age(age):
    if not isinstance(age, int):
        return False
    if age < 0:
        return False
    return True
