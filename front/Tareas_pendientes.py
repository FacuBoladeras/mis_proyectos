import flet as ft


img = ft.Image(
        src=f"https://100seguro.com.ar/wp-content/uploads/2023/07/Logo-Rivadavia-FullHD-990x557.jpg",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,)

class Task(ft.UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,            
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Editar",
                            on_click=self.edit_clicked,
                                                    
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Eliminar",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Modificar",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    async def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        await self.update_async()

    async def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        await self.update_async()

    async def status_changed(self, e):
        self.completed = self.display_task.value
        await self.task_status_change(self)

    async def delete_clicked(self, e):
        await self.task_delete(self)


class TodoApp(ft.UserControl):
    
    def build(self):
        peticion =ft.TextField( hint_text="Marca",on_submit=self.add_clicked, expand=True, color= ft.colors.INDIGO_500)
        peticion2 =ft.TextField( hint_text="Modelo", on_submit=self.add_clicked, expand=True, color= ft.colors.INDIGO_500)
        peticion3 =ft.TextField( hint_text="Patente", on_submit=self.add_clicked, expand=True, color= ft.colors.INDIGO_500 )
        self.new_task = peticion
        self.new_task2 = peticion2
        self.new_task3 = peticion3
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            divider_color= ft.colors.INDIGO,
            label_color=ft.colors.INDIGO,
            unselected_label_color =ft.colors.INDIGO_200,
            overlay_color =ft.colors.INDIGO_100,
            tabs=[ft.Tab(text="Todo"), ft.Tab(text="Activo"), ft.Tab(text="Completo")],
        )

        self.items_left = ft.Text("0 archivos", color=ft.colors.BLACK)
        
        lista = []
        def agregar_val(e):
            
            valor = ft.Text(self.new_task.value)
            lista.append(valor)
            print(type(valor))        
        print(lista)
        
            
        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    [ft.Text(value="App Consecionaria", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color= ft.colors.INDIGO_500)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        self.new_task,
                        self.new_task2,
                        self.new_task3,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_clicked,
                        ),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                ft.OutlinedButton(
                                    text="Agregar", on_click=agregar_val,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    async def add_clicked(self, e):
        combined_value = self.new_task.value + " " + self.new_task2.value + " " + self.new_task3.value
        if combined_value.strip():
            task = Task(combined_value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.new_task2.value = ""
            await self.new_task.focus_async()
            await self.update_async()

    async def task_status_change(self, task):
        await self.update_async()

    async def task_delete(self, task):
        self.tasks.controls.remove(task)
        await self.update_async()

    async def tabs_changed(self, e):
        await self.update_async()

    async def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                await self.task_delete(task)

    async def update_async(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "Todo"
                or (status == "Activo" and task.completed == False)
                or (status == "Completo" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} items activos"
        await super().update_async()


async def main(page: ft.Page):
    page.title = "CRUD CONSECIONARIO"
    page.theme = ft.Theme(color_scheme_seed="blue")    
    page.bgcolor = "#FFFFFFFF"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # create app control and add it to the page
    await page.add_async(img,TodoApp())
    
ft.app(main)