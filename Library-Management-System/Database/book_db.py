import sqlite3

class BookDatabase():
    def __init__(self):
        self.conn = sqlite3.connect("Library.db")
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                author TEXT NOT NULL
            )    
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Loans(
                book_id INTEGER,
                user_id INTEGER ,
                FOREIGN KEY (book_id) REFERENCES Books (id),
                FOREIGN KEY (user_id) REFERENCES Users (id),
                PRIMARY KEY (user_id, book_id)
            )    
        """)

        self.conn.commit()

    def get_book_id(self, book_name):
        self.cursor.execute("SELECT id FROM Books WHERE name = ?", (book_name,))
        return self.cursor.fetchall()

    def add_book(self, book):
        self.cursor.execute("INSERT INTO Books (name, author) VALUES (?, ?)",
                            (book.name, book.author))
        self.conn.commit()

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
        self.conn.commit()

        self.check_table()

    def search_book(self, book_name):
        self.cursor.execute("SELECT * FROM Books WHERE name = ?", (book_name,))
        return self.cursor.fetchall()

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM Books")
        return self.cursor.fetchall()

    def borrow_book(self, book_id, user_id):
        self.cursor.execute("INSERT INTO Loans (book_id, user_id) VALUES (?, ?)",
                            (book_id, user_id))
        self.conn.commit()

    def return_book(self, book_id, user_id):
        self.cursor.execute("DELETE FROM Loans WHERE book_id = ? AND user_id = ?",
                            (book_id, user_id))
        self.conn.commit()

    def check_table(self):
        is_empty = self.table_is_empty()

        if is_empty:
            self.cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'Books'")
            self.conn.commit()
        else:
            return

    def table_is_empty(self):
        self.cursor.execute("SELECT 1 FROM Books LIMIT 1")

        return self.cursor.fetchone() is None # Return True if the first row in the Database is empty   
    
    def close(self):
        self.conn.close()