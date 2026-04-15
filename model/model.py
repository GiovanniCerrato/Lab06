from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAnniVendite(self):
        res = DAO.getAnniVendite()
        return res

    def getAllBrands(self):
        return DAO.getAllBrands()

    def getAllRetailers(self):
        return DAO.getAllRetailers()

    def getAllVendite(self):
        res = DAO.getAllVendite()
        res.sort(key=lambda x: x.Unit_sale_price * x.Quantity, reverse=True)
        return res

    def getBrandFromPN(self,PN):
        return DAO.getBrandFromPN(PN)

    def getAllProduct(self):
        return DAO.getAllProducts()