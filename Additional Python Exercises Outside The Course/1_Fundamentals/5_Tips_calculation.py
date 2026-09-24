#5. Cree una calculadora de propina: reciba el monto de la cuenta y el porcentaje deseado, y muestre el total a pagar.

def tips_calculator(bill, percentage):
    tip = (bill * percentage)/100
    result = bill + tip
    print(f"the total amount to pay is {result}")

tips_calculator(500,10)
