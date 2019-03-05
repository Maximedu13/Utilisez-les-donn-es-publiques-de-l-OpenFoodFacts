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
                                   db='Open_Food_Facts')
        self.cursor = self.cnx.cursor()

    def connect(self):
        try:
            # Trying to connect to the database...
            self.cnx
        except pymysql.InternalError:
            print("No database found, the system is creating a new one...")
            self.cnx
            self.import_sql_file(self.cursor, "create_bdd.sql")
        return self.cnx

    def fill_bdd_categories(self):
        self.cursor.execute(query_create_all_categories)
        self.cnx.commit()

    def get_categories(self):
        self.cursor.execute(query_display_all_categories)
        for row in self.cursor:
            print(row)

    def get_products(self):
        self.cursor.execute(query_display_all_products)
        for row in self.cursor:
            print('{0} - {1}'.format(row[0], row[1]))

    def get_product_details(self, barcode):

        r = requests.get("https://world.openfoodfacts.org/api/v0/product/"+str(barcode)+".json")

        result = json.loads(r.text)
        print("Nom du produit :" + result["product"]["product_name_fr"])

        #requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + category["name"] + "&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=display&json=1"