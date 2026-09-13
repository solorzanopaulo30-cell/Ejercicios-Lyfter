import FreeSimpleGUI as sg
from logica import FinancialMgmt, Entry, Spend
from persistencia import save, load

DATA_FILE = "finance.json"

#---------------------------------------------------------------------------------------------------------------------------------------------


def open_windows_category(manager):
    layout = [
        [sg.Text("Ingrese su categoria:")],
        [sg.InputText(key="category")],
        [sg.Button("Confirmar"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Agregar Categoria", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        elif event == "Confirmar":
            name = values["category"].strip()
            if name == "":
                sg.popup_error("No puede estar vacia la categoria")
                continue
            if any(c.name == name for c in manager.categories):
                sg.popup_error("No puede estar duplicado")
                continue
            manager.add_categories(name)
            save(manager, DATA_FILE)
            break
    window.close()


def open_movement_window(manager, kind):
    if len(manager.categories) == 0:
        sg.popup_error("No hay categorias disponibles. Agregue una primero.")
        return

    category_names = [c.name for c in manager.categories]

    layout = [
        [sg.Text("Titulo")],
        [sg.InputText(key="title")],
        [sg.Text("Monto")],
        [sg.InputText(key="amount")],
        [sg.Text("Categoria")],
        [sg.Combo(category_names, key="category", readonly=True)],
        [sg.Button("Confirmar"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Agregar Transaccion", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        if event == "Confirmar":
            title = values["title"].strip()
            amount_text = values["amount"].strip()
            category_name = values["category"]

            if title == "":
                sg.popup_error("El titulo no puede estar vacio")
                continue
            if not amount_text.replace(".", "", 1).isdigit():
                sg.popup_error("El monto debe ser un numero valido")
                continue
            if category_name == "":
                sg.popup_error("Debe seleccionar una categoria")
                continue

            amount = float(amount_text)
            category = next(c for c in manager.categories if c.name == category_name)

            if kind == "expense":
                movement = Spend(title, amount, category)
            else:
                movement = Entry(title, amount, category)

            try:
                manager.add_movements(movement)
            except ValueError as error:
                sg.popup_error(str(error))
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
        [sg.Table(values=manager.get_movements_table(), headings=["Fecha", "Titulo", "Categoria", "Monto", "Tipo"], key="table")],
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