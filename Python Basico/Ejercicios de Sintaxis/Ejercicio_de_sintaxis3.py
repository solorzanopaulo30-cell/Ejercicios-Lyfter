
import random


secret_number = random.randint(1, 10)
while True:
    user_number = int(input("Adivina el número secreto (1-10): "))
    if user_number == secret_number:
        print("¡Correcto! Has adivinado el número.")
        break
    else:
        print("Incorrecto. Inténtalo de nuevo.")