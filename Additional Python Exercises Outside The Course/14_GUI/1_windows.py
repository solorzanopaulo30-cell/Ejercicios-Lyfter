#`layout`, `sg.Window`, loop de eventos, `sg.Table`, `sg.Combo`, `sg.InputText`.
#1. Cree una ventana simple con un campo de texto y un botón, que muestre un popup con "Hola, <nombre>" al confirmar.


import FreeSimpleGUI as sg

layout = [
    [sg.Text("Ingrese su nombre:")],
    [sg.InputText(key="nombre")],
    [sg.Button("Confirmar")]
]

window = sg.Window("Saludo", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Confirmar":
        nombre = values["nombre"]
        sg.popup(f"Hola, {nombre}")

window.close()