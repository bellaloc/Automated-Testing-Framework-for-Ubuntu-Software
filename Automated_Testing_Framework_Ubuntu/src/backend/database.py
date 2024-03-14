# Automated_Testing_Framework_Ubuntu/src/backend/database.py

import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tests (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                result TEXT
                                )''')
        self.conn.commit()

    def insert_test_result(self, name, result):
        self.cursor.execute('''INSERT INTO tests (name, result) VALUES (?, ?)''', (name, result))
        self.conn.commit()

    def get_test_results(self):
        self.cursor.execute('''SELECT * FROM tests''')
        return self.cursor.fetchall()
