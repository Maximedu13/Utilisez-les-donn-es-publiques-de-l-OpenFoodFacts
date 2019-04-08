class Category:
    def __init__(self, iD, name, url):
        self.iD = iD
        self.name = name
        self.url = url


class Product:
    def __init__(self, iD, name, brand, nutri_score, calories, sugars, salts, lipids, proteins, description,
                 location_available, url_image, url_page, stores, category_id):
        self.iD = iD
        self.name = name
        self.brand = brand
        self.nutri_score = nutri_score
        self.calories = calories
        self.sugars = sugars
        self.salts = salts
        self.lipids = lipids
        self.proteins = proteins
        self.description = description
        self.location_available = location_available
        self.url_image = url_image
        self.url_page = url_page
        self.stores = stores
        self.category_id = category_id


class Favourite:
    def __init__(self, iD, name, brand, nutri_score, calories, sugars, salts, lipids, proteins, description,
                 location_available, url_image, url_page, stores, category_id):
        self.iD = iD
        self.name = name
        self.brand = brand
        self.nutri_score = nutri_score
        self.calories = calories
        self.sugars = sugars
        self.salts = salts
        self.lipids = lipids
        self.proteins = proteins
        self.description = description
        self.location_available = location_available
        self.url_image = url_image
        self.url_page = url_page
        self.stores = stores
        self.category_id = category_id
