from classes import *

query_reset = "DELETE FROM category"

query_fill_bdd = ("INSERT INTO category(iD, name, url) VALUES(1, 'Boissons à l‘avoine', 'https://fr.openfoodfacts.org/categorie/boissons-a-l-avoine.json'), (2, 'Guacamoles', 'https://fr.openfoodfacts.org/categorie/guacamoles.json'), (3, 'Chips de Mais', 'https://fr.openfoodfacts.org/categorie/chips-de-mais.json'), (4, 'Pommes noisettes', 'https://fr.openfoodfacts.org/categorie/pommes-noisettes.json')")

query_display_all_categories = ('SELECT iD, name FROM category')

query_insert_all_products = ("INSERT INTO {table} ({f1}, {f2}, {f3}, {f4}, {f5}, {f6}, {f7}, {f8}, {f9}, {f10}, {f11}, {f12}, {f13}) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

query_display_all_products = "SELECT * FROM product INNER JOIN category ON product.category_id = category.iD"

query_display_product_details = "SELECT * FROM product WHERE id=2"

find_a_substitute = "SELECT * FROM product WHERE nutri_score='a'"

find_food_substituted = "SELECT * FROM favourite"
