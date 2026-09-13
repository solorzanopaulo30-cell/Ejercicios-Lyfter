from datetime import date


class Category():
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

    @staticmethod
    def from_dict(data):
        return Category(data["name"])


class Movement():
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date.today()

    def __str__(self):
        return f"[{self.date}] {self.title} - {self.category.name}: {self.amount}"

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category.name,
            "date": str(self.date),
            "type": type(self).__name__
        }

    @staticmethod
    def from_dict(data, categories):
        category = next((c for c in categories if c.name == data["category"]), None)
        if data["type"] == "Entry":
            return Entry(data["title"], data["amount"], category)
        else:
            return Spend(data["title"], data["amount"], category)


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

    def add_categories(self, category_name):
        if category_name == "":
            print("Category cannot be empty")
            return
        if any(c.name == category_name for c in self.categories):
            print("This category already exists")
            return
        self.categories.append(Category(category_name))

    def add_movements(self, movement):
        if len(self.categories) == 0:
            raise ValueError("No hay categorias disponibles")
        hypothetical_balance = self.balance + movement.apply()
        if hypothetical_balance < 0:
            raise ValueError("Saldo insuficiente")
        self.movements.append(movement)
        self.balance = hypothetical_balance

    def total_per_category(self, category_name):
        total = 0
        for movement in self.movements:
            if movement.category.name == category_name:
                total += movement.apply()
        return total

    def get_movements_table(self):
        pivot = []
        for movement in self.movements:
            type_ = "ENTRY" if isinstance(movement, Entry) else "SPEND"
            row = [movement.date, movement.title, movement.category.name, movement.amount, type_]
            pivot.append(row)
        return pivot

#----------------------------------------------------------------------------------

