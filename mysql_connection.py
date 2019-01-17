import pymysql

try:
    # Try to connect to the database.
    cnx = pymysql.connect(user='root',
                          password='root',
                          host='localhost',
                          port = 8889,
                          charset='utf8',
                          db='GOT')
except pymysql.InternalError:
    print("No database found...")


https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=nutella&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=display&json=1
