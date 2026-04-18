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

        if len(res) < 5:
            topFive = [vendita for vendita in res]
        else:
            topFive = [res[i] for i in range(0,5)]
        if not topFive:
            self._view.create_alert("Nessun risultato trovato")
            return

        for vendita in topFive:
            self._view.txt_result.controls.append(ft.Text(f"{vendita}"))
            self._view.update_page()


    def handle_analizzaVendite(self,e):
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
            res = [vendita for vendita in res if vendita.Product_number in product_numbers]

        if self._retailerSelezionato:
            res = [vendita for vendita in res if vendita.Retailer_code == self._retailerSelezionato.Retailer_code]

        if not res:
            self._view.create_alert("Nessun risultato trovato")
            return
        giro_affari = 0
        numero_vendite = 0
        lista_retailer = []
        lista_prodotti = []
        for vendita in res:
            numero_vendite += 1
            if vendita.Retailer_code not in lista_retailer:
                lista_retailer.append(vendita.Retailer_code)
            if vendita.Product_number not in lista_prodotti:
                lista_prodotti.append(vendita.Product_number)
            giro_affari += vendita.Unit_sale_price * vendita.Quantity

        self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite:\nGiro d'affari: {giro_affari}\nNumero vendite: {numero_vendite}\nNumero Retailer coinvolti: {len(lista_retailer)}\nNumero prodotti coinvolti: {len(lista_prodotti)}"))
        self._view.update_page()


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


