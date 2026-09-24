#3. Cree una ventana con un `Combo` que permita elegir un color de una lista, y muestre el color elegido en un popup.



import FreeSimpleGUI as sg

layout = [
    [sg.Text("Elija un color:")],
    [sg.Combo(values=["Rojo", "Verde", "Azul", "Amarillo"], key="color")],
    [sg.Button("Mostrar Color"), sg.Button("Cerrar")]
]

window = sg.Window("Selector de Color", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Cerrar"):
        break
    elif event == "Mostrar Color":
        color_elegido = values["color"]
        sg.popup(f"El color elegido es: {color_elegido}")

window.close()
