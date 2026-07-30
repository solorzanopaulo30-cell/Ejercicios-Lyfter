
time = int(input("Ingrese un tiempo en segundos: "))
if time < 600:
    remain_time = 600 - time
    print(f"Faltan {remain_time} segundos para llegar a 10 minutos.")
elif time > 600:
    print("Mayor")
else:
    print("Igual")