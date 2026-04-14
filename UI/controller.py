import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._annoSelezionato = None
        self._brandSelezionato = None
        self._retailerSelezionato = None

    def handle_topVendite(self):
        pass

    def handle_analizzaVendite(self):
        pass

    def filldd_anno(self):
        anni = self._model.getAnniVendite()
        for anno in  anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(
                key = anno,
                data = anno,
                on_click= self._choiceDDanno
            ))
        self._view.update_page()

    def _choiceDDanno(self,e):
        self._annoSelezionato = e.control.data
        print(self._annoSelezionato)

    def filldd_brand(self):
        brands = self._model.getAllBrands()
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(
                key=brand,
                data=brand,
                on_click=self._choiceDDbrand
            ))
        self._view.update_page()

    def _choiceDDbrand(self,e):
        self._brandSelezionato = e.control.data
        print(self._brandSelezionato)

    def filldd_retailer(self):
        retailers = self._model.getAllRetailers()
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(
                key= retailer.Retailer_code,
                data=retailer,
                on_click= self._choiceDDretailer
            ))

    def _choiceDDretailer(self,e):
        self._retailerSelezionato = e.control.data
        print(self._retailerSelezionato)


