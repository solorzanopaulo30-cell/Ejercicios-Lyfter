
def float_of_values(list_1):
    sum_total = 0
    for element in list_1:
        try:
            number = float(element)
            print(f"{number}sumando correctamente")
            sum_total += number
        except ValueError as error:
            print(f"elemento ivanlido {element}")
    print(f"total de la suma: {sum_total}")



float_of_values(["10","manzana","5.5","3","n/a"])