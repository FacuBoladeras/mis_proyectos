import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Prueba CRUD"
    page.scroll = "adaptive"
    page.bgcolor = "#FFFFFFFF"
   
    
       
    boton_tipo = ft.Row(controls=[ft.Dropdown(
            
            label="Tipo de plan",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("Trimestral"),
                ft.dropdown.Option("Cuatrimestral"),
                ft.dropdown.Option("Semestral"),
                ft.dropdown.Option("Anual"),
            ],            
            width=500,
            
        )], alignment=ft.MainAxisAlignment)
    
    texto = ft.Text(boton_tipo.key)
    texto2 = texto.value
    print(texto2)
    panel = ft.Row([
                ft.Container(
                    content=ft.Text(texto2),
                    margin=20,
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREY_200,
                    width=1800,
                    height=400,
                    border_radius=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    boton_buscar = ft.Row(controls=[ft.ElevatedButton("Buscar", data=0)],alignment=ft.MainAxisAlignment.CENTER)
    
    
    page.add(boton_tipo,panel)
    
    
ft.app(main)