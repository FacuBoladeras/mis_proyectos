import flet as ft
from flet import DataColumn, Text, DataTable

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Prueba CRUD"
    page.scroll = "adaptive"
    page.bgcolor = "#FFFFFFFF"    
    
    def button_clicked(e):
        t.value = f"Moto marca {tb2.value}'"
        new_row = ft.DataRow(ft.DataCell(ft.Text(tb2.value)))
        tb.rows.append(new_row)
        page.update()
    
    
    img = ft.Image(
        src=f"https://100seguro.com.ar/wp-content/uploads/2023/07/Logo-Rivadavia-FullHD-990x557.jpg",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,)
    
    
    t = ft.Text()
    tb2 = ft.TextField(label="Marca", value="First name")
    # tb3 = ft.TextField(label="Modelo")
    # tb4 = ft.TextField(label="Patente")
    # tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)  

    
    tb = DataTable(
	columns=[
		DataColumn(ft.Text("Marca")),
		DataColumn(ft.Text("Modelo")),
		DataColumn(ft.Text("Patente")),
	],
	rows=[]
)
    
    page.add(img, tb2, b, t, tb)
    
ft.app(main)