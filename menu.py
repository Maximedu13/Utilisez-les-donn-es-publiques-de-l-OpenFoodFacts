from base_action import Base_action

action = Base_action()

def menu():

    print('Bonjour et bienvenue dans Open Food Facts,' + '\n' +
          'le programme qui vous aide à manger mieux 🍎.')
    print('1 - Quel aliment souhaitez-vous remplacer ?')
    print('2 - Retrouver mes aliments substitués.')
    choice = input('Entrez le chiffre correspondant et appuyez sur entrée.')

    if choice == '1' or choice == ' 1' or choice == '1 ':
        print('🤖 Oui. Voici ce que j\'ai. Veuillez choisir une catégorie.' + '\n' +
              'Entrez le chiffre correspondant et appuyez sur entrée.')
        #Base_action.get_product_details(3017620429484, 3017620429484)
        #Base_action.get_product_details(7613033150395, 7613033150395)
        action.get_categories()
menu()
