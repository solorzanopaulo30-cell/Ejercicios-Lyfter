#10. Cree un programa que simule un cajero automático simple: menú con "Consultar saldo", "Depositar", "Retirar" y "Salir", usando un `while`.


def ATM():
    balance = 0
    while True:
        print("--- Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        option = input("Elija una opción: ")

        if option == "1":
            print(f"Su saldo actual es: {balance}")
        elif option == "2":
            amount = float(input("Ingrese el monto a depositar: "))
            balance += amount
            print(f"Depósito exitoso. Nuevo saldo: {balance}")
        elif option == "3":
            amount = float(input("Ingrese el monto a retirar: "))
            if amount > balance:
                print("Saldo insuficiente")
            else:
                balance -= amount
                print(f"Retiro exitoso. Nuevo saldo: {balance}")
        elif option == "4":
            print("Gracias por usar el cajero")
            break
        else:
            print("Opción inválida")

ATM()