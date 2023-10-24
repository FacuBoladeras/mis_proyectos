import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#FFFFFFFF"
    def dropdown_changed(e):
        t.value = f"{dd.value}"
        page.update()

    t = ft.Text()
    dd = ft.Dropdown(
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
        width=200,
    )
    print(type(dd))
    boton_tipo = ft.Row(controls=[ft.Dropdown(
            on_change=dropdown_changed,
            label="Tipo de plan",
            options=[
                ft.dropdown.Option("Trimestral"),
                ft.dropdown.Option("Cuatrimestral"),
                ft.dropdown.Option("Semestral"),
                ft.dropdown.Option("Anual"),
            ],            
            width=500,
            
        )], alignment=ft.MainAxisAlignment)
    print(type(boton_tipo))
    
    page.add(dd, t)


ft.app(target=main)