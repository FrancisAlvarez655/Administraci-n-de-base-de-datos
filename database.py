import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )''')
        self.connection.commit()

    def insert_sale(self, product_name, quantity, price):
        self.cursor.execute('INSERT INTO sales (product_name, quantity, price) VALUES (?, ?, ?)', 
                            (product_name, quantity, price))
        self.connection.commit()

    def close(self):
        self.connection.close()