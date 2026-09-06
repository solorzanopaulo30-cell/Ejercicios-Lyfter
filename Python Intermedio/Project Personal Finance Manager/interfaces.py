import FreeSimpleGUI as sg
from logica import FinancialMgmt, Entry, Spend
from persistencia import save, load

DATA_FILE = "finanzas.json"


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







def open_windows_category(manager):
    layout = [
        [sg.Text("Ingrese su categoria:")],
        [sg.InputText(key="category")],
        [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
    window = sg.Window("Agregar Categoria", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED,"Cancelar"):
            break
        elif event == "Confirmar":
            name = values["category"].strip()
            if name == "":
                sg.popup_error("No puede estar vacia la categoria")
                continue
            if name in manager.categories:
                sg.popup_error("No puede estar duplicado")
                continue
            manager.add_categories(name)
            break
    window.close()


def open_movement_window(manager,kind):
    if len(manager.categories) == 0:
        sg.popup_error("No hay categorias disponibles. Agregue una primero.")
        return
    
    layout = [[sg.Text("titulo")],
            [sg.InputText(key = "title")],
            [sg.Text("Monto")],
            [sg.InputText(key ="amount")],
            [sg.Text("Categoria")],
            [sg.Combo(manager.categories,key = "category", readonly=True)],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
            ]
    window = sg.Window("Agregar Transaccion", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED,"Cancelar"):
            break
        if event == "Confirmar":
            title = values["title"].strip()
            amount_text = values["amount"].strip()
            category = values["category"]
            if title == "":
                sg.popup_error("El titulo no puede estar vacio")
                continue
            if not amount_text.replace(".", "", 1).isdigit():
                sg.popup_error("El monto debe ser un numero valido")
                continue
            if category == "":
                sg.popup_error("Debe seleccionar una categoria")
                continue
            amount = float(amount_text)
            if kind == "expense":
                movement = Spend(amount, category)
            else:
                movement = Entry(amount, category)
            balance_before = manager.balance
            manager.add_movements(movement)
            if manager.balance == balance_before and kind == "expense":
                sg.popup_error("Saldo insuficiente para este gasto")
                continue
            save(manager, DATA_FILE)
            break
    window.close()


def main():
    manager = load(DATA_FILE)
    if manager is None:
        manager = FinancialMgmt()
    layout = [
        [sg.Text("Gestor de Finanzas", font=("Arial", 16))],
        [sg.Text(f"Balance actual: {manager.balance}", key="balance")],
        [sg.Table(values=manager.get_movements_table(), headings=["Fecha", "Categoria", "Monto", "Tipo"], key="table")],
        [sg.Button("Agregar Categoria"), sg.Button("Agregar Gasto"), sg.Button("Agregar Ingreso"), sg.Button("Salir")]
    ]
    window = sg.Window("Finanzas Personales", layout, finalize=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            save(manager, DATA_FILE)
            break
        elif event == "Agregar Categoria":
            open_windows_category(manager)
        elif event == "Agregar Gasto":
            open_movement_window(manager, "expense")
        elif event == "Agregar Ingreso":
            open_movement_window(manager, "income")
        window["table"].update(values=manager.get_movements_table())
        window["balance"].update(f"Balance actual: {manager.balance}")
    window.close() 



if __name__ == '__main__':
    main()