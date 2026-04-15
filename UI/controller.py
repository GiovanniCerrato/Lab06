import copy

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

        self._vendite = None
        self._prodotti = None


    def handle_topVendite(self,e):
        self._view.txt_result.clean()
        if not self._vendite:
            self._vendite = self._model.getAllVendite()
        res = self._vendite[:]

        if self._annoSelezionato:
            res = [e for e in res if e.Date.year == self._annoSelezionato]

        if self._brandSelezionato:
            if not self._prodotti:
                self._prodotti = self._model.getAllProduct()
            product_numbers = []
            for p in self._prodotti:
                if p.Product_brand == self._brandSelezionato:
                    product_numbers.append(p.Product_number)
                    print(p.Product_brand)
            res = [vendita for vendita in res if vendita.Product_number in product_numbers]

        if self._retailerSelezionato:
            res = [vendita for vendita in res if vendita.Retailer_code == self._retailerSelezionato.Retailer_code]

        topFive = res[0:5]
        if not res:
            topFive = self._vendite[0:5]
        for vendita in topFive:
            self._view.txt_result.controls.append(ft.Text(f"{vendita}"))
            self._view.update_page()


    def handle_analizzaVendite(self,e):
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
                text = f"{retailer.Retailer_name} ({retailer.Retailer_code})",
                data=retailer,
                on_click= self._choiceDDretailer
            ))

    def _choiceDDretailer(self,e):
        self._retailerSelezionato = e.control.data
        print(self._retailerSelezionato)


