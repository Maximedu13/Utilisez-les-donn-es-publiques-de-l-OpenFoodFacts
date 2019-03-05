query_create_all_categories = ('INSERT INTO category(iD, name, url) \
VALUES(1, "Boissons à l\'avoine", "https://fr.openfoodfacts.org/categorie/boissons-a-l-avoine.json"), \
(2, "Guacamoles", "https://fr.openfoodfacts.org/categorie/guacamoles.json"), \
(3, "Chips de Mais", "https://fr.openfoodfacts.org/categorie/chips-de-mais.json"), \
(4, "Pommes noisettes", "https://fr.openfoodfacts.org/categorie/pommes-noisettes.json")\
WHERE NOT EXISTS (SELECT * FROM category)')


query_display_all_categories = ("SELECT iD, name FROM category")



query_display_all_products = ("SELECT iD, name FROM product INNER JOIN category ON product.category = category.name")

query_display_product_details = ("SELECT iD, name, description FROM product")
