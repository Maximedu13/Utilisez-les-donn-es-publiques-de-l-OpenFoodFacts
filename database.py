import pymysql
import mysql.connector

class connection():
    def __init__(self):
        self.cnx = None
        self.cursor = None
        self.config = { 'host':'localhost',
                                'user':'root',
                                'password':'root',
                                'port': 8889,
                                'charset':'utf8'}

    def executeScriptsFromFile(self, cursor, filename):
        # Open and read the file as a single buffer
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()
        # all SQL commands (split on ';')
        sqlCommands = sqlFile.split(';')
        # Execute every command from the input file
        for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                if command.rstrip() != '':         
                    cursor.execute(command)
            except ValueError as msg:
                print ("Command skipped: ", msg)

    def connect(self):
        try:
            # Trying to connect to the database...
            self.cnx = pymysql.connect(**self.config, db='Open_Food_Facts')
            self.cur = self.cnx.cursor()
        except pymysql.InternalError:
            print("No database found, the system is creating a new one...")
            self.cnx = pymysql.connect(**self.config)
            self.cur = self.cnx.cursor()
            self.executeScriptsFromFile(self.cur, "create_bdd.sql")   

    #https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=nutella&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=display&json=1