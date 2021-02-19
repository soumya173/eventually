
import sqlite3
import os

DB_NAME = os.path.join('swagger_server', 'database.db')

class DbInterface:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(DB_NAME)

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def select(self, sql):
        if not self.conn:
            return None
        rows = self.conn.execute(sql)
        return rows
