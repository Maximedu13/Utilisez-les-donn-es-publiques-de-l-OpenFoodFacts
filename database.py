"""database.py"""
import pymysql

class Connection():
    """Connection class"""
    def __init__(self):
        self.cnx = None
        self.cursor = None
        self.cur = None
        self.config = {'host':'localhost',
                       'user':'root',
                       'password':'root',
                       'port': 8889,
                       'charset':'utf8'}

    def execute_scripts_from_file(self, cursor, filename):
        """Method to import and execute sql file"""
        # Open and read the file
        f_d = open(filename, 'r')
        sql_file = f_d.read()
        f_d.close()
        # all SQL commands (split on ';')
        sql_commands = sql_file.split(';')
        # Execute every command from the input file
        for command in sql_commands:
            try:
                if command.rstrip() != '':
                    cursor.execute(command)
            except ValueError as msg:
                print("Command skipped: ", msg)

    def connect(self):
        """Method to connect"""
        try:
            # Trying to connect to the database...
            self.cnx = pymysql.connect(**self.config, db='Open_Food_Facts')
            self.cur = self.cnx.cursor()
        except pymysql.InternalError:
            # Creating the database...
            print("No database found, the system is creating a new one...")
            self.cnx = pymysql.connect(**self.config)
            self.cur = self.cnx.cursor()
            self.execute_scripts_from_file(self.cur, "create_bdd.sql")
