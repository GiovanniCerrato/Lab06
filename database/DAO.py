from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendita import Vendita


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnniVendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """select YEAR(date) as year 
                    from go_daily_sales ds
                    group by year(date) """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(int(row[0]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllBrands():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """select Product_brand
                    from go_products
                    group by Product_brand"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllRetailers():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                   from go_retailers"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Retailer(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllVendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                    from go_daily_sales"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Vendita(**row))

        cursor.close()
        cnx.close()
        return res
