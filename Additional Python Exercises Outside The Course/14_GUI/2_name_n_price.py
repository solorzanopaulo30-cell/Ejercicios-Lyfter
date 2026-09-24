#2. Cree una ventana con una tabla que muestre una lista fija de productos (nombre y precio).



import FreeSimpleGUI as sg

layout = [
    [sg.Text("Lista de Productos")],
    [sg.Table(values=[["Producto 1", "$10"], ["Producto 2", "$20"], ["Producto 3", "$30"]],
                headings=["Nombre", "Precio"],
                auto_size_columns=False,
                justification="center",
                num_rows=3,
                key="tabla")],
    [sg.Button("Cerrar")]      
]

window = sg.Window("Productos", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Cerrar"):
        break

window.close()