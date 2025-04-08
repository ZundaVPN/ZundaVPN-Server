import sqlite3, os, logging

class db_manager:
    def __init__(self):
        self.BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) # what
        self.DB_PATH = os.path.join(self.BASE_DIR, 'user.db') # the
        self.database = self.DB_PATH # fuck
        # self.con = sqlite3.connect(self.database)
        # self.cursor = self.con.cursor()

    def search(self, target: str, value: str): # WARNING : DO NOT get 'target' directly from user input. NEVER.
        logging.debug(f"search target is {target}, value is {value}")
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        query = f"SELECT * FROM usertable WHERE {target} = ?"
        cursor.execute(query, (value,))
        if cursor.fetchone() == None:
            return False
        return True

    def insert(self, target: str, value: str): # WARNING : DO NOT get 'target' directly from user input. NEVER.
        logging.debug(f"search target is {target}, value is {value}")
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        try:
            with con:
                query = f"INSERT INTO usertable ({target}) VALUES (?)"
                cursor.execute(query, (value,))
            return True
        except(sqlite3.Error, sqlite3.OperationalError) as e:
            logging.critical("DB MANAGER : insert failed\n", e)
            return False

    def reg_request(self, username: str, password: str): # WARNING : DO NOT get 'target' directly from user input. NEVER.
        logging.debug(f"reg_request username is {username}, password is {password}")
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        try:
            with con:
                cursor.execute("INSERT INTO usertable (username, token) VALUES (?, ?)", (username, password))
            return True
        except(sqlite3.Error, sqlite3.OperationalError) as e:
            logging.critical("DB MANAGER : insert failed\n", e)
            return False

db_manager = db_manager()