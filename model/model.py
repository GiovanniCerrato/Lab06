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
        res.sort(key=lambda x: x.Date, reverse=True)
        return res