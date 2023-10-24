import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Prueba CRUD"
    page.scroll = "adaptive"
    page.bgcolor = "#FFFFFFFF"

    title_text = ft.Row(
                        controls=[ft.Stack([
                                            ft.Text(
                                                spans=[
                                                    ft.TextSpan(
                                                        "Ruben Rabbia Seguros",
                                                        ft.TextStyle(
                                                            size=70,
                                                            weight=ft.FontWeight.BOLD,
                                                            foreground=ft.Paint(
                                                                color=ft.colors.BLUE_800,
                                                                stroke_width=6,
                                                                stroke_join=ft.StrokeJoin.ROUND,
                                                                style=ft.PaintingStyle.STROKE,
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                                    ft.Text(
                                                spans=[
                                                            ft.TextSpan(
                                                                "Ruben Rabbia Seguros",
                                                                ft.TextStyle(
                                                                    size=70,
                                                                    weight=ft.FontWeight.BOLD,
                                                                    color=ft.colors.BLUE_200,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ]
                                    )
                                ],
                        alignment=ft.MainAxisAlignment.CENTER)
    
    img = ft.Image(
        src=f"https://100seguro.com.ar/wp-content/uploads/2023/07/Logo-Rivadavia-FullHD-990x557.jpg",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )
    boton_dia = ft.Row(controls=[ft.Dropdown(
            label="Dia",
            hint_text="Choose your favourite color?",
            options=[ft.dropdown.Option(f"{i}") for i in range(1,32)],            
            width=500,
        )],alignment=ft.MainAxisAlignment.START)
       
    
    boton_mes = ft.Row(controls=[ft.Dropdown(
        label="Mes",
        hint_text="Choose your favourite color?",
        options=[ft.dropdown.Option(f"{i}") for i in range(1,13)],
        width=500,
    )],alignment=ft.MainAxisAlignment)
    

    boton_año = ft.Row(controls=[ft.Dropdown(
            label="Año",
            hint_text="Choose your favourite color?",
            options=[
                ft.dropdown.Option("2022"),
                ft.dropdown.Option("2023"),      
            ],            
            width=500,
        )],alignment=ft.MainAxisAlignment)

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
        )],alignment=ft.MainAxisAlignment)
    
    panel = ft.Row([
                ft.Container(
                    content=ft.Text([]),
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
    
    row = ft.Row(controls=[boton_dia,boton_mes,boton_año],alignment=ft.MainAxisAlignment.CENTER)
    row2 = ft.Row(controls=[boton_dia,boton_mes,boton_año],alignment=ft.MainAxisAlignment.CENTER)
    row3 = ft.Row(controls=[boton_tipo, boton_buscar],alignment=ft.MainAxisAlignment.CENTER)
    
    page.add(title_text,img,row,row2,row3,panel)
    
    
ft.app(main)