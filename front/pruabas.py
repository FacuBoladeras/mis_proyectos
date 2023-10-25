import flet as ft

def main(page: ft.Page):
    # Inicializa las filas de la tabla como una lista vacía
    rows = []

    async def button_clicked(e):
        t.value = f"Moto marca {tb2.value}'"
        new_row = ft.DataRow(ft.DataCell(ft.Text(tb2.value)))        
        # Agrega la nueva fila a la lista de filas
        rows.append(new_row.data)
        # Actualiza la tabla con las nuevas filas
        t1.rows = rows
        page.update()
        return(t.value)

    t = ft.Text()
    tb2 = ft.TextField(label="Marca", value="First name")
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    t1 = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=False),
            ],
            rows=rows,  # Usa la lista de filas para inicializar la tabla
        )

    page.add(tb2,b,t1)

ft.app(main)