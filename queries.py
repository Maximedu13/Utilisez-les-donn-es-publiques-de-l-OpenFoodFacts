"""Queries"""

QUERY_RESET = "DELETE FROM category"

QUERY_FILL_BDD = "INSERT INTO category(iD, name, url) \
VALUES(1, 'Boissons à l‘avoine', 'https://fr.openfoodfacts.org/categorie/boissons-a-l-avoine.json'), \
    (2, 'Guacamoles', 'https://fr.openfoodfacts.org/categorie/guacamoles.json'), \
    (3, 'Chips de Mais', 'https://fr.openfoodfacts.org/categorie/chips-de-mais.json'), \
    (4, 'Risottos', 'https://fr.openfoodfacts.org/categorie/risottos.json'), \
    (5, 'Yaourts sur lit de fruits', 'https://fr.openfoodfacts.org/categorie/yaourts-sur-lit-de-fruits.json'), \
    (6, 'Pavés de saumon', 'https://fr.openfoodfacts.org/categorie/paves-de-saumon.json')"

QUERY_DISPLAY_ALL_CATEGORIES = "SELECT iD, name FROM category"

QUERY_INSERT_ALL_PRODUCTS = "INSERT INTO {table} ({f1}, {f2}, {f3}, {f4}, {f5}, \
    {f6}, {f7}, {f8}, {f9}, {f10}, {f11}, {f12}, {f13}, {f14}, {f15}) \
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

QUERY_DISPLAY_ALL_PRODUCTS = "SELECT * FROM product INNER JOIN category \
    ON product.category_id = category.iD"

QUERY_DISPLAY_PRODUCT_DETAILS = "SELECT * FROM product WHERE id={f1}"

FIND_A_SUBSTITUTE = "SELECT * FROM product WHERE nutri_score='a' \
    ORDER BY RAND () LIMIT 1"

INSERT_A_SUBSTITUTE = "INSERT INTO {table1} SELECT * FROM {table2} WHERE id={substitute}"

FIND_FOOD_SUBSTITUTED = "SELECT * FROM favourite"

NO_SUBSTITUTE = "DELETE FROM favourite"
