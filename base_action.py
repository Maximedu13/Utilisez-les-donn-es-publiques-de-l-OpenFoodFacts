"""base_action.py"""
# coding=utf-8
import json
import requests
from database import Connection
from queries import *
import pymysql

class Base_action():
    def __init__(self):
        self.mysql = Connection()
        self.db = self.mysql.connect()
        self.list_products = []
        self.list_ch = []

    def fill_bdd(self):
        """Method to fill the database"""
        self.mysql.cur.execute(QUERY_RESET)
        self.mysql.cur.execute(QUERY_FILL_BDD)
        self.mysql.cnx.commit()

    def check_category(self):
        """Method to check if the number category exists"""
        self.mysql.cur.execute(QUERY_DISPLAY_ALL_CATEGORIES)

    def check_product(self):
        """Method to check if the number product exists"""
        self.mysql.cur.execute(QUERY_DISPLAY_ALL_PRODUCTS)

    def check_substitutes(self):
        """Method to check if there is a subsitute"""
        self.mysql.cur.execute(FIND_FOOD_SUBSTITUTED)

    def get_categories(self):
        """Method to get the categories"""
        self.mysql.cur.execute(QUERY_DISPLAY_ALL_CATEGORIES)
        for row in self.mysql.cur:
            self.list_products.append(row[1])
            print('{0} - {1}'.format(row[0], row[1]))

    def get_products(self):
        """Method to get the products"""
        self.mysql.cur.execute(QUERY_DISPLAY_ALL_PRODUCTS)
        for row in self.mysql.cur:
            if not row[2]:
                print('{0} - {1}'.format(row[0], row[1]))
            else:
                print('{0} - {1} - {2}'.format(row[0], row[1], row[2]))

    def display_details(self):
        """Method display products details"""
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
                   'Lien : {11}' + "\n"
                   'Magasins : {12}' + "\n"
                   'Catégorie : {13} ({i})').format(row[1], row[2], row[3].upper(), row[4], \
                    row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], \
                    row[13], row[14], i = self.list_ch[row[14] - 1]))

    def get_product_details(self):
        """Method to get product details"""
        self.mysql.cur.execute(QUERY_DISPLAY_PRODUCT_DETAILS.format(f1=choice_third_level))
        self.display_details()

    def insert_substitutes(self):
        """Method to insert the substitutes"""
        self.mysql.cur.execute(FIND_A_SUBSTITUTE)
        for row in self.mysql.cur:
            self.mysql.cur.execute(INSERT_A_SUBSTITUTE.format(table1="favourite", \
                table2="product", substitute=row[0]))
        self.mysql.cnx.commit()

    def display_substitutes(self):
        """Method to display a substitute"""
        self.mysql.cur.execute(FIND_FOOD_SUBSTITUTED)
        self.display_details()


    def replace_characters(self):
        """Method to replace characters categories"""
        for product in self.list_products:
            product = product.replace(' ', "-")
            product = product.replace('‘', "-")
            product = product.replace('à', "a")
            product = product.lower()
            self.list_products = []
            self.list_ch.append(product)

    def insert_products(self):
        """Method to insert the products"""
        self.replace_characters()
        r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0= \
            categories&tag_contains_0=contains&tag_0=" + self.list_ch[choice_second_level - 1] + \
            "&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action= \
            display&json=1")
        result = json.loads(r.text)
        for i in range(len(result["products"])):
            self.iD = i + 1
            try:
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
                self.category_id = choice_second_level
                if result["products"][i]["product_name_fr"] == "":
                    result["products"][i]["product_name"]
                else:
                    self.name = result["products"][i]["product_name_fr"]
                self.description = result["products"][i]["generic_name"]
                self.url_image = result["products"][i]["image_small_url"]
                self.url_page = result["products"][i]["url"]
                self.stores = result["products"][i]["stores"]
                val = (
                    self.iD, self.name, self.brand, self.nutri_score, self.calories, \
                    self.sugars, self.salts, self.lipids,\
                    self.proteins, self.description, self.location_available, self.url_image, \
                    self.url_page, self.stores, self.category_id)
                self.mysql.cur.execute(
                    QUERY_INSERT_ALL_PRODUCTS.format(table="product", f1="iD", f2="name", \
                    f3="brand", f4="nutri_score", f5="calories", f6="sugars", f7="salts", \
                    f8="lipids", f9="proteins", f10="description", \
                    f11="location_available", f12="url_image", f13="url_page",\
                    f14="stores", f15="category_id"), val)
                self.mysql.cnx.commit()
            except:
                pass

class Menu():
    action = Base_action()
    def __init__(self):
        self.message_input_category = "Entrez le chiffre correspondant à la catégorie et appuyez sur entrée."
        self.message_input_product = "Entrez le chiffre correspondant au produit et appuyez sur entrée."
        self.message_input = "Entrez le chiffre correspondant et appuyez sur entrée."
        self.display_first_level()

    def first_choice_first_level(self):
        """Method to display the first choice first level"""
        self.choice_first_level = str(input(self.message_input))
        if self.choice_first_level == "1":
            print('🤖 Oui. Voici ce que j‘ai. Veuillez choisir une catégorie.')
            self.action.fill_bdd()
            self.action.get_categories()
            self.first_choice_second_level()
        elif self.choice_first_level == "2":
            self.possibilities = []
            self.action.check_substitutes()
            for row in self.action.mysql.cur:
                    self.possibilities.append(row[0])
            if not self.possibilities:
                print('Aucun aliment substitué retrouvé.')
                print('1 - Quel aliment souhaitez-vous remplacer ?')
                print('2 - Retrouver mes aliments substitués.')
                self.first_choice_first_level()
            else:
                self.action.display_substitutes()
                print("Voici le substitut en question. Que voulez-vous faire maintenant ?")
                print('1 - Quel aliment souhaitez-vous remplacer ?')
                print('2 - Retrouver mes aliments substitués.')
                self.first_choice_first_level()
        else:
            self.first_choice_first_level()

    def first_choice_second_level(self):
        """Method to display the first choice second level"""
        global choice_second_level
        choice_second_level = int(input(self.message_input_category))
        self.action.mysql.cur.execute(QUERY_DISPLAY_ALL_PRODUCTS)
        self.action.check_category()
        self.possibilities = []
        for row in self.action.mysql.cur:
            self.possibilities.append(row[0]) 
        try:
            if choice_second_level in self.possibilities:
                self.action.insert_products()
                self.action.get_products()
                self.first_choice_third_level()
                print('🤖 Oui. Voici ce que j‘ai. Veuillez choisir un produit.')
        except ValueError:
            print("C'est pas un chiffre ca.")
            self.first_choice_second_level()
        else:
            print("Chiffre incorrect !")
            self.first_choice_second_level()
            
    def first_choice_third_level(self):
        """Method to display the first choice third level"""
        global choice_third_level
        choice_third_level = int(input(self.message_input_product))
        print('🤖 Oui. Voici ce que j‘ai.')
        self.possibilities = []
        self.action.check_product()
        for row in self.action.mysql.cur:
            self.possibilities.append(row[0])
        if choice_third_level in self.possibilities:
            self.action.get_product_details()
            self.first_choice_fourth_level()
        else:
            print("Chiffre incorrect !")
            self.first_choice_third_level()

    def first_choice_fourth_level(self):
        """Method to display the first choice fourth level"""
        choice_fourth_level = \
            str(input('Souhaitez-vous trouver un substitut plus sain au produit ?'))
        if choice_fourth_level == "oui" or choice_fourth_level == "OUI":
            print("Voici ci-dessous un substitut plus sain au produit précédent 🍎")
            self.action.insert_substitutes()
            self.action.display_substitutes()
            self.first_choice_fifth_level()
        elif choice_fourth_level == "non" or choice_fourth_level == "NON":
            self.action.mysql.cur.execute(NO_SUBSTITUTE)
            print("Tant pis 🍔. Retour au menu principal.")
            self.display_first_level()
        else:
            self.first_choice_fourth_level()

    def first_choice_fifth_level(self):
        """Method to display the first choice fifth level"""
        choice_fifth_level = str(input('Souhaitez-vous enregistrer ce ' + \
        'substitut dans la base de données ?'))
        if choice_fifth_level == "oui" or choice_fifth_level == "OUI":
            print("Substitut enregistré ! Retour au menu principal.")
            self.display_first_level()
        else:
            print("Tant pis 🍔. Retour au menu principal.")
            self.action.mysql.cur.execute(NO_SUBSTITUTE)
            self.display_first_level()

    def display_first_level(self):
        """Method to display the first level"""
        # FIRST WE NEED TO VERIFIY WHAT THE USER WANTS
        print('Bonjour et bienvenue dans Open Food Facts,' + '\n' + \
              'le programme qui vous aide à manger mieux 🍎.' + \
               'Vous pouvez quitter le programme a tout moment en appuyant sur ctrl + c')
        print('1 - Quel aliment souhaitez-vous remplacer ?')
        print('2 - Retrouver mes aliments substitués.')
        self.first_choice_first_level()
