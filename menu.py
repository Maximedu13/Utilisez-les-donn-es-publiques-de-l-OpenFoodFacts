from base_action import Base_action

action = Base_action()

def menu():
    def __init__(self):
        self.message_input = "Entrez le chiffre correspondant et appuyez sur entrée."

    def first_choice_first_level():
        choice_first_level = int(input('Entrez le chiffre correspondant et appuyez sur entrée.'))
        if choice_first_level == 1:
            print('🤖 Oui. Voici ce que j‘ai. Veuillez choisir une catégorie.')
            action.fill_bdd()
            action.get_categories()
            first_choice_second_level()
        elif choice_first_level == 2:
            pass
        else :
            print('euh?')

    def first_choice_second_level():
        choice_second_level = int(input('Entrez le chiffre correspondant et appuyez sur entrée.'))
        print('🤖 Oui. Voici ce que j‘ai. Veuillez choisir un produit.')
        if type(choice_second_level) is int:
            action.insert_products()

    def display_first_level():
        #FIRST WE NEED TO VERIFIY WHAT THE USER WANTS
        print('Bonjour et bienvenue dans Open Food Facts,' + '\n' +
            'le programme qui vous aide à manger mieux 🍎.')
        print('1 - Quel aliment souhaitez-vous remplacer ?')
        print('2 - Retrouver mes aliments substitués.')
        first_choice_first_level()
    display_first_level()








    def first_choice_third_level():
        choice_third_level = input('🤖 Oui. Souhaitez-vous trouver un substitut au produit ?' \
        + '\n' + 'Entrez le chiffre correspondant et appuyez sur entrée.')
        print('1 - Oui')
        print('2 - Non.')
        if isinstance(choice_third_level, int):
            pass

                #action.get_product_details()
        #Base_action.get_product_details(3017620429484, 3017620429484)
        #Base_action.get_product_details(7613033150395, 7613033150395)
menu()
