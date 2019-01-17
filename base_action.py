import pymysql
import requests, json
from queries import *



class Base_action():
    def __init__(self):
        self.db = self.connect
        self.categories_list = ()
        self.products_list = ()
        self.cnx = pymysql.connect(user='root',
                                   password='root',
                                   host='localhost',
                                   port=8889,
                                   charset='utf8',
                                   db='openfoodfact')
        self.cursor = self.cnx.cursor()

    def connect(self):
        try:
            # Trying to connect to the database...
            self.cnx
            
        except pymysql.InternalError:
            print("No database found...")

        return self.cnx

    def get_data(self):
        self.name = name
        self.category = category

    def get_categories(self):
        self.cursor.execute(query_select_all_categories)
        for row in self.cursor:
            print('{0}'.format(row[0]))

    def get_product_details(self, barcode):
        r = requests.get("https://world.openfoodfacts.org/api/v0/product/"+str(barcode)+".json")

        # Il faut convertir ton texte en dictionnaire
        result = json.loads(r.text)
        print(result["product"]["product_name_fr"])
