import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_topVendite = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.dd_anno = ft.Dropdown(
            label="Anno",
            options=[
                ft.dropdown.Option(key="Nessun filtro", data = None, on_click= self._controller._choiceDDanno)
            ]
        )
        self._controller.filldd_anno()
        self._page.update()

        self.dd_brand = ft.Dropdown(
            label="Brand",
            options=[
                ft.dropdown.Option(key="Nessun filtro", data = None, on_click= self._controller._choiceDDbrand)
            ]
        )
        self._controller.filldd_brand()
        self._page.update()
        self.dd_retailer = ft.Dropdown(
            label="Retailer",
            expand = True,
            options=[
                ft.dropdown.Option(key="Nessun filtro", data = None, on_click= self._controller._choiceDDretailer)
            ],

        )
        self._controller.filldd_retailer()
        self._page.update()

        row1 = ft.Row([self.dd_anno, self.dd_brand, self.dd_retailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.btn_topVendite = ft.ElevatedButton(text="Top Vendite", on_click=self._controller.handle_topVendite)
        self.btn_analizzaVendite = ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.handle_analizzaVendite)

        row2 = ft.Row([self.btn_topVendite, self.btn_analizzaVendite], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)
        # List View where the reply is printed
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
