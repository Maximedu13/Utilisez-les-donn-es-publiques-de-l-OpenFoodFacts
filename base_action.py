# coding=utf-8
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

    def get_products(self):
        self.mysql.cur.execute(query_display_all_products)
        for row in self.mysql.cur:
            print('{0} - {1} - {2}'.format(row[0], row[1], row[2]))

    def display_details(self):
        for row in self.mysql.cur:
            print(('Nom : {0}' + "\n"
                  'Marque : {1}' + "\n"
                  'Score nutritionnel : {2}' + "\n"
                  'Calories : {3} kcal' + "\n" 
                  'Sucres : {4} g' + "\n"
                  'Sels : {5} g' + "\n"
                  'Lipides : {6} g' + "\n"
                  'Protéines : {7} g' + "\n"
                  'Description : {8}' + "\n"
                  'Disponible en : {9}' + "\n"
                  'Image : {10}' + "\n"
                  'Catégorie : {11}').format(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]))

    def get_product_details(self):
        self.mysql.cur.execute(query_display_product_details)
        self.display_details()
    
    def display_substitutes(self):
        self.mysql.cur.execute(find_a_substitute)
        self.display_details()
        
    def replace_characters(self):
        for product in self.list_products:
            product = product.replace(' ', "-")
            product = product.replace('‘', "-")
            product = product.replace('à', "a")
            product = product.lower()
            self.list_products = []
            self.list_ch.append(product)

    def insert_products(self):
        self.replace_characters()
        r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + self.list_ch[choice_second_level - 1] + "&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=display&json=1")
        result = json.loads(r.text)
        for i in range(len(result["products"])):
            self.iD = i + 1
            try :
                self.brand = result["products"][i]["brands"]
                self.nutri_score = result["products"][i]["nutrition_grade_fr"]
                self.calories = float(result["products"][i]["nutriments"]["energy_100g"])
                # Kilojoules(kJ) to calories(cal)
                self.calories /= 4.184
                self.sugars = result["products"][i]["nutriments"]["sugars_100g"]
                self.salts = result["products"][i]["nutriments"]["salt_100g"]
                self.lipids = result["products"][i]["nutriments"]["fat_100g"]
                self.proteins = result["products"][i]["nutriments"]["proteins_100g"]
                self.location_available = result["products"][i]["countries"]
                self.category_id = 4
                self.name = result["products"][i]["product_name_fr"]
                self.description = result["products"][i]["generic_name"]
                self.url_image = result["products"][i]["image_small_url"]
                val = (
                self.iD, self.name, self.brand, self.nutri_score, self.calories, self.sugars, self.salts, self.lipids,
                self.proteins, self.description, self.location_available, self.url_image, self.category_id)
                self.mysql.cur.execute(
                    query_insert_all_products.format(table="product", f1="iD", f2="name", f3="brand", f4="nutri_score",
                                                     f5="calories", f6="sugars", f7="salts", f8="lipids", f9="proteins",
                                                     f10="description", f11="location_available", f12="url_image",
                                                     f13="category_id"), val)
                self.mysql.cnx.commit()
            except:
                pass

class Menu():
    action = Base_action()
    def __init__(self):
        self.message_input = "Entrez le chiffre correspondant et appuyez sur entrée."
        self.display_first_level()

    def first_choice_first_level(self):
        self.choice_first_level = str(input('Entrez le chiffre correspondant et appuyez sur Entrée.'))
        if self.choice_first_level == "1":
            print('🤖 Oui. Voici ce que j‘ai. Veuillez choisir une catégorie.')
            self.action.fill_bdd()
            self.action.get_categories()
            self.first_choice_second_level()
        elif self.choice_first_level == "2":
            pass
        else:
            self.first_choice_first_level()

    def first_choice_second_level(self):
        global choice_second_level
        choice_second_level = int(input('Entrez le chiffre correspondant et appuyez sur entrée.'))
        print('🤖 Oui. Voici ce que j‘ai. Veuillez choisir un produit.')
        if type(choice_second_level) is int:
            self.action.insert_products()
            self.action.get_products()
            self.first_choice_third_level()
        else:
            self.first_choice_second_level()

    def first_choice_third_level(self):
        choice_third_level = int(input('Entrez le chiffre correspondant et appuyez sur entrée.'))
        print('🤖 Oui. Voici ce que j‘ai.')
        if type(choice_third_level) is int:
            self.action.get_product_details()
            self.first_choice_fourth_level()

    def first_choice_fourth_level(self):
        choice_fourth_level = str(input('Souhaitez-vous trouver un substitut plus sain au produit ?'))
        if choice_fourth_level == "oui" or choice_fourth_level == "OUI":
            print("Voici ci-dessous un substitut plus sain au produit précédent 🍎")
            self.action.display_substitutes()
            self.first_choice_fifth_level()
        elif choice_fourth_level == "non" or choice_fourth_level == "NON":
            self.display_first_level()
        else:
            self.first_choice_fourth_level()

    def first_choice_fifth_level(self):
        choice_fifth_level = str(input('Souhaitez-vous enregistrer ce substitut dans la base de données ?'))
        if choice_fifth_level == "oui" or choice_fifth_level == "OUI":
            print("ok")
        else:
            print("Tant pis 🍔. Retour au menu principal.")
            self.display_first_level()

    def display_first_level(self):
        # FIRST WE NEED TO VERIFIY WHAT THE USER WANTS
        print('Bonjour et bienvenue dans Open Food Facts,' + '\n' +
              'le programme qui vous aide à manger mieux 🍎.')
        print('1 - Quel aliment souhaitez-vous remplacer ?')
        print('2 - Retrouver mes aliments substitués.')
        self.first_choice_first_level()