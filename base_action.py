import pymysql
import requests

class Base_action(object):
    def __init__(self, cnx):
        self.db = self.connect
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def connect(self):
        try:
            # Try to connect to the database.
            cnx = pymysql.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  port = 8889,
                                  charset='utf8',
                                  db='openfoodfact')
        except pymysql.InternalError:
            print("No database found...")

        return cnx

    def get_data(self):
        self.name = name
        self.category = category


    def get_product_details(self):
        self.cnx.cursor.execute("""SELECT * WHERE id = %s""", ("5", ))
        rows = self.cursor.fetchall()
        for row in rows:
            print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))


    def menu():

        print('Bonjour et bienvenue dans Open Food Facts,' + '\n' +
              'le programme qui vous aide à manger mieux 🍎.')
        print('1 - Quel aliment souhaitez-vous remplacer ?')
        print('2 - Retrouver mes aliments substitués.')
        choice = input('Entrez le chiffre correspondant et appuyez sur entrée.')

        if choice == '1' or choice == ' 1' or choice == '1 ':
            print('🤖 Oui. Voici ce que j\'ai. Veuillez choisir une catégorie.' + '\n' +
                  'Entrez le chiffre correspondant et appuyez sur entrée.')
    menu()
