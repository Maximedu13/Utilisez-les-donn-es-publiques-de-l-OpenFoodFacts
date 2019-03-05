from base_action import Base_action

action = Base_action()

def menu():

    print('Bonjour et bienvenue dans Open Food Facts,' + '\n' +
          'le programme qui vous aide à manger mieux 🍎.')
    print('1 - Quel aliment souhaitez-vous remplacer ?')
    print('2 - Retrouver mes aliments substitués.')

    #FIRST WE NEED TO VERIFIY IF THE USER WANTS
    choice_menu = input('Entrez le chiffre correspondant et appuyez sur entrée.')


    if choice_menu == '1' or choice_menu == ' 1' or choice_menu == '1 ':
        print('🤖 Oui. Voici ce que j\'ai. Veuillez choisir une catégorie.')
        action.fill_bdd_categories()
        action.get_categories()
        choice_category = input('Entrez le chiffre correspondant et appuyez sur entrée.')
        if type(choice_category) is int:
            action.get_products()
            product_choice = input('🤖 Oui. Voici ce que j\'ai. Veuillez choisir un produit.' \
            + '\n' + 'Entrez le chiffre correspondant et appuyez sur entrée.')
            if isinstance(product_choice, int):
                product_substitute_choice = input('🤖 Oui. Voici ce que j\'ai. \
                Souhaitez-vous trouver un substitut au produit ?' + '\n' + \
                'Entrez le chiffre correspondant et appuyez sur entrée.')
                print('1 - Oui')
                print('2 - Non.')

                #action.get_product_details()
        #Base_action.get_product_details(3017620429484, 3017620429484)
        #Base_action.get_product_details(7613033150395, 7613033150395)
menu()
