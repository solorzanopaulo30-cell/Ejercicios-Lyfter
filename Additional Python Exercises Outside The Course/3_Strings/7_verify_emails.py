#
#7. Cree una función que reciba un email y valide (de forma simple) si contiene "@" y un ".".


def verify(mail):
    if "@" in mail and "." in mail:
        print("correo valido")
    else:
        raise ValueError("El correo no es válido")