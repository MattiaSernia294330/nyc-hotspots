import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self.ddProvider=None
        self.btnGrafo=None
        self.txtDistanza=None
        self.btnAnalizza=None
        self.txtStringa=None
        self.btnCalcolaP=None
        self.ddTarget=None
        self.txt_result=None


    def load_interface(self):
        # title
        self._title = ft.Text("NYC-Hotspot", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txtDistanza = ft.TextField(
            label="Distanza(x)",
            width=200,
            on_change=self._controller.readDistanza
        )
        self.ddProvider = ft.Dropdown(label="Provider",width=200)

        # button for the "hello" reply
        self.btnGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleGraph, width=200)
        row1 = ft.Row([self.ddProvider, self.btnGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self.btnAnalizza = ft.ElevatedButton(text="Analizza", on_click=self._controller.handleAnalizza,width=200)
        row2 = ft.Row([self.txtDistanza, self.btnAnalizza], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self.txtStringa = ft.TextField(
            label="Stringa(s)",
            width=200,
        )
        self.btnCalcolaP = ft.ElevatedButton(text="calcola Percorso", on_click=self._controller.handleCalcolaP, width=200)
        row3 = ft.Row([self.txtStringa, self.btnCalcolaP], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self.ddTarget = ft.Dropdown(label="Target",width=200)
        row4=ft.Row([self.ddTarget], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)
        # List View where the reply is printed
        self._controller.fillDD()
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
