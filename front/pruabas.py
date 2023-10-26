import flet as ft

lista = []
def main(page: ft.Page):
    
    def button_clicked(e):
        t.value = {tb1.value}, {tb2.value}, {tb3.value}
        
        page.update()
        lista.append(t.value)
        print(lista)

    t = ft.Text()
    tb1 = ft.TextField(label="Marca")
    tb2 = ft.TextField(label="Modelo")
    tb3 = ft.TextField(label="Patente")
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, b, t)

ft.app(target=main)