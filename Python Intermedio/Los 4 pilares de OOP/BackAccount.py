class BankAccount():
    def __init__(self,balance):
        self.balance = balance 

    def EnterMoney (self):
        new_money = int(input("Ingrese el monto a añadir: "))
        new_balance = new_money + self.balance
        self.balance = new_balance
        print(f"Tu balance actual es de: {self.balance}")
        return self.balance

    def Deposit (self):
        new_deposit = int(input("Ingrese el monto a debitar: "))
        self.balance = self.balance - new_deposit
        print(f"el monto debitado es de {new_deposit} y su balance actual es de {self.balance}")


class SavingAccount(BankAccount):
    def __init__(self,balance,min_balance):
        self.min_balance = min_balance
        super().__init__(balance)

    def Deposit(self):
        new_deposit = int(input("Ingrese el monto a debitar: "))
        if (self.balance - new_deposit) < self.min_balance:
            raise ValueError("Balance insuficiente para retirar")
        self.balance = self.balance - new_deposit
        print(f"el monto debitado es de {new_deposit} y su balance actual es de {self.balance}")


my_account = SavingAccount(500,100)

try:
    my_account.Deposit()
except ValueError as error:
    print(error)
