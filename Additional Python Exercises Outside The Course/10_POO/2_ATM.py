#Clases, `__init__`, `self`, atributos, métodos.
#2. Cree una clase `CuentaBancaria` con métodos para depositar y retirar, validando que no se pueda retirar más de lo disponible.


class CuentaBancaria():
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")


cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)      
cuenta.retirar(2000)       
cuenta.retirar(300)        
cuenta.depositar(-50)      