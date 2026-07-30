
price = float(input("Ingrese el precio del producto: "))
if price < 100:
    discount = price * 0.02
    price = price - discount
else:
    discount = price * 0.10 
    price = price - discount
print(f"El precio final es: {price}")