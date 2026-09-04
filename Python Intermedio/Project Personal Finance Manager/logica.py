from datetime import date


class Movement():
    def __init__(self, amount, category=""):
        self.amount = amount
        self.category = category
        self.date = date.today()

    def __str__(self):
        return f"[{self.date}] {self.category} : {self.amount}"

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": str(self.date),
            "type": type(self).__name__
        }

    @staticmethod
    def from_dict(data):
        if data["type"] == "Entry":
            return Entry(data["amount"], data["category"])
        else:
            return Spend(data["amount"], data["category"])


class Entry(Movement):
    def apply(self) -> float:
        return self.amount


class Spend(Movement):
    def apply(self) -> float:
        return -abs(self.amount)


class FinancialMgmt():
    def __init__(self):
        self.categories = []
        self.movements = []
        self.balance = 0

    def add_categories(self, category):
        if category == "":
            print("Category cannot be empthy")
            return
        if category in self.categories:
            print("This category already exists")
            return
        self.categories.append(category)

    def add_movements(self, movement):
        if len(self.categories) == 0:
            print("No hay categorias disponibles")
            return
        hypothetical_balance = self.balance + movement.apply()
        if hypothetical_balance < 0:
            print("Insuficient balance")
            return
        self.movements.append(movement)
        self.balance = hypothetical_balance

    def total_per_category(self, category):
        total = 0
        for movement in self.movements:
            if movement.category == category:
                total += movement.apply()
        return total


    def get_movements_table(self):
        pivot = []
        for movement in self.movements:
            if isinstance(movement, Entry):
                type_ = "ENTRY"
            else:
                type_ = "SPEND"
            column = [movement.date, movement.category, movement.amount, type_]
            pivot.append(column)
        return pivot 


#----------------------------------------------------------------------------------
