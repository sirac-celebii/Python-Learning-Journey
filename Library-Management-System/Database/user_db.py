import sqlite3

class UserDatabase():
    def __init__(self):
        self.conn = sqlite3.connect("Library.db")
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        self.conn.commit()


    def add_user(self, user):
        self.cursor.execute("INSERT INTO Users (name) VALUES (?)",
                            (user.name,))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))
        self.conn.commit()

    def search_user(self, user_name):
        self.cursor.execute("SELECT * FROM Users WHERE name = ?", (user_name,))
        return self.cursor.fetchall()
    
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()
    
    def check_table(self):
        is_empty = self.table_is_empty()

        if is_empty:
            self.cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'Users'")
            self.conn.commit()
        else:
            return

    def table_is_empty(self):
        self.cursor.execute("SELECET 1 FROM Users LIMIT 1")

        return self.cursor.fetchone() is None
    
    def close(self):
        self.conn.close()