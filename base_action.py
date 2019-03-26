import pymysql
import requests, json
from classes import *
from database import *
from queries import *

class Base_action():
    def __init__(self):
        self.mysql = connection()
        self.db = self.mysql.connect()
        self.list_products = []
        self.list_ch = []

    def fill_bdd(self):
        self.mysql.cur.execute(query_reset)
        self.mysql.cur.execute(query_fill_bdd)
        self.mysql.cnx.commit()

    def get_categories(self):
        self.mysql.cur.execute(query_display_all_categories)
        for row in self.mysql.cur:
            self.list_products.append(row[1])
            print('{0} - {1}'.format(row[0], row[1]))

    def fill_products(self):
        self.mysql.cur.execute(query_display_all_categories)

    def get_products(self):
        self.mysql.cur.execute(query_display_all_products)
        for row in self.mysql.cur:
            print('{0} - {1}'.format(row[0], row[1]))

    def replace_characters(self):
        for product in self.list_products:
            product = product.replace(' ', "-")
            product = product.replace('‘', "-")
            product = product.replace('à', "a")
            product = product.lower()
            self.list_products = []
            self.list_ch.append(product)

    def insert_products(self):
        #r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=%22%20+%20pommes-noisettes%20+%20%22&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=display&json=1")  
        self.replace_characters()
        #for item in self.list_ch:
        #r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + item + "&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=display&json=1")
        r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=%22%20+%20pommes-noisettes%20+%20%22&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=display&json=1")
        result = json.loads(r.text)
        """for i in range(len(result["products"])):
            try :
                print (result["products"][i]["product_name_fr"] + ' - ' + result["products"][i]["brands"])
            except:
                print (result["products"][i]["product_name"])"""
        for i in range(len(result["products"])):
            try :
                self.name = result["products"][i]["product_name_fr"]
                self.description = result["products"][i]["generic_name"]
                self.url_image = result["products"][i]["image_small_url"]
                #print(str(i + 1) + " - " + result["products"][i]["product_name"] + " - " + result["products"][i]["brands"])
                #sys.exit()
            except:
                #print(result["products"][0])
                self.name = result["products"][i]["product_name"]
                self.description = ""
                self.url_image = result["products"][i]["image_ingredients_small_url"]
            self.iD = i + 1
            self.brand = result["products"][i]["brands"]
            self.nutri_score = result["products"][i]["nutrition_grade_fr"]
            self.calories = float(result["products"][i]["nutriments"]["energy_value"])
            self.sugars = float(result["products"][i]["nutriments"]["sugars_100g"])
            self.salts = float(result["products"][i]["nutriments"]["salt_100g"])
            self.lipids = float(result["products"][i]["nutriments"]["fat_100g"])
            self.proteins = float(result["products"][i]["nutriments"]["proteins_100g"])
            self.location_available = result["products"][i]["countries"]

            self.category_id = 4
            val = (self.iD, self.name, self.brand, self.nutri_score, self.calories, self.sugars, self.salts, self.lipids, self.proteins, self.description, self.location_available, self.url_image, self.category_id)
            self.mysql.cur.execute(query_insert_all_products.format(table="product", f1="iD", f2="name", f3="brand", f4="nutri_score", f5="calories", f6="sugars", f7="salts", f8="lipids", f9="proteins", f10="description", f11="location_available", f12="url_image", f13="category_id"), val)
            self.mysql.cnx.commit()
    def get_product_details(self):
        pass
        #requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + category["name"] + "&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=display&json=1"