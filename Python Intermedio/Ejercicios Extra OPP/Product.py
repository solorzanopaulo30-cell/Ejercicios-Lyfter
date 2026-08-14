

#------Products
class Product():
    def __init__(self,name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

#-------- Inventario 
class Invenroty():
    def __init__(self):
        self.purshed_list = []

    def add_product(self, product):
        self.purshed_list.append(product)

    def show_products(self):
        for product in self.purshed_list:
            print(f"nombre: {product.name}")
            print(f"el precio es de: {product.price}")
            print(f"la cantita de stock es de: {product.amount}")

    def calculate_value(self):
        total_value = 0
        for product in self.purshed_list:
            total_value += product.price * product.amount
        return total_value


#------------------------------------Run

stock = Invenroty()
product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

stock.add_product(product1)
stock.add_product(product2)

stock.show_products()
print(stock.calculate_value())  